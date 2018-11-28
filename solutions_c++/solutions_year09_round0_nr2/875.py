#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#define inf 1013741823
using namespace std;
int n,m;
const int d[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
int a[110][110];
char q,ans[110][110];
int h(int x,int y)
{
	return x<0||x>=n||y<0||y>=m?inf:a[x][y];
}
char dfs(int x,int y)
{
	if(ans[x][y]!=0)return ans[x][y];
	int low=a[x][y];
	for(int i=0; i<4; i++)
		low=min(low,h(x+d[i][0],y+d[i][1]));
	if(low==a[x][y])
		return ans[x][y]=q++;
	for(int i=0; i<4; i++)
		if(h(x+d[i][0],y+d[i][1])==low)
			return ans[x][y]=dfs(x+d[i][0],y+d[i][1]);
}
int main()
{
	int _;
	scanf("%d",&_);
	for(int t=1; t<=_; t++)
	{
		scanf("%d%d",&n,&m);
		for(int i=0; i<n; i++)
			for(int j=0; j<m; j++)
				scanf("%d",&a[i][j]);
		memset(ans,0,sizeof(ans));
		q='a';
		for(int i=0; i<n; i++)
			for(int j=0; j<m; j++)
				dfs(i,j);
		printf("Case #%d:\n",t);
		for(int i=0; i<n; i++)
			for(int j=0; j<m; j++)
			{
				printf("%c",ans[i][j]);
				if(j==m-1)
					puts("");
				else
					printf(" ");
			}
	}
	return 0;
}
