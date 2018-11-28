#include <cstdio>
#include <cmath>
#include <vector>
#include <utility>
#include <algorithm>
#include <memory.h>
using namespace std;

#define forn( i,n ) for ( int i=0; i<(int)(n); i++ )
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef pair<int,int> pii;

int n, a[50];
char s[50];

int main()
{
  int t;
  scanf( "%d", &t );
  for ( int tc=1; tc<=t; tc++ )
  {
    scanf( "%d\n", &n );
    forn( i,n )
    {
      gets( s );
      a[i] = -1;
      forn( j,n )
        if ( s[j] == '1' ) a[i] = j;
    }

    int ans = 0;
    forn( i,n )
      if ( a[i] > i )
      {
        for ( int j=i+1; j<n; j++ )
          if ( a[j] <= i )
          {
            ans += j-i;
            int z = a[j];
            for ( int k=j; k>i; k-- )
              a[k] = a[k-1];
            a[i] = z;
            break;
          }
      }

    printf( "Case #%d: %d\n", tc, ans );
  }
}        