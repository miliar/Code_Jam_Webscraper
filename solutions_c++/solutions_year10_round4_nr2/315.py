#include <iostream>
#include <string>
#include <string.h>
#include <cstring>
#include <algorithm>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <bitset>
#pragma comment (linker, "/STACK:256000000")

#define INF 1000000000

using namespace std;

int p,n;
int m[10000],cost[10000];
int dp[10000][20];
int used[10000][20];
int mas[11000];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);

	for (int cc=1; cc<=t; cc++){
		/*memset(a,0,sizeof(a));
		printf("Case #%d: ",cc);

		int n;
		scanf("%d",&n);

		for (int i=1; i<=n; i++){
			int x,b,c,d;
			scanf("%d%d%d%d",&x,&b,&c,&d);
			for (int j=b; j<=d; j++)
				for (int k=x; k<=c; k++)
					a[j][k]=1;
		}*/
		cin>>p;
		printf("Case #%d: ",cc);
		n=1<<p;
		for (int i=0; i<n; i++) cin>>m[i];
		for (int i=1; i<=p; i++)
			for (int j=1<<(p-i); j<(1<<(p-i+1)); j++)
				cin>>cost[j];

		memset(dp,-1,sizeof(dp));
		memset(used,0,sizeof(used));

		for (int i=2*n; i>=1; i--){
			for (int j=12; j>=0; j--){
				if (i>=n){
					m[i-n]<j?dp[i][j]=INF:dp[i][j]=0;
				} else
				{
					dp[i][j]=min(INF,dp[2*i][j]+dp[2*i+1][j]+cost[i]);
					dp[i][j]=min(dp[i][j],dp[2*i][j+1]+dp[2*i+1][j+1]);
				}
			}
		}

		cout<<dp[1][0]<<endl;
	}
    return 0;
}