#include<iostream>
#include<string>
#include<vector>
#include<cstdio>
#include<map>
#include<algorithm>
using namespace std;

int G[100000];
int C[100000];
int DP[10005][2];

#define inf 40000

int solve( int pos, int desired_value )
{
	int &ret = DP[pos-1][desired_value];
	if( ret >= 0 ) return ret;

	int type = G[pos-1];
	int c    = C[pos-1];

	if( type < 0 ){
		if( c == desired_value ) return ret=0; else return ret=inf;
	}
	else if( type == 1 ){ // AND
		if( desired_value == 1 ){
			int v = solve( pos * 2, 1 ) + solve( pos * 2 + 1, 1 );
			if( c )
				v = min( v,
						1 + min(
							solve( pos * 2, 0 ) + solve( pos * 2 + 1, 1 ),
							solve( pos * 2, 1 ) + solve( pos * 2 + 1, 0 )
						)
					);
			return ret=v;
		}
		else{
			int v = 
				min(
					solve( pos * 2, 0 ) + solve( pos * 2 + 1, 1 ),
					solve( pos * 2, 1 ) + solve( pos * 2 + 1, 0 )
				);
			v = min( v, solve( pos * 2, 0 ) + solve( pos * 2 + 1, 0 ) );
			return ret=v;
		}
	}
	else{ // OR
		if( desired_value == 1 ){
			int v = 
				min(
					solve( pos * 2, 0 ) + solve( pos * 2 + 1, 1 ),
					solve( pos * 2, 1 ) + solve( pos * 2 + 1, 0 )
				);
			v = min( v, solve( pos * 2, 1 ) + solve( pos * 2 + 1, 1 ) );
			return ret=v;
		}
		else{
			int v = solve( pos * 2, 0 ) + solve( pos * 2 + 1, 0 );
			if( c )
				v = min( v,
						1 + min(
							solve( pos * 2, 0 ) + solve( pos * 2 + 1, 1 ),
							solve( pos * 2, 1 ) + solve( pos * 2 + 1, 0 )
						)
					);
			return ret=v;
		}
	}
}

int main( void )
{
	int N;
	cin >> N;
	for( int CC = 0; CC < N; CC ++ ){
		int M, V;
		cin >> M >> V;
		int Mi = (M-1) / 2, Ml = (M+1) / 2;
		for( int i = 0; i < Mi; i ++ ){
			cin >> G[i] >> C[i];
		}
		for( int i = 0; i < Ml; i ++ ){
			cin >> C[i+Mi];
			G[i+Mi] = -1;
		}
		memset( DP, 0xff, sizeof(DP) );
		int v = solve( 1, V );
		if( v < inf )
			printf( "Case #%d: %d\n", CC + 1, v );
		else
			printf( "Case #%d: IMPOSSIBLE\n", CC + 1 );
	}
}
