#include <iostream.h>
#include <stdio.h>
//include<string>
//include<map>
#define debug 1

void sort(long long int* a, int n)
{
	int i=1,j=0;
	long long int temp;
	if(n == 1)
		return;
	for( i =1; i< n;i++)
	{
		for(j=0; j<i; j++)
		{
			if(a[j] > a[i])
			{
				temp = a[i];
				a[i] = a[j];
				a[j]=temp;
			}
		}
	}
 }



 long long int comb(long long int n)
 {
	if(n<3)
		return 0;
	if(debug)
		printf("\n in comb return comb of %lld as %lld",n,(n*(n-1)*(n-2))/6);
	return((n*(n-1)*(n-2))/6);
 }

void main()
{

	int i,j,test,N,press;
	long long int P,K,L,temp,count,pdt;
	long long int alp[1000];

	scanf("%d",&N);


	for (test=1; test<=N; test++)
	{
		scanf("%lld %lld %lld",&P,&K,&L);
		for(i=0;i<L;i++)
		{
		    scanf("%lld",&temp);
		    alp[i]=temp;

		}
		if (P*K < L)
		{
		      printf("Case #%d: Impossible",test);
		      continue;
		}
		sort(alp,L);
		count = pdt =0,press=1;
		for(j=L-1; j>=0; j--,count++)
		{
			if(count == K)
			{
				count = 0;
				press++;
			}
			if(press>P)
			 {
				printf("Error case %d",test);
			 }
			pdt += alp[j] * press;

		}

		printf("Case #%d: %lld\n",test,pdt);

	}
}