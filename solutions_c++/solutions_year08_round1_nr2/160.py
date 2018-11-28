#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <queue>
#define MAX 2009
using namespace std;

struct node{int x,y;}tmp;
vector<node>st[MAX];
int C,n,m,i,j,k,t,ok,done,cas,rep,imp;
int ans[MAX];

int main()
{
	scanf("%d",&C);
	cas = 0;
	while (C--)
	{
		memset(ans,-1,sizeof(ans));
		scanf("%d%d",&n,&m);
		for (i=0; i<m; i++ )
		{
			st[i].clear();
			scanf("%d",&t);
			for (j=0;j<t ;j++ )
			{
				scanf("%d%d",&tmp.x,&tmp.y);
				st[i].push_back(tmp);
			}
		}
		memset(ans,0,sizeof(ans));
		done = 0;
		imp = 0;
		while (!done)
		{
			rep++;
			done = 1;
			for (i=0;i<m ;i++ )
			{
				ok = 0;
				for (j=0;j<st[i].size() ;j++ )
				{
					if (ans[st[i][j].x]==st[i][j].y)
					{
						ok = 1;
					}
				}
				if (!ok)
				{
					for (j=0;j<st[i].size() ;j++ )
					{
						if (st[i][j].y==1)
						{
							ans[st[i][j].x]=1;
							ok = 1;
							break;
						}
					}
					done = 0;
				}
				if (!ok)
				{
					imp=1;break;
				}
			}
			if (imp)
			{
				break;
			}
		}
		for (i=0;i<m ;i++ )
		{
			ok = 0;
			for (j=0;j<st[i].size() ;j++ )
			{
				if (ans[st[i][j].x]==st[i][j].y)
				{
					ok = 1;
				}
			}
			if (!ok)
			{
				imp = 1;
				break;
			}
		}
		printf("Case #%d:",++cas);
		if (imp)
		{
			printf(" IMPOSSIBLE\n");
		}
		else
		{
			for (i=1;i<=n ;i++ )
			{
				printf(" %d",ans[i]);
			}
			printf("\n");
		}
	}
	return 0;
}
