#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>

#define FOREACH(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define REP(i, n) for(int i = 0; i < (n); i++)
#define CLEAR(a) memset(a, 0, sizeof(a))

using namespace std;

const int maxn = 110;

bool a[2][maxn][maxn];
int n, m;

int main() {
  int T;
  cin >> T;
  for (int C = 1; C <= T; C++) {
    CLEAR(a);
    int k;
    n = m = 0;
    cin >> k;
    REP(i, k) {
      int r1, r2, c1, c2;
      cin >> r1 >> c1 >> r2 >> c2;
      for (int r = r1; r <= r2; r++)
	for (int c = c1; c <= c2; c++)
	  a[0][r][c] = true;
      n = max(n, r2);
      m = max(m, c2);
    }
    n++;
    m++;
    int old, now = 0;
    int t = 0;
    while (true) {
      t++;
      old = now;
      now = 1-now;
      REP(r, n)
	REP(c, m) {
	  if (a[old][r][c]) 
	    a[now][r][c] = ((r > 0 && a[old][r-1][c]) || (c > 0 && a[old][r][c-1]));
	  else
	    a[now][r][c] = (r > 0 && a[old][r-1][c] && c > 0 && a[old][r][c-1]);
	}

      bool live = false;
      REP(r, n) 
	REP(c, m)
	  if (a[now][r][c])
	    live = true;
      if (!live)
	break;
    }
    cout << "Case #" << C << ": " << t << endl;
  }
}
