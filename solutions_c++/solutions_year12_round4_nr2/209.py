
// UW forfiters
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
using namespace std;
#define FI first
#define SE second
#define MP make_pair
#define PB push_back
typedef long long LL;
typedef double D;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<string> VS;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))

const int max_n = 10010;
D x[max_n], y[max_n], R[max_n];
PII r[max_n];
int g[max_n];
const int M = 1000000000;

D sqr(D a) { return a*a; }

bool ok(D X, D Y, int k) {
   REP(i,k) if (sqr(X-x[i]) + sqr(Y-y[i]) < sqr(R[i])) return false;
   return true;
}

D losuj(int zakres) {
   D a = rand() % M;
   D b = rand() % zakres;
   return (D)a/M + b;
}

int main()
{
   int T,n,W,L;
   scanf("%d", &T);
   FOR(tc,1,T) {
      scanf("%d%d%d",&n,&W,&L);
      REP(i,n) { scanf("%d", &r[i].FI); r[i].SE = i; }
      sort(r, r + n);
      reverse(r, r + n);
      REP(i,n) g[r[i].SE] = i;
      REP(i,n) {
         while (1) {
            D xa = losuj(W);
            D ya = losuj(L);
            if (ok (xa,ya,i)) {
               x[i] = xa;
               y[i] = ya;
               R[i] = r[i].FI * 2;
               break;
            }
         }
      }
      printf("Case #%d:",tc);
      REP(i,n) printf(" %.6lf %.6lf",x[g[i]],y[g[i]]);
      printf("\n");
   }
   return 0;
}
