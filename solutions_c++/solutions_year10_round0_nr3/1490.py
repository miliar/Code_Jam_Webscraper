#include<iostream>
#include<cstdio>

using namespace std;

int Sum[2010], Next[2010];
int v[2010], A[2010];

int main()
{
	freopen( "C.in", "r", stdin );
	freopen( "C.out", "w", stdout );
	int test_cases;
	scanf( "%d", &test_cases );

	for (int casen = 1; casen <= test_cases; casen ++ )
	{
		int R, K, N;
		scanf( "%d %d %d", &R, &K, &N );
		for (int i = 0; i < N; i++ ) scanf( "%d", &A[i] );

		long long sum = 0, ans = 0;
		for (int i = 0; i < N; i++ ) sum += A[i];
		
		if ( sum <= K ) ans = sum * R;
		else
		{
			int k = 0; sum = 0;
			for (int i = 0; i < N; i++ )
			{
				while (sum + A[k % N] <= K) sum += A[(k ++) % N];
				Next[i] = k % N; Sum[i] = sum; sum -= A[i];
			}

			if ( R <= 4 * N )
			{
				int t = 0;
				for (int i = 0; i < R; i++ )
				{
					ans += Sum[t];
					t = Next[t];
				}
			}
			else
			{
				int t = 0; k = 0;
				memset( v, 0, sizeof( v ) );
				while ( v[t] == 0 )
				{
					v[t] = ++ k;
					ans += Sum[t];
					t = Next[t];
				}
			
				int round = (k + 1) - v[t];
				long long roundcost = 0;
				for (int p = 0; p < round; p++ )
				{
					roundcost += Sum[t];
					t = Next[t];
				}

				ans += ((R - k) / round) * roundcost;
				for (int i = 0; i < (R - k) % round; i++ )
				{
					ans += Sum[t];
					t = Next[t];
				}
			}
		}
		printf( "Case #%d: %I64d\n", casen, ans );
	}
}
