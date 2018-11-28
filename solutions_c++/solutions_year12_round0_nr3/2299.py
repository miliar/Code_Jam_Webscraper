
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
   int T,A,B;
   scanf("%d", &T);
   FOR(tc,1,T) {
      scanf("%d%d",&A,&B);
      char buf[100];
      set<PII> s;
      FOR(p,A,B) {
         sprintf(buf, "%d", p);
         int d = strlen(buf);
         FOR(i,1,d-1) if (buf[i] != '0') {
            int tmp = 0;
            FOR(j,i,d-1) tmp = tmp * 10 + buf[j] - '0';
            FOR(j,0,i-1) tmp = tmp * 10 + buf[j] - '0';
            if (p < tmp && tmp <= B) {
               s.insert(MP(p,tmp));
            }
         }
      }
      printf("Case #%d: %d\n",tc,SIZE(s));
   }
    return 0;
}
