
#include<stdio.h>
int main()
{
	freopen("6.txt","w",stdout);
	int t;
	scanf("%d",&t);
	{
		int jj=1;
		while(t--)
		{
			int n;
			int i;
			scanf("%d",&n);
			double count=0;
			for(i=1;i<=n;i++)
			{
				int b;
				scanf("%d",&b);
				if(i!=b)
					count++;
			}
			printf("Case #%d: ",jj++);
			printf("%.6lf\n",count );
		}
	}
	return 0;
}