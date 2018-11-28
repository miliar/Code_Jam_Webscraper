#include <vector>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

FILE *in = fopen( "B-large (1).in" , "r" );

int N , X , Y;
pair< int , int > a[ 1111 ];
int ans[ 1111 ][ 2 ];

bool Can( vector< int > p ){
  int x = 0 , y = a[ 0 ].first , nx = a[ 0 ].first;
  int iind = 0 , endind = p.size();
  while( iind < endind ){
    int ind = p[ iind ] + 1;
    if( !( y != 0 && y + a[ ind ].first > Y ) && !( x != 0 && x + a[ ind ].first > X ) ){
      ans[ a[ ind ].second ][ 0 ] = x == 0 ? 0 : x + a[ ind ].first;
      ans[ a[ ind ].second ][ 1 ] = y == 0 ? 0 : y + a[ ind ].first;
      y = y == 0 ? a[ ind ].first : y + 2 * a[ ind ].first;
      iind ++;
      nx = max( nx , x == 0 ? a[ ind ].first : x + 2 * a[ ind ].first );
    }
    else if( x != 0 && x + a[ ind ].first > X ){
      return 0;
    } 
    else{
      x = nx;
      y = 0;
    }
  }
  return 1;
}

int main(){
  freopen( "f.out" , "w" , stdout );
  int T;
  fscanf( in , "%d"  ,&T );
  
  for( int kase = 1 ; kase <= T ; kase++ ){
    fscanf( in , "%d%d%d" ,&N ,&X ,&Y );
    for( int q = 0 ; q < N ; q++ ){
      fscanf( in , "%d" ,&a[ q ].first );
      a[ q ].second = q;
    }
    sort( a , a + N );
    for( int q = 0 ; q < N / 2 ; q++ ){
      swap( a[ q ] , a[ N - q - 1 ] );
    } 
    ans[ a[ 0 ].second ][ 0 ] = 0;
    ans[ a[ 0 ].second ][ 1 ] = 0;
    
    vector< int > p , sor;
    for( int q = 0 ; q < N - 1 ; q++ ){
      p.push_back( q );
      sor.push_back( q );
    }
    reverse( p.begin() , p.end() );
    if( Can( p ) ){
      printf( "Case #%d:" ,kase );
      for( int q = 0 ; q < N ; q++ ){
	printf( " %d %d" ,ans[ q ][ 0 ] ,ans[ q ][ 1 ] );
      }
      printf( "\n" );
      goto DONE;
    }
    printf( "ERRROOOOORRRR\n" );
    DONE:;
  }
  
  return 0;
}
