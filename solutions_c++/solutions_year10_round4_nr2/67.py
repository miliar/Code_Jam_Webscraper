#include <iostream>
#include <vector>
using namespace std;

int M[10240];
int price[10240];

// i -> 2*i+1, 2*i+2
// i (i>=N-1) -> M[N-1+(i-(N-1))]
/*
	0
		1
			3
				7=7
				8=6
			4
				9=5
				104
		2
			5
				113
				122
			6
				131
				140
*/
int DP[1024][12];
int N;
int solve( int pos, int miss )
{
	if( pos >= N-1 ){
//		cerr << pos << " " << (N-1-(pos-(N-1))) << " " << miss << " " << M[N-1+(pos-(N-1))] << endl;
		if( miss <= M[N-1-(pos-(N-1))] )
			return 0;
		else
			return -1;
	}
	if( DP[pos][miss] != -2 ) return DP[pos][miss];
	int ret = -1;
	{
		int v1 = solve( pos * 2 + 1, miss );
		int v2 = solve( pos * 2 + 2, miss );
		if( v1 >= 0 && v2 >= 0 ){
			int v = v1 + v2 + price[pos];
			if( ret < 0 || ret > v ) ret = v;
		}
	}
	{
		int v1 = solve( pos * 2 + 1, miss + 1 );
		int v2 = solve( pos * 2 + 2, miss + 1 );
		if( v1 >= 0 && v2 >= 0 ){
			int v = v1 + v2 + 0;
			if( ret < 0 || ret > v ) ret = v;
		}
	}
//	cerr << pos << " " << miss << " = " << ret << endl;
	return DP[pos][miss]=ret;
}

int main( void )
{
	int C;
	cin >> C;
	for( int CC = 1; CC <= C; CC ++ ){
		int P;
		cin >> P;
		N = 1 << P;
		for( int i = 0; i < N; i ++ )
			cin >> M[i];
		for( int i = 0; i < N-1; i ++ )
			cin >> price[N-2-i];

/*
		for( int i = 0; i < N; i ++ )
			cerr << M[i] << " ";
		cerr << endl;
		for( int i = 0; i < N-1; i ++ )
			cerr << price[i] << " ";
		cerr << endl;
*/
		for( int i = 0; i < 1024; i ++ )
			for( int j = 0; j < 12; j ++ )
				DP[i][j] = -2;
		printf( "Case #%d: %d\n", CC, solve( 0, 0 ) );
	}
	return 0;
}
