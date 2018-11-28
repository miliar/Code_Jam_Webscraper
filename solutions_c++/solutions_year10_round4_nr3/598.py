#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int maxx(int a,int b)
{
	return a<b?a:b;
}

int num[301][301];

int main()
{
	int case_t;
	freopen("test.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&case_t);
	int pp=1;
	while(case_t--)
	{
		int r;
		scanf("%d",&r);
		int i,j,k;
		memset(num,0,sizeof(num));
		int h_t=0,s_t=0;
		for(i=0;i<r;++i)
		{
			int x1,x2,y1,y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for(k=x1;k<=x2;++k)
				for(j=y1;j<=y2;++j)
					num[k][j]=1;
		}
		int ans=0;
		int pre[301][301];
		while(1)
		{
			ans++;
			memset(pre,0,sizeof(pre));
			for(i=1;i<=300;++i)
				for(j=1;j<=300;++j)
				{
					if(num[i][j])
					{
						if(num[i-1][j]==0&&num[i][j-1]==0)
							pre[i][j]=0;
						else pre[i][j]=1;
					}
					else
					{
						if(num[i-1][j]==1&&num[i][j-1]==1)
							pre[i][j]=1;
						else pre[i][j]=0;
					}
				}
			int up=0;
			for(i=1;i<=300;++i)
				for(j=1;j<=300;++j)
				{
					num[i][j]=pre[i][j];
					if(pre[i][j])
						up=1;
				}
			if(!up)
				break;
		}
		printf("Case #%d: %d\n",pp++,ans);
	}
}