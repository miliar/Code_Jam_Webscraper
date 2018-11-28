
#include <tchar.h>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>

using namespace std;

set<string, less<string> > s;
set<string, less<string> >::const_iterator it;


int _tmain(int argc, _TCHAR* argv[])
{
  int T,N,M;
  FILE *fIn,*fOut;
  int i,j;
  int nMkDir;
  char c;
  char ac[101];

  if ( argc != 3 ) return -1;
  fIn = fopen( argv[1], "rt" );
  fOut = fopen( argv[2], "wt" );

  fscanf( fIn, "%d", &T );

  for ( int t=1; t <= T; t++ )
  {
    nMkDir = 0;
    s.clear();
    fscanf( fIn, "%d %d", &N, &M );
    for ( i=0; i < N; i++ )
    {
      fscanf( fIn, "%s", ac );
      for ( j=1; j < strlen(ac); j++ )
      {
        if ( ac[j] == '/' )
        {
          ac[j] = 0;
          s.insert(ac);
          ac[j] = '/';
        }
      }
      s.insert(ac);
    }
    for ( i=0; i < M; i++ )
    {
      fscanf( fIn, "%s", ac );
      for ( j=1; j < strlen(ac); j++ )
      {
        if ( ac[j] == '/' )
        {
          ac[j] = 0;
          if ( s.find(ac) == s.end() )
          {
            s.insert(ac);
            nMkDir++;
          }
          ac[j] = '/';
        }
      }
      if ( s.find(ac) == s.end() )
      {
        s.insert(ac);
        nMkDir++;
      }
    }
    fprintf( fOut, "Case #%d: %d\n", t, nMkDir );
  }

  fclose( fIn );
  fclose( fOut );

	return 0;
}

