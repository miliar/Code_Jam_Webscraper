#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char g[] = "ynficwlbkuomxsevzpdrjgthaq";
char h[26];
char s[10000];

int main( void ) {
  for( int i = 0; i < 26; ++i )
    h[ g[i]-'a' ] = 'a'+i;

  int t;
  scanf( "%d", &t );
  gets(s);
  for( int cn = 1; cn <= t; ++cn ) {
    gets( s );
    int l = strlen(s);
    for( int i = 0; i < l; ++i )
      if( s[i] >= 'a' && s[i] <= 'z' ) s[i] = h[ s[i]-'a' ];
  
    printf( "Case #%d: %s\n", cn, s );
  }
  return 0;
}
