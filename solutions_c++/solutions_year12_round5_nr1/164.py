
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

class level {
   public:
      int p,l,id;

      bool operator<(const level &L) const {
         int A = l * L.p, B = L.l * p;
         if (A == B) return id < L.id;
         return A < B;
      }
} t[1010];

int main()
{
   int T,n;
   scanf("%d", &T);
   FOR(tc,1,T) {
      scanf("%d", &n);
      REP(i,n) { scanf("%d",&t[i].l); t[i].id = i; }
      REP(i,n) scanf("%d",&t[i].p);
      sort(t, t + n);
      printf("Case #%d:",tc);
      REP(i,n) printf(" %d",t[i].id);
      printf("\n");
   }
    return 0;
}
