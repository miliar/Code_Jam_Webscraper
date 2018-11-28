#include <algorithm>
#include <stdio.h>
#include <math.H>

using namespace std;

__int64 A[1000], B[1000];

int compare1 (const void * a, const void * b)
{
	__int64 x = ( *(__int64*)a - *(__int64*)b );
	if (x>0)
		return 1;
	else if (x<0)
		return -1;
	else
		return 0;
}

int compare2 (const void * a, const void * b)
{
	__int64 x = ( *(__int64*)b - *(__int64*)a );
	if (x>0)
		return 1;
	else if (x<0)
		return -1;
	else 
		return 0;

}

void run()
{
	int n,i;
	scanf("%d\n", &n);
	for(i=0;i<n;i++)
		scanf("%I64d", &A[i]);

	for(i=0;i<n;i++)
		scanf("%I64d", &B[i]);

	qsort (A, n, sizeof(__int64), compare1);
	qsort (B, n, sizeof(__int64), compare2);

	__int64 ans=0;
	for(i=0;i<n;i++)
		ans+=A[i]*B[i];
	printf("%I64d\n", ans);

	
}

main()
{
	int i;
	int n;
	scanf("%d", &n);
	for (i=0; i<n; i++)
	{
		printf("Case #%d: ",i+1);
		run();
	}
	return 0;
}
