#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstdlib>
using namespace std;

#define debug(x) cout << #x << "=" << x << endl

typedef long long ll;

int T,n,m,x,ans;
string s[555];
int w[555][555];
ll sx[555][555],sy[555][555];
ll sw[555][555];

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	cin >> T;
	for (int test=1;test<=T;test++)
	{
		cin >> n >> m >> x;
		for (int i=0;i<n;i++) cin >> s[i];
		for (int i=1;i<=n;i++) for (int j=1;j<=m;j++)
			w[i][j] = s[i-1][j-1] - '0';
		/*
		printf("w:\n");
		for (int i=1;i<=n;i++)
		{
			for (int j=1;j<=m;j++)
				printf("%d ",w[i][j]);
			printf("\n");
		}
		*/
		memset(sw,0,sizeof sw);
		memset(sx,0,sizeof sx);
		memset(sy,0,sizeof sy);
		for (int i=1;i<=n;i++)
			for (int j=1;j<=m;j++)
				sw[i][j] = sw[i-1][j] + sw[i][j-1] - sw[i-1][j-1] + w[i][j];
		/*
		printf("sw:\n");
		for (int i=1;i<=n;i++)
		{
			for (int j=1;j<=m;j++)
				printf("%d ",sw[i][j]);
			printf("\n");
		}*/
		
		for (int i=1;i<=n;i++)
			for (int j=1;j<=m;j++)
			{
				sx[i][j] = sx[i-1][j] + sx[i][j-1] - sx[i-1][j-1] + w[i][j] * i;
				sy[i][j] = sy[i-1][j] + sy[i][j-1] - sy[i-1][j-1] + w[i][j] * j;
			}
		
		ans = 0;
		for (int k=min(n,m);k>=3;k--)
		{
			for (int i=k;i<=n;i++)
			{
				for (int j=k;j<=m;j++)
				{
					ll sumx,sumy,sumw;
					sumw = sw[i][j] - sw[i-k][j] - sw[i][j-k] + sw[i-k][j-k] - w[i][j] - w[i-k+1][j] - w[i][j-k+1] - w[i-k+1][j-k+1];
					sumx = sx[i][j] - sx[i-k][j] - sx[i][j-k] + sx[i-k][j-k] - w[i][j]*i - w[i-k+1][j]*(i-k+1) - w[i][j-k+1]*i - w[i-k+1][j-k+1]*(i-k+1);
					sumy = sy[i][j] - sy[i-k][j] - sy[i][j-k] + sy[i-k][j-k] - w[i][j]*j - w[i-k+1][j]*j - w[i][j-k+1]*(j-k+1) - w[i-k+1][j-k+1]*(j-k+1);
					//printf("i=%d j=%d\n",i,j);
					//debug(sumw);
					//debug(sumx);
					//debug(sumy);
					if (sumx * 2 == (i-k+1+i) * sumw && sumy * 2 == (j-k+1+j) * sumw)
					{
						ans = k;
						break;
					}
				}
				if (ans) break;
			}
			if (ans) break;
		}
		if (ans==0) printf("Case #%d: IMPOSSIBLE\n",test);
		else printf("Case #%d: %d\n",test,ans);
	}
	return 0;
}
