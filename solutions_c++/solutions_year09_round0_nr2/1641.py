#include <stdio.h>
#include <string.h>
#include <queue>
#include <algorithm>
using namespace std;
#define INF 987654321

struct node
{
	int x,y,h;
	node(){}
	node(int xx,int yy,int hh)
	{
		x = xx;y = yy;h = hh;
	}
};
bool operator<(node a,node b)
{
	return a.h<b.h;
}
priority_queue<node> que;

int cn=1,cs,n,m,lb;
int mp[105][105];
int out[105][105],out2[105][105];
int move[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};

int dfs(int x,int y,int h)
{
	int i,j,xx,yy;
	int minh = h,sel=-1;
	if(out[x][y] == -1) out[x][y] = lb;
	else return out[x][y];
	for(i=0;i<4;i++)
	{
		xx = x+move[i][0];
		yy = y+move[i][1];
		if(xx>=0 && xx<n && yy>=0 && yy<m)
		{
			if(minh > mp[xx][yy])
			{
				minh = mp[xx][yy];
				sel = i;
			}
		}
	}
	if(sel == -1) return -1;
	xx = x+move[sel][0];
	yy = y+move[sel][1];
	int ret = dfs(xx,yy,mp[xx][yy]);
	if(ret != -1)
		out[x][y] = ret;
	return ret;
}

void dfs2(int x,int y,int col)
{
	int i,j,xx,yy;
	out2[x][y] = lb;
	for(i=0;i<4;i++)
	{
		xx = x+move[i][0];
		yy = y+move[i][1];
		if(xx>=0 && xx<n && yy>=0 && yy<m)
		{
			if(out[xx][yy]==col && out2[xx][yy]==-1)
			{
				dfs2(xx,yy,col);
			}
		}
	}
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-out.txt","w",stdout);
	int i,j;
	scanf("%d",&cs);
	while(cs--)
	{
		while(!que.empty()) que.pop();
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				scanf("%d",&mp[i][j]);
				que.push(node(i,j,mp[i][j]));
			}
		}
		memset(out,-1,sizeof(out));
		lb = 0;
		while(!que.empty())
		{
			node tmp = que.top();que.pop();
			if(out[tmp.x][tmp.y] != -1) continue;
			int ret = dfs(tmp.x,tmp.y,tmp.h);
			if(ret == -1) lb++;
			/*for(i=0;i<n;i++)
			{
				for(j=0;j<m;j++)
				{
					printf("%d",out[i][j]);
					if(j==m-1) printf("\n");
					else printf(" ");
				}
			}*/
		}
		lb = 0;
		memset(out2,-1,sizeof(out2));
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				if(out2[i][j] == -1)
				{
					dfs2(i,j,out[i][j]);
					lb++;
				}
			}
		}
		printf("Case #%d:\n",cn++);
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				printf("%c",out2[i][j]+'a');
				if(j==m-1) printf("\n");
				else printf(" ");
			}
		}
	}
	return 0;
}

