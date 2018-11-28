#include <cstdio>
#include <cstring>
using namespace std;
const int MAXL = 70;

char buff[MAXL+1];
char bio[36];

int main()
{
  int t; scanf( "%d", &t );
  for( int t_case = 0; t_case < t; ++t_case ) {
    scanf( "%s", buff );
    int base = 0;
    memset( bio, false, sizeof( bio ) );
    for( int i = 0; buff[i]; ++i ) {
      int x = 0;
      if ( buff[i] >= 'a' && buff[i] <= 'z' )
	x = buff[i] - 'a' + 10;
      else
	x = buff[i] - '0';
      
      if ( !bio[x] )
	++base;
      bio[x] = true;
    }
    if ( base == 1 ) base = 2;
    
    memset( bio, -1, sizeof( bio ) );

    long long sol = 0;
    int seen = 0;
    for( int i = 0; buff[i]; ++i ) {
      int x = 0;
      if ( buff[i] >= 'a' && buff[i] <= 'z' )
	x = buff[i] - 'a' + 10;
      else
	x = buff[i] - '0';

      if ( bio[x] == -1 ) {
	if ( seen == 0 )
	  bio[x] = 1;
	else if ( seen == 1 )
	  bio[x] = 0;
	else
	  bio[x] = seen;
	++seen;
      }
      sol = sol * base + bio[x];
    }
    printf( "Case #%d: %lld\n", t_case + 1, sol );
  }
  return 0;
}
