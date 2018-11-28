#include <stdio.h>
#include <stdlib.h>

int numa[805];
int numb[805];

int cmp1 ( const void *a, const void *b)
{
	return *(int*)a-*(int*)b;
}
int cmp2( const void *a, const void *b)
{
	return *(int*)b-*(int*)a;
}

int main ()
{
	int n;
	int T;
	int i;
	freopen("ga.in","r",stdin);
	freopen("ga.out","w",stdout);
	scanf("%d", &T);
	for ( int t=1; t<=T; t++ )
	{
		scanf("%d",&n);
		for ( i=0; i<n; i++ )
			scanf("%d", &numa[i]);
		for ( i=0; i<n; i++ )
			scanf("%d", &numb[i]);
		qsort( numa, n, sizeof(numa[0]), cmp1 );
		qsort( numb, n, sizeof(numb[0]), cmp2 );
		__int64 ans = 0;
		for ( i=0; i<n; i++ )
		{
			ans = ans+ (__int64)(numa[i])*(__int64)(numb[i]);
		}
		printf("Case #%d: %I64d\n", t, ans );
	}
	return 0;
}