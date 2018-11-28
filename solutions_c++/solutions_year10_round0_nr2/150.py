#include <iostream>
#include <algorithm>

using namespace std;

int nums[1000];

int gcd(int a,int b){
	if (a==0) return b;
	if (b==0) return a;
	if (a>b) return gcd(a%b,b);
	return gcd(a,b%a);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	scanf("%d",&t);
	for (int tt=1; tt<=t; tt++){
		int n;
		scanf("%d",&n);
		int dp[10];
		for (int i=1; i<=n; i++)
			scanf("%d",&dp[i]);
		sort(dp+1,dp+n+1);
		int v=0;
		for (int i=1; i<=n; i++)
			for (int j=i+1; j<=n; j++)
				v++, nums[v]=dp[j]-dp[i];
		
		printf("Case #%d: ",tt);
		if (n==1) printf("0\n");

		int T=nums[1];
		for (int i=1; i<=v; i++)
			T=gcd(T,nums[i]);

		int res=dp[1]%T;
		res=T-res;
		if (res==T) res=0;
		printf("%d\n",res);
	}

	return 0;
}