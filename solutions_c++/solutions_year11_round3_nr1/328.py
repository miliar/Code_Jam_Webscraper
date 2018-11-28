#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

char a[100][100],ans[100][100];
int flag[100][100];

int main()
{
	int cas=1;
	freopen("A-large.in","r",stdin);
	freopen("outAL.txt","w",stdout);
	int T;scanf("%d",&T);
	while(T--)
	{
		memset(flag,0,sizeof(flag));
		int i,j;
		int r,c;scanf("%d%d",&r,&c);
		memset(ans,0,sizeof(ans));
		for(i=0;i<r;++i)
		{
			scanf("%s",a[i]);
			for(j=0;j<c;++j)
				ans[i][j]=a[i][j];
		}
		for(i=0;i<r-1;++i)
		{
			for(j=0;j<c-1;++j)
			{
				if(ans[i][j]=='#'&&ans[i+1][j]=='#'&&ans[i+1][j+1]=='#'&&ans[i][j+1]=='#')
				{
					ans[i][j]=ans[i+1][j+1]='/';
					ans[i][j+1]=ans[i+1][j]=92;
				}
			}
		}
		printf("Case #%d:\n",cas++);
		int f=0;
		for(i=0;i<r;++i)
			for(j=0;j<c;++j)
				if(ans[i][j]=='#')
					f=1;
		if(!f)
		{
			for(i=0;i<r;++i)
				printf("%s\n",ans[i]);
		}
		else
		{
			printf("Impossible\n");
		}
	}
}