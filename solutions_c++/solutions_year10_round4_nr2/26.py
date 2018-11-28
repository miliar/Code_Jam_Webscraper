#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
typedef long long LL;

#define inf 10000000000000000LL

int mm[1111], vv[1111];
LL dp[2222][40];
int main(){
	int nn,ii,n,b,c,cnt;
	scanf("%d",&nn);
	for(ii =1;ii<=nn;ii++){
		scanf("%d",&n);
		int po = 1; for(int i=0; i<n; i++)po*=2;
		for(int i=po-1; i>=0; i--){
			scanf("%d", &mm[i]);
			mm[i]=n-mm[i];
		}
		for(int i=po-1; i> 0; i--)scanf("%d", &vv[i]);
		for(int i=0; i<po; i++)for(int j=0; j<=n;j++){
			if(j>=mm[i])dp[i+po][j]=0;else dp[i+po][j]=inf;
		}
		for(int i=po-1; i> 0; i--){
			for(int j=0; j<=n;j++){
				dp[i][j] = min(min(dp[i*2][j]+dp[i*2+1][j], j==n?inf:(dp[i*2][j+1]+dp[i*2+1][j+1]+vv[i])),inf);
				//printf(" %I64d", dp[i][j]);
			}
			//printf("\n");
		}
		printf("Case #%d: %I64d\n",ii,dp[1][0]);
	}
	return 0;
}

