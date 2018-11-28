#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <string>
#include <algorithm>

#define FOREACH(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define REP(i, n) for(int i = 0; i < (n); i++)
#define CLEAR(a) memset(a, 0, sizeof(a))

using namespace std;

const int maxn = 55;

int a[maxn][maxn];
int n;

bool check(int x, int y) {
  return (x >= 0 && y >= 0 && x < n && y < n);
}

bool check_plus(int d) {
  REP(x, n)
    REP(y, n) {
      int xx = d-y;
      int yy = d-x;
      if (check(xx, yy) && a[x][y] != a[xx][yy])
	return false;
    }
  return true;
}

bool check_minus(int d) {
  REP(x, n)
    REP(y, n) {
      int xx = d+y;
      int yy = x-d;
      if (check(xx, yy) && a[x][y] != a[xx][yy])
	return false;
    }
  return true;
}
int main() {
  int T;
  cin >> T;
  for (int C = 1; C <= T; C++) {
    CLEAR(a);
    cin >> n;
    int x = 0;
    int y = 0;
    REP(i, n*n) {
      cin >> a[x][y];
      if (x == n-1) {
	x = y+1;
	y = n-1;
      }
      else if (y == 0) {
	y = x+1;
	x = 0;
      }
      else {
	x++;
	y--;
      }
    }
    /*
    REP(y, n) {
      REP(x,  n)
	cout << a[x][y];
      cout << endl;
    }
    */

    int p = 999;
    for (int d = 0; d < 2*n-1; d++)
      if (check_plus(d))
	p = min(p, abs(n-1-d));

    int m = 999;
    for (int d = -n+1; d <= n-1; d++)
      if (check_minus(d))
	m = min(m, abs(d));

    int r = n+p+m;
    cout << "Case #" << C << ": " << r*r-n*n << endl;
  }
}
