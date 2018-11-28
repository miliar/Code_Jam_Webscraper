#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;
typedef long long LL;
#define mal 3000000

LL dp[mal];

int n;
LL l;
int a[1000];

int main(){
	int nnt, ntt;
	scanf("%d", &nnt);
	for(ntt = 1; ntt<=nnt; ntt++){
		scanf("%lld%d", &l, &n);
		for(int i=0; i<n; i++)scanf("%d", &a[i]);
		sort(a, a+n);
		memset(dp, -1, sizeof(dp));
		dp[0]=0;
		for(int i=0; i<mal && i<=l; i++){
			for(int j=0; j<n; j++){
				if(a[j]>i)break;
				if(dp[i-a[j]]<0)continue;
				LL t = dp[i-a[j]]+1;
				if(dp[i]==-1 || dp[i]>t)dp[i]=t;
			}
		}
		/*for(int i=0; i<=100; i++){
		 printf("%4d: %8lld", i, dp[i]);
		 if(i%5==0)printf("\n");
		 }*/
		
		LL ans = -1;
		
		if(l<mal)ans = dp[l];else{
			LL mu = l / a[n-1];
			for(LL i = mu; i >=0; i--){
				int w = l-i*a[n-1];
				//printf(" w=%d\n", w);
				 if(w>=mal)break;
				if(dp[w]<0)continue;
				LL tans = dp[w] + i;
				if(ans < 0 || tans < ans)ans = tans;
			}
		}
		printf("Case #%d: ", ntt);
		if(ans<0)printf("IMPOSSIBLE\n");else
		printf("%lld\n", ans);
	}
	return 0;
}

