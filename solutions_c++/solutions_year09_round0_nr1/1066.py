#include <cstdio>
#include <memory.h>
#include <string>
using namespace std;

int n, m, L, all[20][26], ans;
char s[5010][20];
char t[1500];

int main()
{
  scanf( "%d %d %d\n", &L, &n, &m );

  for ( int i=0; i<n; i++ ) gets( s[i] );

  for ( int tc=1; tc<=m; tc++ )
  {
    gets( t );
    int ip = 0, i = 0;
    memset( all, 0, sizeof(all) );
    while ( i < (int)strlen(t) )
    {
      if ( t[i] == '(' )
      {
        i++;
        while ( t[i] != ')' )
        {
          all[ip][ t[i]-'a' ] = 1;
          i++;
        }
      }
      else
      {
        all[ip][ t[i]-'a' ] = 1;
      }
      ip++, i++;
    }

    ans = 0;
    for ( int i=0; i<n; i++ )
    {
      int fl = 1;
      for ( int j=0; j<L && fl; j++ )
        fl &= all[j][ s[i][j]-'a' ];
      ans += fl;
    }
    printf( "Case #%d: %d\n", tc, ans );
  }
}