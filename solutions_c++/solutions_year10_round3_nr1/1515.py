#include<stdio.h>
#include<stdlib.h>

#define MAX_W 1007

struct CONT{
	long Ind;
	long A,B;
} Wind[ MAX_W+7];


int Comp( const void *a,const void *b)
{
	CONT *p1 =(CONT*)a;
	CONT *p2 =(CONT*)b;

	return p2->A - p1->A;
}


int Comp2( const void *a,const void *b)
{
	CONT *p1 =(CONT*)a;
	CONT *p2 =(CONT*)b;

	return p2->B - p1->B;
}

inline long MIN( long a,long b)
{
	return a<b ? a:b;
}

int main( void)
{
	long k,Icase;
	long i,N;

	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);

	scanf("%ld",&Icase);
	for( k=1;k<=Icase;k++){
		scanf("%ld",&N);
		for( i=1;i<=N;i++){
			scanf("%ld%ld",&Wind[i].A,&Wind[i].B);
		}

		qsort( &Wind[1],N,sizeof(CONT),Comp);
		for( i=1;i<=N;i++){
			Wind[i].Ind =i;
		}
		qsort( &Wind[1],N,sizeof(CONT),Comp2);

		long Ans =0;
		for(i=1;i<=N;i++){
			long Low =N-i;
			long Up =Wind[i].Ind-1;
			Ans +=MIN( Low,Up);
		}

		printf("Case #%ld: %ld\n",k,Ans);
	}

	return 0;
}


