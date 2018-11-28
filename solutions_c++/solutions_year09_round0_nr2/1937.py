#include <iostream>

using namespace std;

int t;
int h,w;
int a[200][200];
int d[200][200];
int used[200][200];
int con;

void dfs(int x,int y)
{
	if (used[x][y]!=0) return;
	used[x][y]=con;

	if (d[x][y]==1) dfs(x-1,y);
	if (d[x][y]==2) dfs(x,y-1);
	if (d[x][y]==3) dfs(x,y+1);
	if (d[x][y]==4) dfs(x+1,y);

	if (d[x-1][y]==4) dfs(x-1,y);
	if (d[x+1][y]==1) dfs(x+1,y);
	if (d[x][y-1]==3) dfs(x,y-1);
	if (d[x][y+1]==2) dfs(x,y+1);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d",&t);

	int tt;

	for (tt=1; tt<=t; tt++)
	{
		scanf("%d%d",&h,&w);
		memset(used,0,sizeof(used));
		int i,j,k;

		for (i=0; i<200; i++)
			for (j=0; j<200; j++)
				a[i][j]=11000;

		for (i=1; i<=h; i++)
			for (j=1; j<=w; j++)
			scanf("%d",&a[i][j]);

		for (i=1; i<=h; i++)
			for (j=1; j<=w; j++)
			{
				if (a[i+1][j]>=a[i][j]&&a[i-1][j]>=a[i][j]&&a[i][j+1]>=a[i][j]&&a[i][j-1]>=a[i][j]) d[i][j]=0; else
				if (a[i-1][j]<a[i][j]&&a[i+1][j]>=a[i-1][j]&&a[i][j+1]>=a[i-1][j]&&a[i][j-1]>=a[i-1][j]) d[i][j]=1; else
				if (a[i][j-1]<a[i][j]&&a[i+1][j]>=a[i][j-1]&&a[i][j+1]>=a[i][j-1]&&a[i-1][j]>=a[i][j-1]) d[i][j]=2; else
				if (a[i][j+1]<a[i][j]&&a[i+1][j]>=a[i][j+1]&&a[i-1][j]>=a[i][j+1]&&a[i][j-1]>=a[i][j+1]) d[i][j]=3; else
					d[i][j]=4;
			}
		
		con=0;

		for (i=1; i<=h; i++)
			for (j=1; j<=w; j++)
				if (used[i][j]==0)
				{
					con++;
					dfs(i,j);
				}

		printf("Case #%d:\n",tt);

		for (i=1; i<=h; i++)
		{
			for (j=1; j<=w; j++)
				printf("%c ",used[i][j]+'a'-1);
			printf("\n");
		}
	}

	return 0;
}