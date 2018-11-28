#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
char map[55][55];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("Aout.out","w",stdout);
	int t,cas;
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++)
	{
		memset(map,0,sizeof(map));
		int n,m;
		scanf("%d%d",&n,&m);
		int i,j,num=0;
		for(i=0;i<n;i++)
		{
			scanf("%s",map[i]);
			for(j=0;j<m;j++)
				if(map[i][j]=='#')
					num++;
		}
		printf("Case #%d:\n",cas);
		if(num==0)
		{
			for(i=0;i<n;i++)
				printf("%s\n",map[i]);
			continue;
		}
		if(num%4!=0)
		{
			printf("Impossible\n");
			continue;
		}
		int flag=1;
		for(i=0;flag&&i<n;i++)
			for(j=0;flag&&j<m;j++)
				if(map[i][j]=='#')
				{
					map[i][j]='/';
					if(map[i+1][j]=='#')
						map[i+1][j]='\\';
					else flag=0;
					if(map[i][j+1]=='#')
						map[i][j+1]='\\';
					else flag=0;
					if(map[i+1][j+1]=='#')
						map[i+1][j+1]='/';
					else flag=0;
				}
		if(!flag)
			printf("Impossible\n");
		else
		{
			for(i=0;i<n;i++)
				printf("%s\n",map[i]);
		}
	}
	return 0;
}
