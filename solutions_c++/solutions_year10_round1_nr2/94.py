#include <cstdio>
#include <algorithm>
using namespace std;

int a,b,c,n,m,p[105],T[260],dp[105][260],AC;

int main(){
	scanf("%d",&c);
	for (int tc=1;tc<=c;tc++){
		scanf("%d%d%d%d",&a,&b,&m,&n);
		for (int i=1;i<=n;i++) scanf("%d",&p[i]);
		for (int i=0;i<=255;i++) dp[0][i]=0;
		for (int i=1;i<=n;i++){
//delete
			for (int j=0;j<=255;j++) dp[i][j]=dp[i-1][j]+a;
//change
			for (int j=0;j<=255;j++){
				for (int k=0;k<=255;k++)
					if (abs(k-j)<=m) dp[i][j]=min(dp[i][j],dp[i-1][k]+abs(p[i]-j));
			}
//insert
			if (!m) continue;
			for (int j=0;j<=255;j++) T[j]=dp[i][j];
			for (int j=0;j<=255;j++){
				for (int k=0;k<=255;k++) dp[i][k]=min(dp[i][k],T[j]+b*((abs(k-j)+m-1)/m));
			}
		}
		AC=-1;
		for (int i=0;i<=255;i++)
			if (AC==-1||dp[n][i]<AC) AC=dp[n][i];
		printf("Case #%d: %d\n",tc,AC);
	}
	return 0;
}
