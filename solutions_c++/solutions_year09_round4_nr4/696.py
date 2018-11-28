#include <stdio.h>
#include <string.h>
#include <math.h>
int main()
{
	int c,n,i,j;
	int x[5];
	int y[5];
	int r[5];
	double d[5];
	double ans;
	freopen("out.txt","w",stdout);
	scanf("%d",&c);
	for(i=1;i<=c;i++)
	{
		scanf("%d",&n);
		for(j=0;j<n;j++)
		{
			scanf("%d%d%d",&x[j],&y[j],&r[j]);
		}
		if(n==1)
			ans = r[0];
		else if(n==2)
			ans = (r[0]>r[1]?r[0]:r[1]);
		else
		{
			d[0] = sqrt((double)((x[0] - x[1]) * (x[0] - x[1]) + (y[0] - y[1]) * (y[0] - y[1]))) + r[0]+r[1];
			d[1] = sqrt((double)((x[2] - x[1]) * (x[2] - x[1]) + (y[2] - y[1]) * (y[2] - y[1]))) + r[2]+r[1];
			d[2] = sqrt((double)((x[0] - x[2]) * (x[0] - x[2]) + (y[0] - y[2]) * (y[0] - y[2]))) + r[0]+r[2];
			ans = (d[0]<d[1]?d[0]:d[1]);
			ans = (ans<d[2]?ans:d[2]);
			ans /=2;
		}
		printf("Case #%d: %.6llf\n",i,ans);

		
	}
}