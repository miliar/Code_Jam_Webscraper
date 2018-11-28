#include <stdio.h>
#include <math.h>
int D,I,M,n;

int insertto(int a, int b)
{
	if (a==b) return 0;
	if (M==0) return 255000;
	return (abs(a-b)-1)/M*I;
}

int min2(int a, int b)
{	
	int min,i,cost;
	min=D;
	for (i=0; i<=255; i++)
	{
		cost=abs(i-a)+insertto(i,b);
		if (cost<min) min=cost;
	}
	return min;
}

int main()
{
	int t,cas,i,j,k,a[120],min,cost;
	freopen("B-small-attempt2.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&t);
	for (cas=1; cas<=t; cas++)
	{
		scanf("%d%d%d%d",&D,&I,&M,&n);
		for (i=0; i<n; i++) scanf("%d",&a[i]);
		if (n<=1) min=0;
		else if (n==2)
		{
			min=min2(a[0],a[1]);
		} else {
			min=min2(a[0],a[1])+D;
			cost=min2(a[0],a[2])+D;
			if (cost<min) min=cost;
			cost=min2(a[1],a[2])+D;
			if (cost<min) min=cost;
			for (i=0; i<=255; i++)
			{
				for (j=0; j<=255; j++)
				{
					for (k=0; k<=255; k++)
					{
						cost=abs(i-a[0])+abs(j-a[1])+abs(k-a[2])+insertto(i,j)+insertto(j,k);
						if (cost<min) min=cost;
					}
				}
			}
		}
		printf("Case #%d: %d\n",cas,min);
	}
	return 0;
}
			
				
			
