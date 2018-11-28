#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
char k[8]={'Q','W','E','R','A','S','D','F'};
char comb[40][4],cler[30][4],s[105];
int op[300][300],vis[300];
int com[300][300];
int ans[300];
int main()
{
	int t,cas;
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++)
	{
		memset(com,0,sizeof(com));
		memset(s,0,sizeof(s));
		memset(comb,0,sizeof(comb));
		memset(cler,0,sizeof(cler));
		memset(op,0,sizeof(op));
		memset(vis,0,sizeof(vis));
		int n,m;
		scanf("%d",&n);
		int i,len;
		for(i=0;i<n;i++)
		{
			scanf("%s",comb[i]);
			com[comb[i][0]][comb[i][1]]=comb[i][2];
			com[comb[i][1]][comb[i][0]]=comb[i][2];
		}
		scanf("%d",&m);
		for(i=0;i<m;i++)
		{
			scanf("%s",cler[i]);
			op[cler[i][0]][cler[i][1]]=1;
			op[cler[i][1]][cler[i][0]]=1;
		}
		scanf("%d",&len);
		scanf("%s",s);
		memset(vis,0,sizeof(vis));
		int p=1,j;
		ans[0]=s[0];
		vis[s[0]]++;
		for(i=1;i<len;i++)
		{
			int flag=0;
			if(com[s[i]][ans[p-1]]>0)
			{
				vis[ans[p-1]]--;
				ans[p-1]=com[s[i]][ans[p-1]];
				continue;
			}
			else
			{
				for(j=0;j<8;j++)
				{
					if(op[s[i]][k[j]]==1&&vis[k[j]]>0)
					{
						flag=1;
						p=0;
						memset(vis,0,sizeof(vis));
					}
				}
			}
			if(flag==0)
			{
				ans[p++]=s[i];
				vis[s[i]]++;
			}
		}
		printf("Case #%d: [",cas);
		for(i=0;i<p;i++)
		{
			if(i==0)
				printf("%c",ans[i]);
			else
				printf(", %c",ans[i]);
		}
		printf("]\n");
	}
	return 0;
}
