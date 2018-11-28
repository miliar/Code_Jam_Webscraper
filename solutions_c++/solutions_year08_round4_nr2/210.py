#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

const int INF = 1<<30;                
const double EPS = 1e-9;
const double PI = acos(-1.0);

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
typedef long double LD;

#define ALL(a) a.begin(),a.end()
#define PB push_back
#define MP make_pair
#define SZ(a) (int)a.size()
#define CLR(a,v) memset((a),(v),sizeof(a))
#define FOR(i,a,n) for(int i=(a);i<(n);++i)
#define FORD(i,a,n) for(int i=(a);i>=(n);--i)
#define REP(i,n) FOR(i,0,n) 



/// CODE HERE

int cross(int X0, int Y0, int X1, int Y1, int X2, int Y2) {
  return (X1-X0)*(Y2-Y0)-(X2-X0)*(Y1-Y0);
}

int gcd(int a, int b) {
  return b != 0 ? gcd(b, a%b) : a;
}

int gcd(int a, int b, int& x, int &y) {
  if (b == 0) {
    x = 1, y = 0;
    return a;
  }
  int x1, y1;
  int g = gcd(b, a%b, x1, y1);
  x = y1;
  y = x1-(a/b)*y1;
  return g;
}

int N, M, A;

int main() {
  freopen("B.in", "r", stdin);
  freopen("B.out", "w", stdout);

  int T;
  scanf("%d", &T);

  FOR(NT,1,T+1) {
    scanf("%d %d %d", &N, &M, &A);
    printf("Case #%d:", NT);
    bool ok = false;
    REP(X0,N+1) REP(Y0,M+1) REP(X1,N+1) REP(Y1,M+1) {
      if (X0 == X1 && Y0 == Y1) continue;
      if (X0 == 0 && Y0 == 0) continue;
      if (X1 == 0 && Y1 == 0) continue;
     /* int D = -X1*Y0+X0*Y1;
      D = A-D;
      int aa = X1-X0;
      int bb = Y0-Y1;
      int g = gcd(aa, bb);
      if (g == 0 || D % g) continue;
      int X2, Y2;
      gcd(aa, bb, Y2, X2);*/
      if (cross(0, 0, X0, Y0, X1, Y1) == A) {
        ok = true;
        printf(" %d %d %d %d %d %d\n",0, 0, X0, Y0, X1, Y1);
        goto end;
      }
    }
end:;
    if (!ok) {
      printf(" IMPOSSIBLE\n");
    }

  }


  return 0;
}