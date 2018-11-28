#include <stdio.h>
#include <string.h>

#include <algorithm>

using namespace std;

#define MAX 110
#define INFTY 0x3F3F3F3F
#define MAXL 10000000

int dp[MAXL];

int gcd(int a,int b) {
	while(b) {
		int r=a%b;
		a=b;
		b=r;
	}
	return a;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	scanf("%d",&tests);
	for(int test=1;test<=tests;++test) {
		long long l;
		int n;
		int b[MAX];
		scanf("%lld%d",&l,&n);
		for(int i=0;i<n;++i)
			scanf("%d",&b[i]);
		printf("Case #%d: ",test);
		int d=0;
		for(int i=0;i<n;++i)
			d=gcd(d,b[i]);
		if(l%d) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		sort(b,b+n);
		memset(dp,0x3F,sizeof(dp));
		dp[0]=0;
		for(int i=1;i<MAXL;++i)
			for(int j=0;j<n;++j)
				if(b[j]<=i) {
					int t=1+dp[i-b[j]];
					if(t<dp[i])
						dp[i]=t;
				}
		if(l<MAXL) {
			if(dp[l]==INFTY)
				printf("IMPOSSIBLE\n");
			else
				printf("%d\n",dp[l]);
		}
		else {
			long long ans=(l-MAXL)/b[n-1];
			if(l-ans*b[n-1]>=MAXL) ++ans;
			ans+=dp[l-ans*b[n-1]];
			printf("%lld\n",ans);
		}
	}
	return 0;
}
