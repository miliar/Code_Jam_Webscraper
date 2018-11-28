#include <iostream>
#include <stdio.h>
using namespace std;
int is[200][200];
int main()
{
	int i;
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	memset(is,0,sizeof(is));
	int t;
	int r;
	int j,k,l;
	int x1,x2,y1,y2;
	scanf("%d",&t);
	int ans =0;
	for (i = 1;i <= t;i++)
	{
		scanf("%d",&r);
		for (j = 1;j <=r;j++)
		{
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for (k = x1;k<=x2;k++)
				for (l = y1;l <= y2;l++)
				{
					is[k][l] = 1;
				}
		}
		ans = 0;
		while(1)
		{
			ans ++;
			int flag = 0;
			for (j = 100;j >= 1;j--)
			{
				for (k = 100;k >= 1;k--)
				{
					if (is[j][k] && !is[j-1][k]&&!is[j][k-1])
						is[j][k] = 0;
					if (!is[j][k] && is[j-1][k]&&is[j][k-1])
						is[j][k] = 1;
					flag += is[j][k];
				}
			}
			if (flag ==0)
				break;			
		}
		printf("Case #%d: %d\n",i,ans);
	}
}