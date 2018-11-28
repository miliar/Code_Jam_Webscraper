#include<iostream>
using namespace std;

const int wlk[4][2]={{-1,0},{0,-1},{0,1},{1,0}};

int w,h,tot;
int hei[110][110];
int dp[110][110];
bool used[110][110];

int dfs(int x,int y)
{
	if (used[x][y]) return dp[x][y];
	used[x][y]=true;

	int nx,ny,tx,ty,min=10000000;
	bool found=false;
	for (int i=0;i<4;i++)
	{
		nx=x+wlk[i][0];
		ny=y+wlk[i][1];

		if (nx>=1 && nx<=h && ny>=1 && ny<=w && hei[nx][ny]<hei[x][y])
		{
			if (hei[nx][ny]<min)
			{
				min=hei[nx][ny];
				tx=nx;
				ty=ny;
			}
			found=true;
		}
	}
	if (!found) dp[x][y]=++tot;
	else dp[x][y]=dfs(tx,ty);

	return dp[x][y];
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("b.out","w",stdout);

	int tt,tc;
	int i,j;

	cin>>tc;
	for (tt=1;tt<=tc;tt++)
	{
		cin>>h>>w;
		for (i=1;i<=h;i++)
			for (j=1;j<=w;j++)
				cin>>hei[i][j];

		tot=0;
		memset(used,0,sizeof(used));

		for (i=1;i<=h;i++)
			for (j=1;j<=w;j++)
				dfs(i,j);

		char cnt='a';
		char cast[27];
		bool usedd[27];
		memset(usedd,0,sizeof(usedd));

		printf("Case #%d:\n",tt);
		for (i=1;i<=h;i++)
			for (j=1;j<=w;j++)
			{
				if (!usedd[dp[i][j]])
				{
					usedd[dp[i][j]]=true;
					cast[dp[i][j]]=cnt++;
				}
				
				cout<<cast[dp[i][j]];
				if (j==w) cout<<endl;
				else cout<<" ";
			}
	}
}
