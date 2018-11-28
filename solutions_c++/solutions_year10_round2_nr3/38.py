#include <iostream>
#include <vector>
using namespace std;
#define MOD 100003

int rev[100003];

int C( int n, int m )
{
	long long ret = 1;
	for( long long i = 1; i <= n; i ++ ){
		ret *= i;
		ret %= MOD;
	}
	for( long long i = 1; i <= m; i ++ ){
		ret *= rev[i];
		ret %= MOD;
	}
	for( long long i = 1; i <= n-m; i ++ ){
		ret *= rev[i];
		ret %= MOD;
	}
//	cerr << n << "C" << m << " = " << ret << endl;
	return (int)ret;
}

int DP[600][600];
int solve( long long n0, long long n1 )
{
	if( n1 == 1 )
		return 1;
	if( DP[(int)n0][(int)n1] >= 0 )
		return DP[(int)n0][(int)n1];
	long long ret = 0;
	for( int n2 = 1; n2 < n1; n2 ++ ){
		int n = n0 - n1 - 1;
		int m = n1 - n2 - 1;
		if( n >= m ){
			ret += (long long)solve( n1, n2 ) * (long long)C(n, m);
			ret %= MOD;
		}
	}
	return DP[(int)n0][(int)n1] = (int)ret;
}

int main( void )
{
	memset( rev, 0xff, sizeof(rev) );
	for( int i = 1; i < MOD; i ++ ){
		for( int j = i; j < MOD; j ++ ){
			int m = (long long)i * j % MOD;
			if( m == 1 ){
				if( rev[i] >= 0 ) exit(1);
				rev[i] = j;
				rev[j] = i;
			}
		}
	}
	for( int i = 1; i < MOD; i ++ ){
		if( rev[i] < 0 ) exit(1);
	}

	int C;
	cin >> C;
	memset( DP, 0xff, sizeof(DP) );
	for( int CC = 1; CC <= C; CC ++ ){
		int n0;
		cin >> n0;
		int ret = 0;
		for( int n1 = 1; n1 < n0; n1 ++ ){
			ret += solve(n0, n1);
			ret %= MOD;
		}
		printf( "Case #%d: %d\n", CC, ret );
	}
	return 0;
}
