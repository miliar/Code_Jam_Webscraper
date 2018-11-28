#include <iostream>
#include <algorithm>
using namespace std;
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(a,b,c) for(int a=b;a<=c;a++)

int w,h,n;
int x[20],y[20];
int dp[200][200];
int mask[200][200];

int main(){
	int d;
	scanf("%d",&d);
	FOR(test,1,d){
		memset(dp,0,sizeof(dp));
		memset(mask,0,sizeof(mask));
		scanf("%d %d %d",&h,&w,&n);
		REP(i,n){
			scanf("%d %d",&x[i],&y[i]);
			mask[ x[i] ][ y[i] ] = 1;
		}
		dp[1][1]=1;
		FOR(i,1,h)FOR(j,1,w)if( !mask[i][j] ){
			dp[i+1][j+2]=(dp[i+1][j+2]+dp[i][j])%10007;
			dp[i+2][j+1]=(dp[i+2][j+1]+dp[i][j])%10007;
		}
		printf("Case #%d: %d\n",test,dp[h][w]);
	}
	return 0;
}
