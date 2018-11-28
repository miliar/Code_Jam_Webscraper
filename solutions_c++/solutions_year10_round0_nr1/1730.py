#include<stdio.h>

#define MAX_N 30

long Step[ MAX_N+7];

void Calc( void)
{
	long i;
	Step[1] =1;
	for( i=2;i<=MAX_N;i++){
		Step[i] =2*Step[i-1]+1;
	}
}

int main( void)
{
	long i,Icase;
	long N,K;
	bool V;

	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);

	Calc();
	scanf("%ld",&Icase);
	for( i=1;i<=Icase;i++){

		scanf("%ld%ld",&N,&K);
		printf("Case #%ld: ",i);

		V =(K % (Step[N]+1)) != Step[N];

		if( V) printf("OFF\n");
		else printf("ON\n");
	}

	return 0;
}