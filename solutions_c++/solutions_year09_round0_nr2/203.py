#include<stdio.h>
#include<string.h>
struct data{
	int x,y;
}dir[4]={{-1,0},{0,-1},{0,1},{1,0}};
#define MAX 101
int mp[MAX][MAX],to[MAX][MAX],ans[MAX][MAX],n,m;
bool ok(int x,int y)
{
	if(x>=0&&x<n&&y>=0&&y<m)
		return true;
	return false;
}
int main()
{
	int cas,d,i,j,k,bestx,besty,nowx,nowy,cnt;
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&cas);
	for(d=0;d<cas;d++)
	{
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				scanf("%d",&mp[i][j]);
		memset(to,-1,sizeof(to));
		for(cnt=i=0;i<n;i++)
			for(j=0;j<m;j++)
			{
				nowx=i;
				nowy=j;
				while(true)
				{
					bestx=nowx;
					besty=nowy;
					for(k=0;k<4;k++)
						if(ok(nowx+dir[k].x,nowy+dir[k].y)&&mp[bestx][besty]>mp[nowx+dir[k].x][nowy+dir[k].y])
						{
							bestx=nowx+dir[k].x;
							besty=nowy+dir[k].y;
						}
					if(bestx==nowx&&besty==nowy)
					{
						if(to[bestx][besty]==-1)
							to[bestx][besty]=cnt++;
						ans[i][j]=to[bestx][besty];
						break;
					}
					else
					{
						nowx=bestx;
						nowy=besty;
					}
				}
			}
		printf("Case #%d:\n",d+1);
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				printf("%c%c",ans[i][j]+'a',j==m-1?'\n':' ');
	}
	return 0;
}