#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <fstream>

#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <utility>
#include <functional>

#include <cmath>
#include <cstring>
#include <ctime>
using namespace std;
const int NULA = 0;
const int MAXM = 10050;

const int AND[ 3 ][ 3 ] = { { 0, 0, 0 },
                            { 0, 1, 2 },
                            { 0, 2, 2 } };
const int OR[ 3 ][ 3 ] = { { 0, 1, 2 },
                           { 1, 1, 1 },
                           { 2, 1, 2 } };
const int BOTH[ 3 ][ 3 ] = { { 0, 2, 2 }, 
                             { 2, 1, 2 },
                             { 2, 2, 2 } };

int polje[ MAXM ];
int tip[ MAXM ];
int koliko[ MAXM ];
int m;
int n, v;

int rek( int where ) {
  int &ref = polje[ where ];
  if( ref != -1 ) return ref;
  
  if( tip[ where ] == 0 )
    ref = AND[ rek( where * 2 ) ][ rek( where * 2 + 1 ) ];
  else if( tip[ where ] == 1 )
    ref = OR[ rek( where * 2 ) ][ rek( where * 2 + 1 ) ];

  else {
    ref = BOTH[ rek( where * 2 ) ][ rek( where * 2 + 1 ) ];

    if( tip[ where ] - 2 == 0 ) {
      if( ref != AND[ rek( where * 2 ) ][ rek( where * 2 + 1 ) ] )
        ++koliko[ where ];
    }
    else 
      if( ref != OR[ rek( where * 2 ) ][ rek( where * 2 + 1 ) ] )
        ++koliko[ where ];
  }

  koliko[ where ] += koliko[ where * 2 ] + koliko[ where * 2 + 1 ];
  return ref;
}

int mod[ MAXM ][ 2 ];
const int inf = 0x3f3f3f3f;

#define call_and_1( i ) rek2( 2*i, 1 ) + rek2( 2*i+1, 1 )
#define call_and_0( i ) min( rek2( 2*i, 0 ) + rek2( 2*i+1, 0 ), min( rek2( 2*i, 0 ) + rek2( 2*i+1, 1 ), rek2( 2*i, 1 ) + rek2( 2*i+1, 0 ) ) )
#define call_or_1( i ) min( rek2( 2*i, 1 ) + rek2( 2*i+1, 1 ), min( rek2( 2*i, 0 ) + rek2( 2*i+1, 1 ), rek2( 2*i, 1 ) + rek2( 2*i+1, 0 ) ) )
#define call_or_0( i ) rek2( 2*i, 0 ) + rek2( 2*i+1, 0 )


int rek2( int i, int trebam ) {
  int &ref1 = polje[ i ];
  if( ref1 != 2 ) { 
    if( ref1 == trebam ) return 0;
    return inf;
  }

  //  printf( "na poziciji %d trebam %d\n", i, trebam );
  int &ref = mod[ i ][ trebam ];
  if( ref != -1 ) return ref;
  ref = inf;
  
  if( tip[ i ] == 0 )
    if( trebam ) return ref = call_and_1( i );
    else return ref = call_and_0( i );

  if( tip[ i ] == 1 )
    if( trebam ) return ref = call_or_1( i );
    else return ref = call_or_0( i );
    
  if( tip[ i ] == 2 ) 
    if( trebam ) return ref = min( call_and_1( i ), 1 + call_or_1( i ) );
    else return ref = min( call_and_0( i ), 1 + call_or_0( i ) );

  if( tip[ i ] == 3 ) 
    if( trebam ) return ref = min( 1 + call_and_1( i ), call_or_1( i ) );
    else return ref = min( 1 + call_and_0( i ), call_or_0( i ) );

  
  return ref;
}

int main( void ) {
  scanf( "%d", &n );
  int g, c;
  for( int i = 0; i < n; ++i ) {
    printf( "Case #%d: ", i+1 );
    memset( polje, -1, sizeof( polje ) ); 
    memset( koliko, 0, sizeof( koliko ) ); 
    memset( mod, -1, sizeof( mod ) ); 
    
    scanf( "%d%d", &m, &v );
    for( int j = 0; j < m / 2; ++j ) {
      scanf( "%d%d", &g, &c );
      tip[ j + 1 ] = 1 - g + 2 * c;
    }
    for( int j = m / 2; j < m; ++j ) 
      scanf( "%d", &polje[ j + 1 ] );
    
    if( rek( 1 ) != 2 && rek( 1 ) != v ) printf( "IMPOSSIBLE" );
    else if( rek( 1 ) == v ) printf( "0" );
    else printf( "%d", rek2( 1, v )  );
    printf( "\n" );
  }

  return NULA;
}
