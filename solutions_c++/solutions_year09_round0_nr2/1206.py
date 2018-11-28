#include<iostream>
#include<string>
using namespace std;
int Map[110][110];
int res[110][110];
int n,m;
int sta=0;
int cnt;
int ax[]={-1,0,0,1};
int bx[]={0,-1,1,0};
void dfs(int x,int y)
{
	int Min=10010;
	int idx=-1,idy=-1;
	for(int i=0;i<4;++i)
	{
		int tx=x+ax[i];
		int ty=y+bx[i];
		if(tx<0||ty<0||tx>=n||ty>=m)
			continue;
		if(Map[tx][ty]<Map[x][y]&&Map[tx][ty]<Min)
		{
			Min=Map[tx][ty];
			idx=tx,idy=ty;
		}
	}
	if(idx!=-1&&idy!=-1)
	{
		if(res[idx][idy]!=-1)
		{
			sta=res[idx][idy];
			return ;
		}
		else
		{
			dfs(idx,idy);
			res[idx][idy]=sta;
		}
	}
	else
	{
		res[x][y]=cnt;
		sta=cnt++;
	}
	return ;
}
int main()
{
    freopen("G:\\B-large.in","r",stdin);
	freopen("G:\\B-large.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int cas=1;cas<=t;++cas)
	{
		cnt=0;
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;++i)
			for(int j=0;j<m;++j)
				scanf("%d",&Map[i][j]);
		memset(res,-1,sizeof(res));
		for(int i=0;i<n;++i)
			for(int j=0;j<m;++j)
			{
				if(res[i][j]==-1)
				{
					dfs(i,j);
					res[i][j]=sta;
				}
			}
		printf("Case #%d:\n",cas);
		for(int i=0;i<n;++i)
		{
			for(int j=0;j<m-1;++j)
				printf("%c ",(char)(res[i][j]+'a'));
			printf("%c\n",(char)(res[i][m-1]+'a'));
		}
	}
	return 0;
}