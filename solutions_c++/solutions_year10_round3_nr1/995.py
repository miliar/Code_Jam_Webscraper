#include "stdafx.h"
#include "stdio.h"

int main()
{
	int i,j,k,t,n=0,sum;
	int a[1000] = {0},b[1000] = {0};

	freopen("A-large.in","r",stdin); 
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for(i = 1 ; i <= t ; ++i)
	{
		sum = 0;
		for(j = 0 ; j < n ; ++j)
		{
			a[j] = 0;
			b[j] = 0;
		}
		scanf("%d" , &n);

		for(j = 0 ; j != n ; ++j)
		{
			scanf("%d %d" , &a[j] , &b[j]);
		}
		for(j = 0 ; j != n ; ++j)
		{
			for(k = j+1 ; k < n ; ++k)
			{
				if((a[j] > a[k] && b[j] < b[k]) || (a[j] < a[k] && b[j] > b[k]))
				{
					++sum;
				}
			}
		}
		printf("Case #%d: %d\n",i,sum);
	}
	fclose(stdin); 
     fclose(stdout);
	return 0;
}

