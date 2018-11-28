#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int compare(const void * a, const void * b)
{
	return *(int*)a - *(int*)b;
}
void solve()
{
	int N;
	int arr[2000];
	int srt[2000];
	scanf("%d",&N);
	int i;
	for( i = 0 ; i <  N ; i ++ )
	{
		scanf("%d", arr + i );
		srt[i] = arr[i];
	}
	double ans = 0;
	qsort( srt , N, sizeof(int) , compare );
	for( i = 0 ; i < N ; i ++ )
	{
		if( srt[i] != arr[i] )
			ans ++;
	}
	static int cc = 0;
	printf("Case #%d: %.6lf\n",++cc,ans);
}
int main()
{
	int N;
	scanf("%d",&N);
	while(N--) solve();
	return 0;
}
