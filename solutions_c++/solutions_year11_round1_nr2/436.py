#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;
typedef long long ll;


pair<string,int> ar[ 100 ];
string listas[ 10 ];
pair<int,string> best[ 10 ];
int pog[ 10 ];
bool marc[ 100 ];
int n, m, casos;

bool comp( const pair<string,int> &a, const pair<string,int>& b ){
	return a.first.size() < b.first.size();
}

bool contem( string& a, char c ){
	for( int i = a.size() - 1; i >= 0; --i ){
		if( a[ i ] == c )
			return true;
	}
	return false;
}

int calc( string& lista, string& p ){
	int pts = 0;
	int tam = p.size();
	int ini = 0, fim;
	fill( marc, marc + 100, true );
		
	while( ar[ ini ].first.size() != tam ) ++ini;
	fim = ini;
	while( fim < n && ar[ fim ].first.size() == tam ) ++fim;
	 
	for( int c = 0; c < 26; ++c ){
		bool tem = false;
		for( int i = ini; i < fim; ++i ){
			if( marc[ i ] && contem( ar[ i ].first, lista[ c ] ) ){
				tem = true;
				break;
			}
		}
		if( tem ){
			if( contem( p, lista[ c ] ) ){
				for( int i = ini; i < fim; ++i ){
					if( !marc[ i ] ) continue;

					for( int k = 0; k < tam; ++k ){
						if( p[ k ] == lista[ c ] && ar[ i ].first[ k ] != lista[ c ] ){
							marc[ i ] = false;
							break;
						}else if( p[ k ] != lista[ c ] && ar[ i ].first[ k ] == lista[ c ] ){
							marc[ i ] = false;
						}
							
					}
					
				}
			}else{
				for( int i = ini; i < fim; ++i ){
					if( contem( ar[ i ].first, lista[ c ] ) )
						marc[ i ] = false;
				}
				++pts;
			}
		}
		
	}
	
	return pts;
}

int main(){

	
	scanf( "%d", &casos );
	for( int c = 1; c <= casos; ++c ){
		scanf( "%d %d", &n, &m );
		for( int i = 0; i < n; ++i ){
			cin >> ar[ i ].first;
			ar[ i ].second = i;
		}
			
		for( int i = 0; i < m; ++i )
			cin >> listas[ i ];
		
		sort( ar, ar + n, comp );
		
		for( int i = 0; i < m; ++i ){
			best[ i ].first = -1;
			pog[ i ] = 1000000;
			
			for( int p = 0; p < n; ++p ){
				int temp = calc( listas[ i ], ar[ p ].first );
				if( temp > best[ i ].first ){
					best[ i ].first = temp;
					pog[ i ] = ar[ p ].second;
					best[ i ].second = ar[ p ].first;
				}else if( temp == best[ i ].first ){
					if( pog[ i ] > ar[ p ].second ){
						pog[ i ] = ar[ p ].second;
						best[ i ].second = ar[ p ].first;
					}
				}
			}
		}
		printf( "Case #%d:", c );
		for( int i = 0; i < m; ++i ){
			cout << " " << best[ i ].second;
		}
		cout << endl;
	}
}


