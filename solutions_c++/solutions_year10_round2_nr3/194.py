#include <cstdio>
#include <algorithm>

using namespace std;

int		C[501][501];
int		S[501][501];

void buildNoverk()
{
	// C[0][*] = 0 by default
	C[0][0] = 1;
	for( int n=1; n<=500; ++n )
	{
		for( int k=0; k<=500; ++k )
		{
			if( k == 0 )	C[n][k] = 1;
			else			C[n][k] = (C[n-1][k]+C[n-1][k-1]) % 100003;
		}
	}
}

int main()
{
	buildNoverk();

	for( int x=2; x<=500; ++x )
	{
		S[x][1] = 1;

		for( int l=2; l<=x-1; ++l )
		{
			S[x][l] = 0;

			for( int l2=1; l2<l; ++l2 )
			{
				S[x][l] = (int)((S[x][l] + ((long long)S[l][l2] * C[x-l-1][l-1-l2])) % 100003);
			}
		}
	}

	int T;
	scanf("%d",&T);

	int tcc = 1;
	while(T--)
	{
		int N;
		scanf("%d",&N);

		int sum = 0;
		for( int l=1; l<N; ++l )
			sum = (sum + S[N][l]) % 100003;

		printf("Case #%d: %d\n", tcc++, sum );

	}
	return 0;
}