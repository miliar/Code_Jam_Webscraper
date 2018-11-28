#include<stdio.h>
#include<stdlib.h>

__int64 a[100010];
__int64 b[100010];

int cmp( const void *a, const void *b )
{
	return *(__int64 *)a - *(__int64 *)b;
}


int main()
{
	freopen("temp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d", &T);
	int ca;
	for( ca=0; ca<T; ca++ )
	{
		int n;
		scanf("%d", &n);
		int i;
		for( i=0; i<n; i++ )
			scanf("%I64d", &a[i]);
		for( i=0; i<n; i++ )
			scanf("%I64d", &b[i]);
		qsort(a,n, sizeof(a[0]), cmp);
		qsort(b,n, sizeof(b[0]), cmp);
		__int64 ans = 0;
		for( i=0; i<n; i++ )
		{
			ans += a[i]*b[n-i-1];
		}
		printf("Case #%d: %I64d\n", ca+1, ans);
	}
	return 0;
}