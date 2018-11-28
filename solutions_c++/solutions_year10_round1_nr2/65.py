#include <iostream>
#include <string>
#include <cstring>
#include <string.h>
#include <algorithm>
#include <set>
#include <map>
#include <vector>

using namespace std;

int a[200];
int d,i,m,n;
int dp[200][300];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	scanf("%d",&t);

	for (int tt=1; tt<=t; tt++){
		scanf("%d%d%d%d",&d,&i,&m,&n);

		for (int j=1; j<=n; j++)
			scanf("%d",&a[j]);

		int res=1000000000;

		memset(dp,-1,sizeof(dp));
		for (int j=0; j<256; j++)
			dp[0][j]=0;

		for (int j=1; j<=n; j++)
			for (int k=0; k<256; k++){
				if (dp[j-1][k]!=-1) dp[j][k]=dp[j-1][k]+d;
				for (int l=0; l<256; l++)
				if (dp[j-1][l]!=-1){
					int tres=abs(k-a[j]);
					if (m==0&&k==l){
						dp[j][k]=min(dp[j][k],dp[j-1][l]+tres);
						continue;
					} else
						if (m==0) continue;
					int tk=abs(k-l)/m;
					if (abs(k-l)%m==0) tk--;
					if (abs(k-l)<=m) tk=0;
					dp[j][k]=min(dp[j][k],dp[j-1][l]+i*tk+tres);
				}
			}

		for (int j=0; j<256; j++)
			if (dp[n][j]!=-1) res=min(res,dp[n][j]);

		printf("Case #%d: %d\n",tt,res);
	}

	return 0;
}