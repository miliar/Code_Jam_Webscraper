
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

int main()
{
   int T;
   scanf("%d", &T);
   FOR(tc,1,T) {
      int n,S,p;
      int a[101];
      scanf("%d%d%d",&n,&S,&p);
      REP(i,n) scanf("%d",&a[i]);
      int result = 0;
      REP(i,n) {
         if ((a[i] + 2) / 3 >= p) {
            ++result;
         } else if ((a[i] + 4) / 3 >= p && a[i] >= p && S > 0) {
            --S;
            ++result;
         }
      }
      printf("Case #%d: %d\n", tc, result);
   }
    return 0;
}
