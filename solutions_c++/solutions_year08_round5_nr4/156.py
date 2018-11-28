#include<stdio.h>

#define MAX 125

#define OFF 5

int R,C;
int mat[MAX][MAX];
int dp[MAX][MAX];

int main(){

	int r,c,n,i;

	int T,N;

	scanf("%d",&T);

	for(N=1;N<=T;N++){
		
		scanf("%d%d%d",&R,&C,&n);

		for(r=0;r<=R+OFF;r++)
			for(c=0;c<=C+OFF;c++)
				dp[r][c] = 0;

		for(i=0;i<n;i++){
			scanf("%d%d",&r,&c);
			mat[r][c] = N;
		}

		dp[OFF+1][OFF+1] = 1;

		for(r=2;r<=R;r++){
			for(c=2;c<=C;c++){
				
				if(mat[r][c]==N)
					continue;

				dp[OFF+r][OFF+c] = (dp[OFF+r-2][OFF+c-1] + dp[OFF+r-1][OFF+c-2]) % 10007;
			}
		}

		printf("Case #%d: %d\n",N,dp[R+OFF][C+OFF]);

	}

	return 0;
}