#include<stdio.h>

#define MAX 40005
#define INF 1000000000

#define _min(a,b)	(((a)<(b))?(a):(b))

int n;
int dp[MAX][2];

int g[MAX],c[MAX];

int main(){

	int T,N,v;
	int i,p,q;

	scanf("%d",&T);

	for(N=1;N<=T;N++){

		scanf("%d%d",&n,&v);
		for(i=1;i<=n;i++)
			dp[i][0]=dp[i][1] = INF;

		for(i=1;i<=n/2;i++)
			scanf("%d%d",&g[i],&c[i]);
		
		for(;i<=n;i++){
			scanf("%d",&g[i]);
			dp[i][g[i]] = 0;
		}


		for(i=n/2;i>=1;i--){
			
			if(g[i]==1){	//and
				for(p=0;p<=1;p++)for(q=0;q<=1;q++)
					dp[i][p && q] = _min( dp[i][p && q] , dp[2*i][p] + dp[2*i+1][q] );
				if(c[i]==1)for(p=0;p<=1;p++)for(q=0;q<=1;q++)
					dp[i][p || q] = _min( dp[i][p || q] , dp[2*i][p] + dp[2*i+1][q] + 1 );
			}
			else{			//or
				for(p=0;p<=1;p++)for(q=0;q<=1;q++)
					dp[i][p || q] = _min( dp[i][p || q] , dp[2*i][p] + dp[2*i+1][q] );
				if(c[i]==1)for(p=0;p<=1;p++)for(q=0;q<=1;q++)
					dp[i][p && q] = _min( dp[i][p && q] , dp[2*i][p] + dp[2*i+1][q] + 1 );
			}
		}

		if(dp[1][v] == INF)
			printf("Case #%d: IMPOSSIBLE\n",N);
		else
			printf("Case #%d: %d\n",N,dp[1][v]);
		
//		printf("Case #1: %d\n",102931023);

	}

	return 0;
}