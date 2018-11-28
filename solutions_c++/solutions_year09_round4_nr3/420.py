#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <deque>
#include <cstring>
#include <algorithm>
#include <cassert>
#include <cstdio>

using namespace std;

const int N = 202;

int maxflow( const int m[N][N], int n, int s, int t ) {
	static int val[N];
	static deque<int> d;
	static int f[N][N];
	static int dad[N];
	int flow = 0;
	
	for( int i = 0; i < n; ++i ) {
		for( int j = 0; j < n; ++j ) {
			f[i][j] = 0;
		}
	}
	
	while(1) {
		memset( val, 0, sizeof(int)*n );
		val[s] = 0x7FFFFFFF;
		dad[s] = -1;
		d.clear();
		d.push_back(s);
		
		while( !d.empty() ) {
			int k = d.front(); d.pop_front();
			
			if( k == t ) {
				flow += val[t];
				for( int i = t; dad[i] != -1; i = dad[i] ) {
					f[dad[i]][i] += val[t];
					f[i][dad[i]] -= val[t];
				}
				goto nextpath;
			} else {
				for( int i = 0; i < n; ++i ) {
					if( val[i] == 0 && f[k][i] < m[k][i] ) {
						val[i] = min( val[k], m[k][i]-f[k][i] );
						dad[i] = k;
						d.push_back(i);
					}
				}
			}
		}
		break;
		nextpath:;
	}
	return flow;
}

vector<int> prices[100];
int matrix[N][N];

int main() {
	int cases;
	int n, k;
	
	scanf( "%d", &cases );
	for( int caseid = 1; caseid <= cases; ++caseid ) {
		scanf( "%d%d", &n, &k );
		for( int i = 0; i < n; ++i ) {
			prices[i].clear();
			for( int j = 0; j < k; ++j ) {
				int t;
				scanf( "%d", &t );
				prices[i].push_back( t );
			}
		}
		memset( matrix, 0, sizeof(matrix) );
		sort( prices, prices+n );
		for( int i = 0; i < n; ++i ) {
			for( int j = i+1; j < n; ++j ) {
				for( int l = 0; l < k; ++l ) {
					if( prices[i][l] >= prices[j][l] ) goto no;
				}
				matrix[i][n+j] = 1;
				no:;
			}
		}

		for( int i=0; i < n; ++i ) {
			matrix[2*n][i] = 1;
			matrix[n+i][2*n+1] = 1;
		}

		int result = maxflow( matrix, 2*n+2, 2*n, 2*n+1 );
		
		
		printf( "Case #%d: %d\n", caseid, n-result );
	}
	return 0;
}
