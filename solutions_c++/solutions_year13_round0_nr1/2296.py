#include <set>
#include <list>
#include <map>
#include <queue>
#include <stack>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <climits>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#define MID(x,y) ( ( x + y ) >> 1 )
#define L(x) ( x << 1 )
#define R(x) ( x << 1 | 1 )
#define REP(i,t) for(int i=0; i<(t); i++)
#define FOR(i,s,t) for(int i=(s); i<(t); i++)
#define FORD(i,a,b) for (int i = (a); i >= (b); i--)
#define FORL(i,s,t) for(L i=(s); i<(t); i++)
#define BUG puts("here!!!")
#define STOP system("pause")
#define file_r(x) freopen(x, "r", stdin)
#define file_w(x) freopen(x, "w", stdout)
#define EPS 1e-6
#define EQ(a, b) (fabs((a) - (b)) <= EPS)
#define POS(a) ((a) >= EPS)
#define NEG(a) ((a) <= -EPS)
#define BG(a, b) ((a) - (b) >= EPS)
#define LS(a, b) ((b) - (a) >= EPS)
#define CLR(a, x) memset( a, x, sizeof( a ) )
#define PI (atan(1.0) * 4)
#define SQ(x) ((x) * (x))
#define DIST(x1, y1, x2, y2) (sqrt(SQ((x1) - (x2)) + SQ((y1) - (y2))))
#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define LOG2(x) (log(x) / log(2))
#define XX first.first
#define XY first.second
#define YX second.first
#define YY second.second

using namespace std;
typedef unsigned long long ULL;
typedef long long LL;
typedef pair<double, double> Pd;
typedef pair<int, int> Pi;
typedef pair<LL, LL> Pl;

void up(char c, int& x, int& t, int& o) {
  if (c == 'X')
    x++;
  else if (c == 'T')
    t++;
  else if (c == 'O')
    o++;
}

// 1=X, 0=Draw, -1=O
int calc(string v[4]) {
  REP(i, 4) {
    int x = 0, t = 0, o = 0;
    REP(j, 4)
      up(v[i][j], x, t, o);
    if (x + t == 4)
      return 1;
    if (o + t == 4)
      return -1;
  }
  REP(i, 4) {
    int x = 0, t = 0, o = 0;
    REP(j, 4)
      up(v[j][i], x, t, o);
    if (x + t == 4)
      return 1;
    if (o + t == 4)
      return -1;
  }
  int x = 0, t = 0, o = 0;
  REP(i, 4) {
    up(v[i][i], x, t, o);  
  }
  if (x + t == 4)
    return 1;
  if (o + t == 4)
    return -1;

  x = 0, t = 0, o = 0;
  REP(i, 4) {
    up(v[i][3 - i], x, t, o);  
  }
  if (x + t == 4)
    return 1;
  if (o + t == 4)
    return -1;
  int dot = 0;
  REP(i, 4)
    REP(j, 4)
      dot += v[i][j] == '.';
  if (dot)
    return 2;
  return 0;
}

int main()
{
  int t, p = 0;
  cin >> t;
  while (t--) {
    p++;
    string v[4];
    REP(i, 4)
      cin >> v[i];
    int ans = calc(v);
    cout << "Case #" << p << ": "; 
    if (ans == 1)
      cout << "X won";
    else if (ans == 0)
      cout << "Draw";
    else if (ans == -1)
      cout << "O won";
    else
      cout << "Game has not completed";
    cout << endl;
  }
  return 0;
}

