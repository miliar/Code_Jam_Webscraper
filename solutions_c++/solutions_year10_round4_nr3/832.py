#include <iostream>
#include <stdio.h>
using namespace std;
char map1[200][200];
char map2[200][200];
bool test(int t,int n)
{
	int i,j;
	if (t==1)
	{
		for (i=0;i<=n;i++)
		{
			for (j=0;j<=n;j++)
			{
				if (map1[i][j]!=0)
				{
					return false;
				}
			}
		}
		return true;
	}
	else
	{
		for (i=0;i<=n;i++)
		{
			for (j=0;j<=n;j++)
			{
				if (map2[i][j]!=0)
				{
					return false;
				}
			}
		}
		return true;
	}
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int t,r;
	scanf("%d",&t);
	int i,j;
	int x1,y1,x2,y2;
	int p,q;
	for (i=1;i<=t;i++)
	{
		memset(map1,0,sizeof(map1));
		memset(map2,0,sizeof(map2));
		scanf("%d",&r);
		for (j=1;j<=r;j++)
		{
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for (p=x1;p<=x2;p++)
			{
				for (q=y1;q<=y2;q++)
				{
					map1[p][q]=1;
				}
			}
		}
		int ans=0;
		int tmp=1;
		while (1)
		{
			if (test(tmp,100))
			{
				break;
			}
			if (tmp==1)
			{
				for (p=0;p<=100;p++)
				{
					for (q=0;q<=100;q++)
					{
						map2[p][q]=map1[p][q];
						if (map1[p][q]==1&&p>=1&&q>=1&&map1[p-1][q]==0&&map1[p][q-1]==0)
						{
							map2[p][q]=0;							
						}
						if (map1[p][q]==0&&p>=1&&q>=1&&map1[p-1][q]==1&&map1[p][q-1]==1)
						{
							map2[p][q]=1;							
						}
					}
				}
			}
			else if (tmp==0)
			{
				for (p=0;p<=100;p++)
				{
					for (q=0;q<=100;q++)
					{
						map1[p][q]=map2[p][q];
						if (map2[p][q]==1&&p>=1&&q>=1&&map2[p-1][q]==0&&map2[p][q-1]==0)
						{
							map1[p][q]=0;							
						}
						if (map2[p][q]==0&&p>=1&&q>=1&&map2[p-1][q]==1&&map2[p][q-1]==1)
						{
							map1[p][q]=1;							
						}
					}
				}				
			}
			tmp=(tmp+1)%2;
			ans++;
		}
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}