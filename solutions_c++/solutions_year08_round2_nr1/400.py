#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>

using namespace std;

typedef unsigned long long ull;

vector<pair<int, int> > trees;

ull cnt[16];

ull n, A, B, C, D, myX0, myY0, M;

int mk_rem (int a, int b) {
  return ((a % 3) << 2) | (b %3);
}

void solve () {
  trees.clear ();
  for (int i = 0; i < 16; ++i) 
      cnt [i] = 0;

  cin >> n >> A >> B >> C >> D >> myX0 >> myY0 >> M;

  ull X = myX0, Y = myY0;
  trees.push_back (make_pair (X, Y));
  for (int i = 1; i < n; ++i) {
    X = (A * X + B) % M;
    Y = (C * Y + D) % M;
    trees.push_back (make_pair (X, Y));
  }

  for (int i = trees.size ()-1; i >= 0; --i) {
    int x = trees[i].first % 3;
    int y = trees[i].second % 3;
    cnt[mk_rem(x, y)] += 1;
  }

  ull result = 0;
  for (int i = trees.size ()-1; i >= 1; --i) 
    for (int j = i-1; j >= 0; --j) {

      int x = (3 - ((trees[i].first + trees[j].first) % 3)) % 3;
      int y = (3 - ((trees[i].second + trees[j].second) % 3)) % 3;
      int r = mk_rem (x, y);
      result += cnt[r];

      if (r == mk_rem (trees[i].first, trees[i].second))
	--result;
      if (r == mk_rem (trees[j].first, trees[j].second))
	--result;
    }

  if ((result % 3) != 0) cerr << "Should not be!" << endl;
  result /= 3;
  cout << result << endl;
}

int main () {
  int N; cin >> N;
  for (int i = 1; i <= N; ++i) {
    cout << "Case #" << i << ": ";
    solve ();
  }
  return 0;
}

