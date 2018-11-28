#include<stdio.h>
#include<stdlib.h>
int C;
int D;
int P[222];
int V[222];
int dp[500000][222];
int base = 250000;
inline int abs(int a){
	if(a < 0)return -a;
	return a;
}
inline int min(int a,int b){
	if(a < b)return a;
	return b;
}
inline int max(int a,int b){
	if(a > b)return a;
	return b;
}
int main(){
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++){
		scanf("%d %d",&C,&D);
		for(int i=0;i<C;i++){
			scanf("%d %d",&P[i],&V[i]);
			P[i] = 2 * P[i] + base;
			V[i] = D * (V[i]) * 2;
			//printf("<%d,%d>\n",P[i],V[i]);
		}
		for(int i=0;i<500000 ;i++){
			for(int j=0;j<C;j++)
				dp[i][j] = 1000000000;
			
		}
		for(int i=1;i<base * 2;i++){
			for(int j=0;j<C;j++){
				dp[i][j] = dp[i-1][j];
				if(i - V[j] < 0){
					continue;
				}
				if(j == 0){
					dp[i][j] = min(dp[i][j],  max(abs(i - (V[j] - 2 * D) - P[j])  , abs(i - P[j]) ));
				}else{
					dp[i][j] = min(dp[i][j],        max(dp[i - V[j]][j - 1], max(    abs(i - (V[j] - 2 * D) - P[j])  , abs(i - P[j]) )));
					//if(i == 27){
					//	printf("dp[%d][%d] = %d <%d[%d][%d],%d,%d>\n", i,j,dp[i][j],dp[i - V[j]][j - 1],i - V[j],j - 1, abs(i - (V[j] - 2 * D) - P[j]),abs(i - P[j]));
					//}
				}
			}
		}
		/*
		for(int j=0;j<C;j++){
		for(int i=0;i<base * 2;i++){
			if(dp[i][j] != 1000000000)
				printf("%2d ",dp[i][j]);	
			else
				printf("__ ");
		}
		printf("\n");
		}*/

		printf("Case #%d: %.8lf\n",t + 1,dp[base * 2 - 1][C - 1] / 2.0);
		
	}
	return 0;
}
