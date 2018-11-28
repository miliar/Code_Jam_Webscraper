#include<iostream>
#include<string>
#include<vector>
#include<cstdio>
#include<map>
#include<algorithm>
using namespace std;

int COST[20][20][20];

#define inf 1000000

int DP[17][17][17][1<<16];

int solve( int pos, int t0, int tbef, int mask, int k )
{
	int &r = DP[t0][pos][tbef][mask];
	if( r >= 0 ) return r;

	r = inf;

	if( pos == k - 1 ){
		for( int i = 0; i < k; i ++ ){
			if( !(mask & (1<<i)) )
				continue;
			int v = COST[pos-1][tbef][i] + COST[pos][i][t0];
			r = min( r, v );
		}
		return r;
	}
	else if( pos == 0 ){
		for( int i = 0; i < k; i ++ ){
			if( !(mask & (1<<i)) )
				continue;
			int v = solve( pos + 1, i, i, mask & ~(1<<i), k );
			r = min( r, v );
		}
		return r;
	}
	else{
		for( int i = 0; i < k; i ++ ){
			if( !(mask & (1<<i)) )
				continue;
			int v = solve( pos + 1, t0, i, mask & ~(1<<i), k ) + COST[pos-1][tbef][i];
			r = min( r, v );
		}
		return r;
	}
}

int main( void )
{
	int N;
	cin >> N;
	for( int CC = 0; CC < N; CC ++ ){
		int k;
		string S;
		cin >> k >> S;
		int L = S.size();
		for( int i = 0; i < k; i ++ ){
			for( int p = 0; p < k; p ++ ){
				for( int q = 0; q < k; q ++ ){
					if( p == q ) continue;
					int c = 0;
					if( i == k - 1 ){
						for( int t = 0; t+k < L; t += k ){
							if( S[t+p] != S[t+k+q] )
								c ++;
						}
					}
					else{
						for( int t = 0; t < L; t += k ){
							if( S[t+p] != S[t+q] )
								c ++;
						}
					}
					COST[i][p][q] = c;
				}
			}
		}
		memset( DP, 0xff, sizeof(DP) );
		printf( "Case #%d: %d\n", CC + 1, 1 + solve( 0, 0, 0, (1<<k)-1, k ) );
	}
	return 0;
}
