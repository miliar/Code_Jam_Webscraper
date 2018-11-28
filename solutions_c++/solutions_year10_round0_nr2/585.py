#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

struct bignum {
  int big[55];

  bignum( int x = 0 ) { memset( big, 0, sizeof big ); big[0] = x; }

  void input() {
    char s[55]; scanf( "%s", s );
    int x = 0; while( s[x] ) ++x; --x;
    for( int i = 0; x >= 0; --x, ++i ) big[i] = s[x]-'0';
  }

  void print() {
    int x = 54; while( x >= 1 && big[x] == 0 ) --x;
    while( x >= 0 ) printf( "%d", big[x--] );
    printf( "\n" );
  }

  friend bignum operator - ( bignum A, bignum B ) {
    bignum C;
    for( int i = 0; i < 55; ++i ) {
      C.big[i] += A.big[i];
      C.big[i] -= B.big[i];
      if( C.big[i] < 0 ) {
        --C.big[i+1];
        C.big[i] += 10;
      }
    }
    return C;
  }

  friend bignum operator % ( bignum A, bignum B ) {
    if( A < B ) return A;
    if( A == B ) return 0;

    for( int t = 54; t >= 0; --t ) {
      bignum x;
      for( int i = t; i < 55; ++i ) x.big[i-t] = A.big[i];
      while( B < x || x == B ) x = x - B;
      for( int i = t; i < 55; ++i ) A.big[i] = x.big[i-t];
    }

    return A;
  }

  friend bool operator < ( const bignum &A, const bignum &B ) {
    for( int i = 54; i >= 0; --i )
      if( A.big[i] != B.big[i] )
        return A.big[i] < B.big[i];
    return false;
  }

  friend bool operator == ( const bignum &A, const bignum &B ) {
    return !(A<B) && !(B<A);
  }
};

bignum gcd( bignum a, bignum b ) {
  while( 1 ) {
    if( a == 0 ) return b;
    if( b == 0 ) return a;
    if( a < b ) b = b % a;
    else a = a % b;
  }
  return 1;
}

int main( void ) {
  int tc; scanf( "%d", &tc );
  for( int t = 0; t < tc; ++t ) {
    int n; scanf( "%d", &n );

    bignum b[55];
    for( int i = 0; i < n; ++i ) {
      b[i].input();
      if( b[i] < b[0] ) swap( b[0], b[i] );
    }

    bignum a = b[0];
    bignum g = b[1]-a;
    for( int i = 2; i < n; ++i )
      g = gcd( g, b[i]-a );

    a = a % g;
    a = g - a;
    a = a % g;
    printf( "Case #%d: ", t+1 );
    a.print();
  }
  return 0;
}

