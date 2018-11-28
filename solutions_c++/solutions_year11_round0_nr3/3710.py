#include<stdio.h>

void solve()
{
	int n, a[1010], v=0, vv=0, s = 1000001;
	scanf("%d\n", &n );
	for(int i = 0; i < n; i++)
	{
		scanf("%d", a+i);
		v  = v^a[i];
		vv += a[i];
		if( a[i] < s )
			s = a[i];
	}

	if( v > 0 )
		printf("NO\n");
	else
		printf("%d\n", vv-s);


}
int main()
{
#ifndef ONLINE_JUDGE
	freopen("data.txt","r",stdin);
	freopen("out.txt","w",stdout);
#endif

	int T;
	scanf("%d\n", &T);

	for( int i = 1; i <= T; i++ )
	{
		printf("Case #%d: ", i);
		solve();
	}

	return 0;

}
