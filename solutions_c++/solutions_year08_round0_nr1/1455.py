//A. Saving the Universe
#include <cstdio>
#include <map>
#include <string>
#define MAX_CHARS 100+20
#define MAX_S 100+4
using namespace std;

map<string, int> M;
char s[ MAX_CHARS ];
int t[ MAX_S ];


void trim( char s[] )
{
  int dl = strlen ( s );
  while ( dl > 0  &&  ( s[ dl - 1 ] == ' '  ||  s[ dl - 1 ] == '\n' ) )
    s[ --dl ] = 0;
}


int main()
{
  int ilz;
  scanf("%i", &ilz);
  for(int xz=0; xz<ilz; xz++)
  {
    M.clear();
    
    int n;
    scanf("%i", &n);
    for(int x=0; x<n; x++)
    {
      do
      {
        fgets( s, MAX_CHARS, stdin );
        trim( s );
      } while ( s[ 0 ] == 0 );
      if( M.count( s ) == 0 ) {
        M[ s ] = M.size();
      }
    }
    
    int switches_cnt = 0;
    int free_searches = n;
    for(int x=1, Msize=M.size(); x<=Msize; x++)
      t[ x ] = -1;
    
    int m;
    scanf("%i", &m);
    while ( m -- )
    {
      do
      {
        fgets( s, MAX_CHARS, stdin );
        trim( s );
      } while ( s[ 0 ] == 0 );
      int nr = M[ s ];
      if( t[ nr ] != switches_cnt )
      {
        if( --free_searches == 0 )
        {
          switches_cnt++;
          free_searches = n - 1;
        }
        t[ nr ] = switches_cnt;
      }
    }
    
    printf("Case #%i: %i\n", xz + 1, switches_cnt);
  }
  return 0;
}
