#include <stdio.h>
#include <string.h>

long long T,R,k,n,g[1001],iter[1001],cost[1001];

int main(){
	scanf("%lld",&T);
	for (long long TC=1; TC<=T; TC++){
		scanf("%lld %lld %lld",&R,&k,&n);
		for (int i=0; i<n; i++) scanf("%lld",&g[i]);

		memset(cost,-1,sizeof(cost));
		long long s = 0;
		cost[s] = iter[s] = 0;
		for (long long r=1; r<=R; r++){
			long long earn = 0, ps = s;
			for (int i=0; i<n && earn + g[s] <= k; i++){
				earn += g[s];
				s = (s+1) % n;
			}
			if (cost[s]!=-1){
				long long i = iter[s], j = r, L = j - i;
				long long ci = cost[s], cj = cost[ps] + earn, cL = cj - ci;
				memset(cost,-1,sizeof(cost));
				cost[s] = ci + cL * ((R - i)/L);
				iter[s] = 0;
				r = 0;
				R = (R - i) % L;
			} else {
				cost[s] = cost[ps] + earn;
				iter[s] = iter[ps] + 1;
			}
		}

		printf("Case #%lld: %lld\n",TC,cost[s]);
	}
}
