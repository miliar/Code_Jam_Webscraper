
#include <tchar.h>
#include <fstream>
#include <iostream>

using namespace std;

int GetRank( int s, int x )
{
  int m = 1;
  int r = 0;
  if ( !(s & (1<<(x-2)) ) ) return -1;
  for ( int i=1; i <x ;i++ )
  {
    if ( s & m )
    {
      r++;
    }
    m <<= 1;
  }
  return r;
}


int _tmain(int argc, _TCHAR* argv[])
{
  int T, N;
  FILE *fIn,*fOut;
  int i,s,r,m,x,n,q;

  if ( argc != 3 ) return -1;
  fIn = fopen( argv[1], "rt" );
  fOut = fopen( argv[2], "wt" );

  fscanf( fIn, "%d", &T );

  for ( int t=0; t < T; t++ )
  {
    fscanf( fIn, "%d", &N );
    n=1;
    for ( s=1; s<(1 << (N-2)); s++)
    {
      x = N;
      while ( ( x = GetRank(s | (1 << (N-2)),x) ) > 1 );
      if ( x == 1 )
      {
        n++;
      }
      else
      {
        q=0;
      }
    }
    fprintf( fOut, "Case #%d: %d\n", t+1, n % 100003 );
  }

  fclose( fIn );
  fclose( fOut );

	return 0;
}

