#ifndef DEBUG
# define dbg(x)
# define NDEBUG
#else
# define dbg(x) x
#endif
#include <cstdio>
#include <cstring>
#include <cstdarg>
#include <cassert>
#include <algorithm>
using namespace std;
#define FR(i,a,b) for(int i=(a);i<(b);i++)
#define FOR(i,b) FR(i,0,b)
typedef long long ll;
typedef pair<int,int> pii;
const ll INF=1000000000000000000LL;
const int MAXT=100,MAXS=100,MAXN=100;
int T,S,N,P;
int sums[MAXN];
bool got[MAXN];

int main() {
	freopen("dancing.in","r",stdin);
	freopen("dancing.out","w",stdout);
	scanf("%d",&T);
	FOR(t,T) {
		scanf("%d %d %d",&N,&S,&P);
		FOR(i,N) {
			got[i]=false;	
			scanf("%d",sums+i);
		}
		int min1=max(0,P-1)*2+P;
		int min2=max(0,P-2)*2+P;
		int sl=S;
		FOR(i,N) {
			if(sums[i]>=min1) {
				got[i]=true;
			} else if(sl>0&&sums[i]>=min2) {
				got[i]=true;
				sl--;
			}
		}
		int nr=0;
		FOR(i,N) {
			if(got[i]) {
				nr++;
			}
		}
		printf("Case #%d: %d\n",t+1,nr);
	}
	return 0;
}
