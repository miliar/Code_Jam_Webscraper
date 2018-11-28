#include <stdio.h>
#include <string.h>
const int Maxn=100;
const int step[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
int n,m;
int map[Maxn][Maxn],ans[Maxn][Maxn];
int hash[27];
int col;
int color(int x,int y)
{
	if (ans[x][y]>0) return ans[x][y];
	int lowest=-1;
	for (int i=0;i<4;i++)
	{
		int nextx=x+step[i][0],nexty=y+step[i][1];
		if (nextx>=0 && nextx<n && nexty>=0 && nexty<m)
		{
			if (lowest==-1) 
				lowest=i;
			else if (map[nextx][nexty]<map[x+step[lowest][0]][y+step[lowest][1]])
				lowest=i;
		}
	}
	if (lowest>=0 && map[x+step[lowest][0]][y+step[lowest][1]]<map[x][y])
		ans[x][y]=color(x+step[lowest][0],y+step[lowest][1]);
	else ans[x][y]=++col;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int cases;
	scanf("%d",&cases);
	for (int k=1;k<=cases;k++)
	{
		printf("Case #%d:\n",k);
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++)
				scanf("%d",&map[i][j]);
		memset(ans,0,sizeof(ans));
		col=0;
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++)
				if (!ans[i][j]) color(i,j);

		col=0;
		memset(hash,-1,sizeof(hash));
		for (int i=0;i<n;i++)
		{
			for (int j=0;j<m;j++)
			{
				if (hash[ans[i][j]]<0) hash[ans[i][j]]=col++;
				printf("%c ",hash[ans[i][j]]+'a');
			}
			printf("\n");
		}
	}

	return 0;
}