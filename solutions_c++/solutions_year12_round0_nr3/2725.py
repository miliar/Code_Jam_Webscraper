#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#define MAX 2000010

using namespace std;

int color[MAX];

long long getans( long long a, long long b )
{
	memset( color, 0, sizeof( color ) );
	long long ts = 1, temp = a;
	while( temp )
	{
		ts = ts * 10;
		temp /= 10;
	}
	//printf("--%ld\n", ts );
	long long ans = 0;
	for( long long i = a; i <= b; i++ )
	{
		if( color[i] == 0 )
		{
			long long cnt = 0;
			long long tsx = ts, st = 1, c = i ;
			while( st < tsx  )
			{
				long long v = (tsx/st)*( c % st ) + c/st;
				//printf("%lld\n", v );
				st *= 10;
				if( (i/v) < 10 && v >= a && v <= b && color[v] == 0 )
				{
				 	cnt += 1;
					color[v] = 1;
				}
			}
			ans += ( cnt*(cnt - 1) )/2;
		}
		//printf("\n");
	}
	return ans;
}
int main()
{
	int t;
	scanf("%d", &t );
	for( int i = 1; i <= t; i++ )
	{
		long a, b;
		scanf("%ld%ld", &a, &b );
		printf("Case #%d: %lld\n", i, getans( a, b ) );
	}
	return 0;
}
