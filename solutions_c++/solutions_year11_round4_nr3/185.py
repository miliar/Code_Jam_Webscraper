#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)
#define FORE(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
typedef long long ll;

const int N=2000000;
int _,ans;
int pie[N],p[N],pot[N],dz[N];
int P;
ll n;

int main() {
   scanf("%d",&_);
      
      int en = 1000000+20;
      P=0;
      dz[1]=-1;
      for(int i=2;i<=en;++i) dz[i]=-1,p[i]=0;
      for(int i=2;i<=en;++i) if (!p[i]) {
	 pie[P++] = i;
	 for(int j=i; j<=en; j+=i) {
	    p[j]=1;
	    if (dz[j] == -1) dz[j] = P-1;
	 }
      }

   REP(test,_) {
      scanf("%lld",&n);
      int en = min(n, (ll)sqrtl(n)+20);


//      for(int i=1;i<=n;++i) printf("%d:%d ",i,dz[i]); puts("");
      REP(i,P) pot[i]=0;
/*      for(int i=1;i<=en;++i) {
	 
	 int I=i;
	 int lastdzi=-1,cnt=0;
	 while (dz[I] != -1) {
	    if (dz[I] == lastdzi) ++cnt;
	    else {
	       pot[lastdzi] = max(pot[lastdzi], cnt);
	       cnt=1, lastdzi = dz[I];
	    }
	    I /= pie[ dz[I] ];
	 }
	 if (lastdzi!=-1) pot[lastdzi] = max(pot[lastdzi],cnt);
      }*/

      REP(i,P) {
	 ll j=1;
	 while (j <= n/pie[i] ) j*=pie[i], ++pot[i];
      }


//      REP(i,P) printf("%d:%d ",pie[i],pot[i]); puts("");
      ans = 1 - (n==1);
      REP(i,P) {
	 ans += max(0,pot[i]-1);
      }
      printf("Case #%d: %d\n",test+1,ans);
   }
}
