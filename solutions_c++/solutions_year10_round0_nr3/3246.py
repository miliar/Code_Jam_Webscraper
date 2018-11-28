#include <stdio.h>

void main()
{
	int t,r,k,n,i,j,start,groups_taken,empty_places,cach;
	int g[1000];

	freopen("C-small-attempt0.in","r",stdin);
	freopen("A.out","w",stdout);

	scanf("%d",&t);

	for(i = 1; i<=t;i++)
	{
		scanf("%d %d %d",&r,&k,&n);
		for(j = 0;j<n;j++) 
			scanf("%d",&g[j]);
		cach = k*r;
		start = 0;
		groups_taken = 0;
		for(j = 0; j<r;j++)
		{
			empty_places = k;
			for(;groups_taken<n&&empty_places>=g[start];groups_taken++,start = (start<n-1 ? ++start : 0))
			{
				empty_places -=g[start];
			}
			cach -=empty_places;
			groups_taken = 0;
		}
		printf("Case #%d: %d\n",i,cach);
	}

}