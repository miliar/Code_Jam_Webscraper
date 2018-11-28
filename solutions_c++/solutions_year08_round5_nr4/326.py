#include<iostream>
#define MODER 10007
using namespace std;

int dp[200][200];
bool ar[200][200];
int x,y,z,tc,i,j,h,w,r;

int main() {
	freopen("dsmal.in","r",stdin);
	freopen("dsmal.out","w",stdout);
	scanf("%d",&tc);
	for(x=1;x<=tc;x++) {
		scanf("%d %d %d",&h,&w,&r);
		memset(dp,0,sizeof(dp));
		memset(ar,0,sizeof(ar));
		for(i=0;i<r;i++) {
			scanf("%d %d",&z,&y);
			ar[z][y]=1;
		}
		dp[h][w]=1;
		for(i=h;i>=1;i--) {
			for(j=w;j>=1;j--) {
				if((i==h)&&(j==w)) continue;
				if(ar[i][j]) continue;
				dp[i][j]=(dp[i+1][j+2]+dp[i+2][j+1])%MODER;
			}
		}
		printf("Case #%d: %d\n",x,dp[1][1]);
	}	
	fclose(stdin);
	fclose(stdout);
	return 0;
}
