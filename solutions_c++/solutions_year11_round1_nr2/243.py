#include<string>
#include<cstring>
#include<iostream>
#include<algorithm>

using namespace std ;

string S[ 120 ], A ;
bool aban[ 120 ], app[ 120 ][ 30 ] ;

int main( )
{
	int Ncase ;
	cin >> Ncase ;
	for( int T = 1 ; T <= Ncase ; T ++ )
	{
		int N, M ;
		cout << "Case #" << T << ":" ;
		cin >> N >> M ;
		memset( app, false, sizeof( app ) ) ;
		for( int i = 0 ; i < N ; i ++ ) 
		{
			cin >> S[ i ] ;
			for( int j = 0 ; j < S[ i ] . size( ) ; j ++ )
				app[ i ][ S[ i ][ j ] - 'a' ] =  true ;
		}
		for( int i = 0 ; i < M ; i ++ )
		{
			int flag = -1, cost ;
			cin >> A ;
			for( int j = 0 ; j < N ; j ++ )
			{
				int C = 0, l = 0 ;
				memset( aban, false, sizeof( aban ) ) ;
				for( int u = 0 ; u < N ; u ++ )
					if( S[ u ] . size( ) != S[ j ] . size( ) ) aban[ u ] = true ;
				for( int u = 0 ; u < 26 ; u ++ )
				{
					int k = A[ u ] - 'a' ;
					if( ! app[ j ][ k ] )
					{
						bool tragedy = false ;
						for( int v = 0 ; v < N ; v ++ )
							if( app[ v ][ k ] && !aban[ v ] ) aban[ v ] = tragedy = true ;
						if( tragedy ) C ++ ;
					}
					else
					{
						for( int p = 0 ; p < S[ j ] . size( ) ; p ++ ) if( S[ j ][ p ] == A[ u ] ) l ++ ;
						if( l == S[ j ] . size( ) ) break ;
						for( int v = 0 ; v < N ; v ++ )
							if( !aban[ v ] )
							{
								for( int p = 0 ; p < S[ j ] . size( ) ; p ++ )
									if( S[ j ][ p ] == A[ u ] ^ S[ v ][ p ] == A[ u ] )
									{
										aban[ v ] = true ;
										break ;
									}
							}
					}
				}
				if( flag == -1 || C > cost )
				{
					cost = C ;
					flag = j ;
				}
			}
			cout << ' ' << S[ flag ] ;
		}
		cout << endl ;
	}
	return 0 ;
}
