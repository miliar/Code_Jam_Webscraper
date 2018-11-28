#include <cstdio>
#include <iostream>
using namespace std;

#define forn( i,n ) for ( int i=0; i<(int)(n); i++ )
typedef long long ll;

int main()
{
  int t;
  scanf( "%d", &t );
  ll n, k;
  for ( int q=1; q<=t; q++ )
  {
    cin >> n >> k;
    ll m = ( 1<<n ) - 1;
    printf( "Case #%d: ", q );
    if ( (k&m) == m ) puts( "ON" );
    else puts( "OFF" );
  } 
} 