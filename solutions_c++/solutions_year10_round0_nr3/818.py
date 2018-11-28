#include <cstdio>
#include <iostream>
using namespace std;

#define forn( i,n ) for ( int i=0; i<(int)(n); i++ )
typedef long long ll;

int a[1010], next[1010];
ll score[1010];
int r, k, n;

int main()
{
  int t;
  scanf( "%d", &t );
  for ( int q=1; q<=t; q++ )
  {
    scanf( "%d %d %d", &r, &k, &n );
    forn( i,n ) scanf( "%d", &a[i] );

    forn( i,n )
    {
      int j = 0;
      score[i] = 0;
      for ( next[i] = i; j<n && score[i] + a[ next[i] ] <= k; next[i] = ( next[i]+1 ) % n, j++ )
        score[i] += a[ next[i] ];
    } 

    ll ans = 0;
    int cur = 0;
    forn( z, r )
    {
      ans += score[ cur ];
      cur = next[ cur ];
    }

    printf( "Case #%d: ", q );
    cout << ans << endl;
  } 
} 