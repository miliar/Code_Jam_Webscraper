#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
#define MAXN 51

char mp[51][51];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int T,R,C;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		scanf("%d%d",&R,&C);
		for(int i=0;i<R;i++)
			scanf("%s",mp[i]);
		int f=1;
		for(int i=0;i<R&&f;i++)
			for(int j=0;j<C&&f;j++)
			{
				if(mp[i][j]=='#')
				{
					if(i<R&&mp[i+1][j]=='#'&&j<C&&mp[i][j+1]=='#'&&mp[i+1][j+1]=='#')
					{
						mp[i][j]=mp[i+1][j+1]='/';
						mp[i][j+1]=mp[i+1][j]='\\';
					}
					else f=0;
				}
			}
		printf("Case #%d:\n",t);
		if(f)
		{
			for(int i=0;i<R;i++)
				printf("%s\n",mp[i]);
		}
		else printf("Impossible\n");
		
	}
	return 0;
}
