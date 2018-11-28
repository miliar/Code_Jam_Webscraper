#include<stdio.h>
int main()
{
	freopen("11.in","r",stdin);
	freopen("out.txt","w",stdout);
	int thecase=1;
	int case_num;
	scanf("%d",&case_num);
	for (thecase=1;thecase<=case_num;thecase++)
	{
		int r,k,n;
		int g[20];
		scanf("%d%d%d",&r,&k,&n);
		int temp;
		for(temp=0;temp<n;++temp)
			scanf("%d",&g[temp]);
		int point=0;
		int he=0;
		for(temp=1;temp<=r;++temp)
		{
			int x=0;
			int temppoint=point;
			while(x+g[point]<=k)
			{
				he+=g[point];
				x+=g[point];
				point++;
				point=point%n;
				if(point==temppoint) break;
			}

		}
		printf("Case #%d: %d\n",thecase,he);

	}
}