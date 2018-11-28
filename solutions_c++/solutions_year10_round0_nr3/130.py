#include<cstdio>
#include<cstring>
using namespace std;
typedef long long ll;
int next[1024];
ll gain[1024];
ll g[1024];
int chk[1024 * 1024];
ll pioneer[1024*1024];
int main() {
	int T, e = 0;
	scanf("%d",&T);
	while(T--) {
		ll R, k, N, allsum = 0;
		scanf("%lld%lld%lld",&R, &k, &N);
		for(int i=0;i<N;++i) {
			int x;
			scanf("%d",&x); // <= 10^7
			g[i] = x;
			allsum += g[i];
		}
		
		printf("Case #%d: ", ++e);
		ll money = 0;
		
		if(allsum <= k) {
			money = R; money*= allsum;
			printf("%lld\n",money);
			continue;
		}
		
		// naive pre process in n^2 (can do in n, but why bother)
		for(int i=0;i<N;i++) {
			int sum = 0, x = i;
			for(int j=0;j<N;j++,x++) {
				if(x==N) x=0;
				if(sum+g[x] > k) {
					next[i] = x;
					gain[i] = sum;
					break;
				}
				sum+= g[x];
			}
		}
		
		memset(chk, 0, sizeof(chk));		
		int pt = 0, npt;
		for(int t=0;t<R;t++) {		
			npt = next[pt];
			if(chk[pt*1001 + npt]) { // already visited
				int s = chk[pt*1001 + npt] - 1;
				ll intv;
				intv = pioneer[t-1] - (s == 0 ? 0 : pioneer[s-1]);
				ll period = t - s;
				money += ((R-t)/period) * intv;
				if((R-t)%period) {
					money += pioneer[s + (R-t)%period - 1] - (s==0 ? 0 : pioneer[s-1]);
				}
				break;
			}
			chk[pt * 1001 + npt] = t + 1;
			money += gain[pt];		
			pioneer[t] = money;
			pt = npt;
		}
		printf("%lld\n",money);
	}
	return 0;
}
