#include<stdio.h>

const int N=1024;

int a[N], b[N];

inline bool inter(int i, int j)
{
	if( (a[i]<a[j] && b[i]>b[j]) || (a[i]>a[j] && b[i]<b[j]) )
		return 1;
	return 0;
}

void solve(int nr)
{
	int n, result=0;

	scanf("%d",&n);
	
	for( int i=1; i<=n; ++i)
		scanf("%d%d",&a[i],&b[i]);
	
	for( int i=1; i<=n; ++i)
		for( int j=i+1; j<=n; ++j)
			result+=inter(i,j);
	
	printf("Case #%d: %d\n",nr,result);
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	int t;
	scanf("%d",&t);
	
	for( int i=1; i<=t; ++i)
		solve(i);
	
	return 0;
}
