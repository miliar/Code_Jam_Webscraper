#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <math.h>
#include <algorithm>
using namespace std;

int comp(const void *a, const void *b)
{
	int *i = (int *)a;
	int *j = (int *)b;

	if(*i < *j)
		return -1;
	else if(*i > *j)
		return 1;
	else
		return 0;
}


main()
{
	int i,j;
	int CASE=0,n;

	
//	freopen("B-small.in","r",stdin);
//	freopen("B-small.out","w",stdout);


//	freopen("B-large.in","r",stdin);
//	freopen("B-large.out","w",stdout);

	int na,nb,T,resa,resb;
	int reqa[105],reqb[105],availa[105],availb[105];
	int hh,mm;
	
	scanf("%d",&n);

	while(n--)
	{
		scanf("%d",&T);
		scanf("%d %d",&na,&nb);

		for(i=0; i<na; i++)
		{
			scanf("%d:%d",&hh,&mm);
			reqa[i] = (hh*60) + mm; 

			scanf("%d:%d",&hh,&mm);
			availb[i] = (hh*60) + mm + T; 
		}

		for(i=0; i<nb; i++)
		{
			scanf("%d:%d",&hh,&mm);
			reqb[i] = (hh*60) + mm; 

			scanf("%d:%d",&hh,&mm);
			availa[i] = (hh*60) + mm + T; 
		}

		qsort(reqa, na, sizeof(int) , comp);
		qsort(reqb, nb, sizeof(int), comp);
		qsort(availa, nb, sizeof(int), comp);
		qsort(availb, na, sizeof(int), comp);


		resa=resb=0;
		for(i=j=0; i<na; i++)
		{
			if(j < nb)
			{
				if(reqa[i] < availa[j])
					resa++;
				else
					j++;
			}
			else
				resa++;
		}

		for(i=j=0; i<nb; i++)
		{
			if(j < na)
			{
				if(reqb[i] < availb[j])
					resb++;
				else
					j++;
			}
			else
				resb++;
		}


		CASE++;
		printf("Case #%d: ",CASE);

		printf("%d %d\n",resa,resb);

	}

}

