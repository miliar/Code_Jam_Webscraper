#include <iostream>
#include <vector>

using namespace std;

vector<int> o;
vector<int> b;

vector< pair<char, int> > v;

int main() {
  int t; cin >> t;
  for (int tt = 1; tt <= t; tt++) {
    o.clear(); b.clear(); v.clear();

    int n; cin >> n;
    for (int i = 0; i < n; i++) {
      char ch; int p; cin >> ch >> p;

      v.push_back(make_pair(ch, p));
      if (ch == 'O')
        o.push_back(p);
      else
        b.push_back(p);
    }

    int op = 1, bp = 1;
    int oi = 0, bi = 0;
    int i = 0;
    int time = 0;
    while (i < v.size()) {
      time++;

      bool ocanpush = false;
      bool bcanpush = false;

      if (oi < o.size()) {
        if (op < o[oi]) op++;
        else if (op > o[oi]) op--;
        else if (v[i].first == 'O') ocanpush = true;
      }

      if (bi < b.size()) {
        if (bp < b[bi]) bp++;
        else if (bp > b[bi]) bp--;
        else if (v[i].first == 'B') bcanpush = true;
      }

      if (ocanpush) oi++, i++;
      if (bcanpush) bi++, i++;
    }

    cout << "Case #" << tt << ": " << time << endl;
  }

  return 0;
}

