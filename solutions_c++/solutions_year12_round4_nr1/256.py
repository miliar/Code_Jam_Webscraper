
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
VI v[max_n];
int d[max_n], l[max_n];

D sqr(D x) { return x*x; }

int main()
{
   int T,n;
   scanf("%d", &T);
   FOR(tc,1,T) {
      scanf("%d", &n);
      REP(i,n) {
         scanf("%d%d",&d[i],&l[i]);
      }
      scanf("%d", &d[n]);
      l[n] = 0;
      v[0].PB(d[0]);
      REP(i,n) {
         sort(ALL(v[i]));
         v[i].erase(unique(ALL(v[i])), v[i].end());
         int j = i + 1;
         while (j <= n) {
            int o = d[j] - d[i];
            D mx = sqrt(sqr(d[j] - d[i]) + sqr(l[i])) + 1e-9;
            int pos = lower_bound(ALL(v[i]), o) - v[i].begin();
            if (pos < SIZE(v[i]) && v[i][pos] < mx) {
               if (d[j] - d[i] > l[j]) {
                  v[j].PB(l[j]);
               } else {
                  v[j].PB(d[j]-d[i]);
               }
            }
            ++j;
         }
      }
      fprintf(stderr, "%d\n",tc);
      printf("Case #%d: ",tc);
      if (SIZE(v[n])) printf("YES\n"); else printf("NO\n");
      REP(i,n+1) v[i].clear();
   }
   return 0;
}
