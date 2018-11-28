#include <stdio.h>
#include <math.h>
#include <string.h>
#include <vector>
#include <algorithm>
#include <stdlib.h>

using namespace std;

#define min(a,b) ((a)>(b)?(b):(a))
#define maxn 110
#define maxm 1010
#define maxl 110
#define INF 1000000

char names[maxn][maxl];
int n,m;
int mas[maxm];
int dp[maxm][maxn];

void init(){
	scanf("%d\n",&n);
	int i,j;
	for (i=0;i<n;i++){
		gets(names[i]);
		scanf("\n");
	}
	scanf("%d\n",&m);
	char s[maxl];
	for (i=0;i<m;i++){
		gets(s);
		scanf("\n");
		mas[i]=maxn-1;
		for (j=0;j<n;j++)
			if (strcmp(s,names[j])==0)
				mas[i]=j;
	}
}

void solve(){
	int i,j,k;
	for (i=0;i<n;i++)
		dp[0][i]=0;
	dp[0][mas[0]]=INF;
	for (i=1;i<m;i++){
		for (j=0;j<n;j++){
			dp[i][j]=dp[i-1][j];
			for (k=0;k<n;k++){
				dp[i][j]=min(dp[i][j],dp[i-1][k]+1);
			}
		}
		dp[i][mas[i]]=INF;
	}
	int res=dp[m-1][0];
	for (i=0;i<n;i++)
		res=min(res,dp[m-1][i]);
	if (res>=INF) res=-1;
	printf("%d\n",res);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,i;
	scanf("%d",&t);
	for (i=1;i<=t;i++){
		init();
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}