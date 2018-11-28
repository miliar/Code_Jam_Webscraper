#include<stdio.h>

struct node
{
	int x,y;
};
node num[1001];

int main(void)
{
	int t;
	int yy=0;
	freopen("A-large (1).in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		int n;
		yy++;
		scanf("%d",&n);
		int ans=0;
		for(int i=0;i<n;i++)
		{
			scanf("%d%d",&num[i].x,&num[i].y);
			for(int j=0;j<i;j++)
			{
				if((num[j].x<num[i].x)^(num[j].y<num[i].y))
				{
					ans++;
				}
			}
		}
		printf("Case #%d: %d\n",yy,ans);
	}
	return 0;
}