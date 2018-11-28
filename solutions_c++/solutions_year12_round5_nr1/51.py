#include<iostream>
#include<cstdio>

using namespace std;

#define MAXN 1010
const int inf = 1000000000;

int N;
int L[MAXN];
int P[MAXN];
int O[MAXN];

void solve(int casen)
{
	scanf( "%d", &N );
	for (int i = 0; i < N; i++ )
		scanf( "%d", &L[i] );
	for (int i = 0; i < N; i++ )
		scanf( "%d", &P[i] );
	for (int i = 0; i < N; i++ )
		O[i] = i;
	for (int j = N - 1; j > 0; j-- )
	for (int i = 0; i < j; i++ )
	if (L[i] * (1 - P[i + 1]) > L[i + 1] * (1 - P[i]) || (L[i] * (1 - P[i + 1]) == L[i + 1] * (1 - P[i]) && (O[i] < O[i + 1])) )
	{
		swap( L[i], L[i + 1] );
		swap( P[i], P[i + 1] );
		swap( O[i], O[i + 1] );
	}
	printf( "Case #%d: ", casen );
	for (int i = 0; i < N; i++ )
		printf( "%d%c", O[N - 1 - i], (i == N - 1 ? '\n' : ' '));
}

int main()
{
	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );
	int test_cases;
	scanf( "%d", &test_cases );
	for (int i = 1; i <= test_cases; i++ )
		solve(i);
}

 