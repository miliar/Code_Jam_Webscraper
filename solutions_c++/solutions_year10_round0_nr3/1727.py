#include <stdio.h>

int r , k , n;
int mass[ 10000 ];
long long sum;
long long ans;

long long much[ 10000 ];
int next[ 10000 ];

void read()
{
	scanf( "%d%d%d" , &r , &k , &n );
	sum = 0;
	for(int i = 0;i < n;++i)
	{
		scanf( "%d" , mass + i );
		sum += mass[ i ];
		mass[ i + n ] = mass[ i ];
	}
}

void work()
{
	if( sum < k )
	{
		ans = r * sum;
		return;
	}
	ans = 0;
	for(int i = 0;i < n;++i)
	{
		long long local = 0;
		for(int j = i;;++j)
		{
			if( local + mass[ j ] > k )
			{
				much[ i ] = local;
				next[ i ] = j % n;
				break;
			}
			local += mass[ j ];
		}
	}
	int last = 0;
	for(int i = 0;i < r;++i)
	{
		ans += much[ last ];
		last = next[ last ];
	}
}

int main()
{
	freopen( "C-large.in"  , "r" , stdin  );
	freopen( "C-large.out" , "w" , stdout );
	int t;
	scanf( "%d" , &t );

	for(int test = 1;test <= t;++test)
	{
		read();
		work();
		printf( "Case #%d: %lld\n" , test , ans );
	}

	return 0;
}