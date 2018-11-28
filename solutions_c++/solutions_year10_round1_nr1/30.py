#include<iostream>
#include<cstdio>

using namespace std;

const int dx[] = {1, 1, 1, 0, 0, -1, -1, -1};
const int dy[] = {1, 0, -1, 1, -1, 1, 0, -1};

int A[52][52];
bool v[4];
char map[52][52];
int N, K;

int main()
{
	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );
	int Test_cases; scanf( "%d", &Test_cases );
	for (int TCase = 0; TCase < Test_cases; TCase ++ )
	{
		scanf( "%d %d", &N, &K );
		for (int i = 0; i < N; i++ )
			scanf( "%s", map[i] );
		memset( A, 0, sizeof( A ) );
		for (int i = 0; i < N; i++ )
		{
			int R = N;
			for (int j = N - 1; j >= 0; j-- )
				if ( map[i][j] == 'R' )
					A[i][--R] = 1;
				else if ( map[i][j] == 'B' )
					A[i][--R] = 2;
		}
		v[1] = v[2] = false;
		for (int k = 0; k < 8; k++ )
		for (int i = 0; i < N; i++ )
		if ( i + dx[k] * (K - 1) >= 0 && i + dx[k] * (K - 1) < N )
		for (int j = 0; j < N; j++ )
		if ( j + dy[k] * (K - 1) >= 0 && j + dy[k] * (K - 1) < N )
		{
			bool ok = true;
			for (int l = 1; l < K; l++ )
			if ( A[i + dx[k] * l][j + dy[k] * l] != A[i][j] ) ok = false;
			if ( ok ) v[A[i][j]] = true;
		}			
		printf( "Case #%d: ", TCase + 1 );
		if ( v[1] && v[2] ) cout << "Both" << endl;
		else if ( v[1] ) cout << "Red\n";
		else if ( v[2] ) cout << "Blue\n";
		else cout << "Neither\n";
	}
}
