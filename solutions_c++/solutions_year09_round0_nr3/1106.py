#include <cstdio>
#include <memory.h>
#include <string>
using namespace std;

const int md = 10000;
const char* w = "welcome to code jam";
char s[510];
int f[510][20];

int main()
{
  int n;
  scanf( "%d\n", &n );
  for ( int tc=1; tc<=n; tc++ )
  {
    gets( s );
    if ( strlen(s) == 0 )
    {
      printf( "Case #%d: 0000\n", tc );
      continue;
    }

    for ( int i=0; i<19; i++ ) f[i][0] = 0;
    if ( s[0] == 'w' ) f[0][0] = 1;

    for ( int i=1; i < (int)strlen(s); i++ )
    {
      for ( int j=0; j<19; j++ )
      {
        f[i][j] = f[i-1][j];
        if ( j == 0 )
        {
          if ( s[i] == 'w' ) f[i][j] = ( f[i][j] + 1 ) % md;
        }
        else
        {
          if ( s[i] == w[j] ) f[i][j] = ( f[i][j] + f[i-1][j-1] ) % md;
        }
      }
    }
    printf( "Case #%d: %04d\n", tc, f[ strlen(s)-1 ][18] );
  }
}