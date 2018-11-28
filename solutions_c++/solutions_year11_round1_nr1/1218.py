#include<stdio.h>
#include<math.h>

long long int GCD(long long int a, long long int b)
{
    while( 1 )
    {
        a = a % b;
		if( a == 0 )
			return b;
		b = b % a;

        if( b == 0 )
			return a;
    }
}

void solve()
{
	long long int t, d,g, a, b, gcd, f;
	scanf("%lld %lld %lld", &t, &d, &g);

	if( d == 0 && g == 0 )
	{
		printf("Possible\n");
		return;
	}

	if( d == 0 && g != 100 ) 
	{
		printf("Possible\n");
		return;
	}
	if( g == 0 || (d == 0 && g == 100 ) )
	{
		printf("Broken\n");
		return;
	}

	gcd = GCD(d, 100);

	a = d/gcd;
	b = 100/gcd;
	f = t/a;
	if( b <= t )
	{
		
		//if( 100-b >= g-a || 100-b*f >= g-a*f )
		if( (d==100 && g==100) || g < 100 )
			printf("Possible\n");
		else
			printf("Broken\n");

	}
	else
	{
		printf("Broken\n");
	}
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("data.txt","r",stdin);
	freopen("out.txt","w",stdout);
#endif

	int T;
	scanf("%d\n", &T);
	for(int i = 1; i <= T; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}

	return 0;

}
