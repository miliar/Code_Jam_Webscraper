#include <cstdio>
#include <iostream>

using namespace std;

const int MaxD = 15;
const int BASE = 10000;
const int BASELOG = 4;

class bignum {
public:
  int n;
  int a[ MaxD ];

  bignum() { n = 0; memset( a, 0, sizeof( a ) ); };

  bignum( int x ) {
    memset( a, 0, sizeof( a ) );

    n = 0;
    do {
      a[ n++ ] = ( x % BASE );
      x /= BASE;
    } while( x ); 
  }

  bignum( char *s ) {
    memset( a, 0, sizeof( a ) );
    n = 0;

    int len = strlen( s ), cnt = 0, last = len;
    for( int i = len-1; i >= 0; --i ) {
      cnt++;
      if( cnt == BASELOG || !i ) {
	a[n] = 0;
	for( int j = i; j < last; ++j )
	  a[n] = a[n]*10 + ( s[j]-'0' );
	last = i, n++;
	cnt = 0;
      }
    }
  };

  void trim() {
    int tmp = 0;
    for( int i = 0; i < n; ++i ) {
      a[i] += tmp;
      tmp = a[i] / BASE;
      a[i] %= BASE;
    }
    while( tmp ) {
      a[ n++ ] = tmp % BASE;
      tmp /= BASE;
    }

    while( n && !a[ n-1 ] ) --n;
  }

  friend bool operator < ( const bignum &a, const bignum &b ) {
    if( a.n != b.n ) return a.n < b.n;
    for( int i = a.n-1; i >= 0; --i )
      if( a.a[i] != b.a[i] ) return a.a[i] < b.a[i];
    return 0;
  }
  
  friend bool operator == ( const bignum &a, const bignum &b ) {
    if( a.n != b.n ) return 0;
    for( int i = 0; i < a.n; ++i )
      if( a.a[i] != b.a[i] ) return 0;
    return 1;
  }

  friend bool operator != ( const bignum &a, const bignum &b ) { return !( a == b ); }

  friend bignum operator + ( const bignum &a, const bignum &b ) {
    bignum ret;
    ret.n = ( a.n >? b.n );

    int tmp = 0;
    for( int i = 0; i < ret.n; ++i ) {
      ret.a[i] = ( a.a[i]+b.a[i]+tmp );
      if( ret.a[i] >= BASE ) {
	ret.a[i] -= BASE;
	tmp = 1;
      } else
	tmp = 0;
    }

    if( tmp ) ret.a[ ret.n++ ] = 1;

    ret.trim();
    return ret;
  }

  friend bignum operator - ( const bignum &a, const bignum &b ) {
    bignum ret;
    ret.n = a.n;

    int tmp = 0;
    for( int i = 0; i < a.n; ++i ) {
      ret.a[i] = ( a.a[i]-b.a[i]-tmp );
      if( ret.a[i] < 0 ) {
	ret.a[i] += BASE;
	tmp = 1;
      } else
	tmp = 0;
    }

    ret.trim();
    return ret;
  }

  friend bignum operator * ( const bignum &a, const bignum &b ) {
    bignum ret;

    ret.n = a.n+b.n-1;
    for( int i = 0; i < a.n; ++i )
      for( int j = 0; j < b.n; ++j )
	ret.a[ i+j ] += ( a.a[i]*b.a[j] );
    
    ret.trim();
    return ret;
  }

  friend bignum operator / ( const bignum &a, const bignum &b ) {
    bignum d, e, t, r, ret;

    int len = 0;
    r = 0;
    for( int pos = a.n-1; pos >= 0; --pos ) {
      r = r*BASE;
      r = r + a.a[pos];

      int lo = 0, hi = BASE-1;
      while( lo < hi ) {
	int mid = ( lo+hi+1 ) / 2;
	d = b*mid;
	if( d < r || d == r ) lo = mid; else
	  hi = mid-1;
      }
	
      ret.a[pos] = lo;
      d = b*lo;
      r = r-d;
      if( ret.a[pos] > 0 && pos >= len ) len = pos+1;
    }

    ret.n = len;
    ret.trim();
    return ret;
  }
  
  friend bignum operator % ( const bignum &a, const bignum &b ) {
    return a - ( a/b )*b;
  }

  void print() {
    printf( "%d", a[ n-1 ] );
    for( int i = n-2; i >= 0; --i )
      printf( "%04d", a[i] );
    putchar( '\n' );
  }
};

char s[55];
bignum a[1005];

bignum gcd( bignum a, bignum b ) { 
  if( 0 < b ) return gcd( b, a%b );
  return a; 
}

int main( void ) {
  int t;
  scanf( "%d", &t );
  for( int c = 1; c <= t; ++c ) {
    int n;
    scanf( "%d", &n );
    for( int i = 0; i < n; ++i ) {
      scanf( "%s", s );
      a[i] = bignum( s );
    }

    bignum l = 0, x;
    for( int i = 0; i < n; ++i )
      for( int j = i+1; j < n; ++j ) {
	if( a[i] < a[j] ) x = a[j]-a[i]; else
	  x = a[i]-a[j];
	l = gcd( l, x );
      }

    bignum ans = l - ( a[0]%l );
    if( ans == l ) ans = 0;
    
    printf( "Case #%d: ", c );
    ans.print();
  }
  return 0;
}
