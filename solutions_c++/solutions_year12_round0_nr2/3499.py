#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <cstring>
using namespace std;

FILE *in = fopen( "f.in" , "r" );

int N , S , P , A[ 111 ];

bool good( int a , int b , int c , int s ){
  if( a >= 0 && a <= 10 && b >= 0 && b <= 10 && c >= 0 && c <= 10 )
    if( a + b + c == s )
      return 1;
  return 0;
}

int gen1( int s ){
  int r = -1;
  for( int a = 0 ; a <= 10 ; a++ ){
    for( int b = a ; b <= a + 1 ; b++ ){
      for( int c = b ; c <= a + 1 ; c++ ){
	if( good( a , b , c , s ) ){
	  r = max( r , max( a , max( b , c ) ) );
	}
      }
    }
  }
  return r;
}

int gen2( int s ){
  int r = -1;
  for( int a = 0 ; a <= 10 ; a++ ){
    for( int b = a ; b <= a + 2 ; b++ ){
      for( int c = b ; c <= a + 2 ; c++ ){
	if( good( a , b , c , s ) && (a + 2 == b || a + 2 == c) ){
	  r = max( r , max( a , max( b , c ) ) );
	}
      }
    }
  }
  return r;
}

int f[ 111 ][ 111 ];

int main(){
  int ntest;
  fscanf( in , "%d" ,&ntest );
  
  freopen( "f.out" , "w" , stdout );
  
  for( int t = 1 ; t <= ntest ; t++ ){
    fscanf( in , "%d%d%d" ,&N ,&S ,&P );
    for( int q = 0 ; q < N ; q++ ){
      fscanf( in , "%d" ,&A[ q ] );
    }
    f[ N ][ 0 ] = 0;
    for( int q = 1 ; q <= S ; q++ ){
      f[ N ][ q ] = -10000000;
    }
    for( int q = N - 1 ; q >= 0 ; q-- ){
      for( int r = 0 ; r <= N - q ; r++ ){
	f[ q ][ r ] = -10000000;
	if( N - (q + 1) >= r ) f[ q ][ r ] = max( f[ q ][ r ] , (gen1( A[ q ] ) >= P) + f[ q + 1 ][ r ] );
	if( r ) f[ q ][ r ] = max( f[ q ][ r ] , (gen2( A[ q ] ) >= P) + f[ q + 1 ][ r - 1 ] );
      }
    }
    
    printf( "Case #%d: %d\n" ,t ,f[ 0 ][ S ] );
  }
  
  return 0;
}
