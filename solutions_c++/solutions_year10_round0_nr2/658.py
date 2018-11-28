#include <cstdio>
using namespace std;

int n, a[1010];

long long gcd( long long a, long long b )
{
  return b ? gcd( b, a%b ) : a;
} 

long long aa( long long x )
{
  return x < 0 ? -x : x;
} 

int main()
{
  int t;
  scanf( "%d", &t );
  for ( int q=1; q<=t; q++ )
  {
    scanf( "%d", &n );
    for ( int i=0; i<n; i++ ) scanf( "%d", &a[i] );

    long long T = 0;
    for ( int i=0; i<n; i++ )
      for ( int j=0; j<i; j++ )
        T = gcd( T, aa( a[i]-a[j] ) );

    printf( "Case #%d: %I64d\n", q, ( T - (a[0]%T) ) % T );
  }                
}