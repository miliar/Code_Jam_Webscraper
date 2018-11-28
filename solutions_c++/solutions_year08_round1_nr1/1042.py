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
	int CASE=0,n,T;
	int x[1000],y[1000],res;

	
	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);


//	freopen("A-large.in","r",stdin);
//	freopen("A-large.out","w",stdout);

	
	scanf("%d",&T);

	while(T--)
	{
		scanf("%d",&n);

		for(i=0; i<n; i++)
			scanf("%d",&x[i]);

		for(i=0; i<n; i++)
			scanf("%d",&y[i]);

		qsort(x,n,sizeof(int),comp);
		qsort(y,n,sizeof(int),comp);

		for(i=0,j=n-1,res=0; i<n; i++,j--)
			res += (x[i]*y[j]);
		

		CASE++;
		printf("Case #%d: ",CASE);

		printf("%d\n",res);

	}

}

