#include<iostream>
#include<cstdio>

using namespace std;

int D, I, M, N;
int A[1010], dp[102][300];

int main()
{
	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );
	int test_cases, casen = 0;
	for ( scanf( "%d", &test_cases ); test_cases > 0; test_cases -- )
	{
		scanf( "%d %d %d %d", &D, &I, &M, &N );
		for (int i = 0; i < N; i++ )
			scanf( "%d", &A[i] );
		for (int i = 0; i <= N; i++ )
			for (int j = 0; j < 256; j++ )
				dp[i][j] = (i == 0 ? 0 : 1000000000);
		for (int i = 0; i < N; i++ )
		{
			for (int j = 0; j < 256; j++ )
				for (int k = j + 1; k <= min(255, j + M); k++ )
					dp[i][k] = min( dp[i][k], dp[i][j] + I );
			for (int j = 255; j >= 0; j-- )
				for (int k = j - 1; k >= max(0, j - M); k-- )
					dp[i][k] = min( dp[i][k], dp[i][j] + I );
			for (int j = 0; j < 256; j++ )
				dp[i + 1][j] = min( dp[i + 1][j], dp[i][j] + D );
			for (int j = 0; j < 256; j++ )
				for (int k = 0; k < 256; k++ )
					if ( abs(j - k) <= M )
						dp[i + 1][k] = min( dp[i + 1][k], dp[i][j] + abs(A[i] - k) );
		}
		int ans = 1000000000;
		for (int j = 0; j < 256; j++ )
			ans = min( ans, dp[N][j] );
		printf( "Case #%d: %d\n", ++casen, ans );
	}
}
