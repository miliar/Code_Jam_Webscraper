#include<iostream>
#include<cstdio>

using namespace std;

const int MAX[] = {1, 10, 100, 1000, 10000, 100000, 1000000};
int Primes[1000010], R = 0;
int A[200];

int getrev(int a, int b)
{
	if ( a == 1 ) return 1;
	long long t = getrev(b % a, a);
	int ret = ((1 - b * t) / a) % b;
	if ( ret < 0 ) ret += b;
	return ret;
}

long long div(int A, int B, int M)
{
	if ( A < 0 ) A += M; if ( B < 0 ) B += M;
	//cout << A << " " << B << " " << M << endl;
	int t = getrev(B, M);
	return (t * (long long)A) % M;
}

void initPrime()
{
	for (int i = 2; i <= 1000100; i++ )
	{
		bool ok = true;
		for (int j = 2; j * j <= i; j++ )
			if (i % j == 0) ok = false;
		if (ok) Primes[R++] = i;
	}
}

void update(int &A, int B)
{
	//cout << "here\n";
	if (A == -2) A = B;
	else if (A != B) A = -1;
}

int main()
{
	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );
	initPrime();
	int test_cases, casen = 0, D, K;
	for ( scanf( "%d", &test_cases ); test_cases > 0; test_cases -- )
	{
		scanf( "%d %d", &D, &K );
		for (int i = 0; i < K; i++ ) scanf( "%d", &A[i] );
		int Max = 0;
		for (int i = 0; i < K; i++ ) Max = max( Max, A[i] );

		int ans = -2;
		if ( A[0] == A[1] ) ans = A[0];
		else if (K <= 2) ans = -1;
		else
		{
			long long AA, B;
			for (int p = 0; Primes[p] <= MAX[D]; p++ )
			if ( Primes[p] > Max )
			{
				//cout << p << endl;
				AA = div( A[2] - A[1], A[1] - A[0], Primes[p] );
				B = (A[1] - A[0] * AA) % Primes[p];

				//cout << A[0] << " " << A[1] << " " << A[2] << " " << AA << " " << B << " " << Primes[p] << endl;

				bool ok = true;
				for (int i = 2; i < K; i++ )
				if ( (AA * A[i - 1] + B - A[i]) % Primes[p] != 0 ) ok = false;

				if (ok) update( ans, (AA * A[K - 1] + B + Primes[p]) % Primes[p] );
			}
		}
		printf( "Case #%d: ", ++casen );
		if ( ans <= -1 ) cout << "I don't know.\n"; else cout << ans << endl;
	}
}
