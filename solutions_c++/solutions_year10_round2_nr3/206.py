#include<stdio.h>
#include<string.h>

#define MAX 505
#define MOD 100003

typedef __int64 LL;

LL c[MAX][MAX];
LL dp[MAX][MAX];

LL p2(int n){
	if(n==0)
		return 1;
	LL r = p2(n/2);
	r = (r*r)%MOD;
	if(n%2)
		r = (r*2)%MOD;
	return r;
}

LL f(int n,int r){
	if(n<2 || r < 0)
		return 0;

	if(r==1)
		return 1;

	LL& ret = dp[n][r];

	if(ret!=-1)	return ret;

	int i;
	ret = 0;
//	ret = (p2(n-r-1) * f(r,r-1)) % MOD;
	for(i=1;i<r;i++){
		ret = (ret + (f(r,i)*c[n-r-1][r-i-1])%MOD  ) % MOD;
	}
	return ret;
}

int main(){

	int n,i;
	LL res;

	memset(dp,-1,sizeof(dp));

	c[0][0] = 1;
	for(n=1;n<MAX;n++){
		c[n][0]=c[n][n]=1;
		for(i=1;i<n;i++)
			c[n][i] = (c[n-1][i-1] + c[n-1][i]) % MOD;
	}

	for(n=2;n<MAX;n++)
		for(i=1;i<n;i++)
			f(n,i);

	int T,N;
	scanf("%d",&T);
	for(N=1;N<=T;N++){
		scanf("%d",&n);

		res = 0;
		for(i=1;i<=n-1;i++)
			res = (res + f(n,i)) % MOD;

		printf("Case #%d: %d\n",N,res);

	}

	return 0;
}