/*************************************
*Type         :
*Task         :
*Author       : This_poet
*Start Time   :
*Finish Time  :
*Result       :
*Algorithm    :
*************************************/
# include <cstdio>
# include <cstring>
# include <algorithm>
# include <iostream>
# include <cmath>
# define Debug puts("Orz!")
# define outit(x) cout<<#x<<" = "<<x<<endl
# define ps system("pause")
using namespace std;
typedef long long ll;
int test, a, b, hash[10001000];
int swp( int i, int power )
{
	int ret = i / power;
	int temp = i % power;
	if ( temp == 0 ) return -1;
	int p = 1;
	while ( p <= ret ) p *= 10;
	ret += p * temp;
	return ret;
}

int main()
{
	freopen( "in", "r", stdin );
	freopen( "out", "w", stdout );
	scanf( "%d", &test );
	for ( int t = 1; t <= test; t ++ )
	{
		memset( hash, 0, sizeof( hash ) );
		scanf( "%d%d", &a, &b );
		int ans = 0;
		for ( int i = a; i <= b; i ++ )
		{
			int power = 10;
			while ( power < i )
			{
				int temp = swp( i, power );
				if ( temp > i && temp <= b && hash[temp] != i )
				{
					hash[temp] = i;
					ans ++;
				}
				power *= 10;
			}
		}
		printf( "Case #%d: %d\n", t, ans );
	}
	return 0;
}
