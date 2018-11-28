#include<stdio.h>
#include<stdlib.h>

int comp1(const void *a, const void *b)
{
	if( *(double*)a > *(double*)b) return 1;
	else if ( *(double*)a == *(double*)b) return 0;
	return -1;
}

int comp2(const void *a, const void *b)
{
	if( *(double*)b > *(double*)a) return 1;
	else if ( *(double*)a == *(double*)b) return 0;
	return -1;
}

int main()
{
	int test;
	int k,i,l;
	double x[1005],y[1005],hasil;
	scanf("%d",&test);
	for(k=1;k<=test;k++)
	{
		scanf("%d",&l);
		
		for(i=0;i<l;i++)
		{
			scanf("%lf",&x[i]);
		}
		qsort(x,l,sizeof(double),comp1);
		
		for(i=0;i<l;i++)
		{
			scanf("%lf",&y[i]);
		}
		qsort(y,l,sizeof(double),comp2);
		hasil = 0;
		for(i=0;i<l;i++)
		{
			hasil += x[i] * y[i];
		}
		printf("Case #%d: %.0lf\n",k,hasil);
	}
	while(getchar()!=EOF);
	return 0;
}
