#include<stdio.h>
int main()
{
	int n,i;
	int a,b;
	int j,k,max;
	int count;

	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d %d",&a,&b);

		count=0;
		for(j=a;j<=b;j++)
		{
			for(max=1;max<b;max*=10);
			for(k=10;k<max;k*=10)
			{
				if(b>=j%(k)*max/k+j/k && j%(k)*max/k+j/k>j)
				{
					count++;
//					printf("(%d,%d)\n",j,j%(k)*max/k+j/k);
				}
			}
		}
		printf("Case #%d: %d\n",i+1,count);
	}
	

	return 0;
}