#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
#include <cmath>
#include <set>
#include <queue>
using namespace std;
#define GI ({int t;scanf("%d",&t);t;})
#define LET(x,a) __typeof(a) x(a)
#define FOR(i,a,b) for(LET(i,a);i<(b);++i)
#define EACH(x,v) for(typeof(v.begin()) x=v.begin();x<v.end();x++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define mkp make_pair
#define sz size()
#define bset(i,j) (i&(1<<j))
#define INF (int)1e8
#define MAX 402
#define alog(x) exp(x*log(10.0))
typedef long long LL;
typedef double D;
typedef vector<int> VI;
using namespace std;
int main()
{
  int t=GI, kase=1;
  while(t--) {
     printf("Case #%d: ", kase++);
     int p=GI, k=GI, n=GI, f[n];
     REP(i,n) f[i]=GI;
     if(p*k < n) {
          printf("Impossible");
     }
     else {
          sort(f,f+n);          
          LL sum=0, ans=0, cnt=1;
          for(LL i=n-1, kk=1; i>=0; i--, kk++) {
               sum += f[i];          
               if(kk == k) {
                    kk = 0;
                    ans += sum * cnt;
                    cnt++, sum = 0;               
               }          
          }
          if(sum) ans+=sum*cnt;
          printf("%Ld", ans);
     }
     printf("\n");
 
  }
  
}
