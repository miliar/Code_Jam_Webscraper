#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

int t, na, nb, a, b;
vector<pair<int, int> > aj, bj;

pair<int, int> read_j () {
  int t1, t2, t3, t4;
  char colon;
  cin >> t1 >> colon >> t2 >> t3 >> colon >> t4;
  return make_pair (60*t1 + t2, 60*t3+t4+t);
}

void solve () {
  cin >> t >> na >> nb;
  a = b = 0;

  for (int i = 0; i < na; ++i) {
    aj.push_back (read_j ());
  }
  for (int i = 0; i < nb; ++i) {
    bj.push_back (read_j ());
  }

  sort (aj.begin (), aj.end ());
  reverse (aj.begin (), aj.end ());
  sort (bj.begin (), bj.end ());
  reverse (bj.begin (), bj.end ());

  priority_queue<int> qa, qb;
  while (!aj.empty() || !bj.empty()) {
    if (aj.empty () || (!bj.empty() && aj.back().first > bj.back().first)) {
      // use b
      pair<int, int> travel = bj.back();
      bj.pop_back ();
      if (qb.empty () || (-qb.top()) > travel.first) {
	++b;
      } else {
	qb.pop ();
      }
      qa.push (- travel.second);
    } else {
      // use a 
      pair<int, int> travel = aj.back();
      aj.pop_back ();
      if (qa.empty () || (-qa.top()) > travel.first) {
	++a;
      } else {
	qa.pop ();
      }
      qb.push (- travel.second);
    }
  }

  cout << a << " " << b << endl;
}

int main () {
  int N;
  cin >> N;
  for (int i = 0; i < N; ++i) {
    cout << "Case #" << (i+1) << ": ";
    solve ();
  }

  return 0;
}

