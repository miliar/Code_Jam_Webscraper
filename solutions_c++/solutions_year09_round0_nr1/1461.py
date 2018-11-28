#include <cstdio>
#include <cstring>
using namespace std;
const int MAXN = 5000;
const int MAXL = 15;

char DICT[MAXN][MAXL+1];
char buff[MAXL*28+1];

char ima[MAXL][26];

int main()
{
  int l, n, t; scanf( "%d%d%d", &l, &n, &t );
  for( int i = 0; i < n; ++i )
    scanf( "%s", DICT[i] );

  for( int t_case = 0; t_case < t; ++t_case ) {
    scanf( "%s", buff );

    memset( ima, false, sizeof( ima ) );

    int slovo = 0;
    char zag = false;
    for( int i = 0; buff[i]; ++i )
      if ( buff[i] == '(' )
	zag = true;
      else if ( buff[i] == ')' ) {
	zag = false;
	++slovo;
      }
      else {
	ima[slovo][buff[i]-'a'] = true;
	if ( !zag ) ++slovo;
      }

    int sol = n;
    for( int i = 0; i < n; ++i )
      for( int j = 0; j < l; ++j )
	if ( !ima[j][DICT[i][j]-'a'] ) {
	  --sol;
	  break;
	}

    printf( "Case #%d: %d\n", t_case + 1, sol );
  }
  return 0;
}
