// cj_qf_a.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdio.h"

int main()
{
	long int t,n,k;
	long int i,j,po;

	freopen("A-large.in","r",stdin); 
	freopen("out.txt","w",stdout); 

	scanf("%d",&t);
	for(i = 1 ; i <= t ; ++i)
	{
		scanf("%ld %ld",&n,&k);
		po = 1;
		for(j = 0 ; j != n; ++j)
		{
			po *= 2;
		}
		//po = pow(2,n);
		if((k+1) % po == 0)
			printf("Case #%d: ON\n",i);
		else
			printf("Case #%d: OFF\n",i);
	}
	fclose(stdin); 
	fclose(stdout);

	return 0;
}

