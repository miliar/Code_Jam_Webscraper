#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

char str[50001];
int dp[16][1<<16][16];
int a[16][16];
int n,m;

void run(int T) {
	scanf("%d %s",&n,str);
	m=strlen(str)/n;
	memset(a,0,sizeof(a));
	for(int i=0;i<m;i++) {
		for(int j=0;j<n;j++)
			for(int k=0;k<n;k++)
				if (str[i*n+j]!=str[i*n+k]) a[j][k]++;
	}
	memset(dp,0x7f,sizeof(dp));
	for(int i=0;i<n;i++) dp[i][1<<i][i]=0;
	int mask=(1<<n)-1;
	for(int i=1;i<=mask;i++) {
		for(int j=0;j<n;j++)
			if (i&(1<<j))
				for(int k=0;k<n;k++)
					if (i&(1<<k)) {
						for(int l=0;l<n;l++)
							if (!(i&(1<<l)))
								dp[j][i|(1<<l)][l]=min(dp[j][i|(1<<l)][l],dp[j][i][k]+a[k][l]);
					}
	}
	int ret=strlen(str);
	for(int i=0;i<n;i++)
		for(int j=0;j<n;j++) {
			int t=dp[i][mask][j];
			for(int k=0;k<m-1;k++)
				if (str[k*n+i]!=str[k*n+n+j]) t++;
			ret=min(ret,t);
		}
	printf("Case #%d: %d\n",T,ret+1);
}

int main() {
	int N,cs=0;
	for(scanf("%d",&N);N--;) run(++cs);
	return 0;
}
