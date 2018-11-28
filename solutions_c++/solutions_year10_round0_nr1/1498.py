#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
	freopen( "A.in", "r", stdin );
	freopen( "A.out", "w", stdout );
	int test_cases, N, K, casen = 0;
	for (scanf( "%d", &test_cases ); test_cases > 0; test_cases -- )
	{
		scanf( "%d %d", &N, &K );
		if ( (K % (1 << N)) == (1 << N) - 1 ) printf( "Case #%d: ON\n", ++ casen );
			else printf( "Case #%d: OFF\n", ++ casen );
	}
}
