
#include <tchar.h>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>

using namespace std;


int iInterSect( int a1, int b1, int a2, int b2 )
{
  if ( (a1-a2)*(b1-b2) < 0 ) 
  {
    return 1;
  }
  return 0;
}

int _tmain(int argc, _TCHAR* argv[])
{
  int T,N;
  FILE *fIn,*fOut;
  int i,j,n;
  int a[1000],b[1000];

  if ( argc != 3 ) return -1;
  fIn = fopen( argv[1], "rt" );
  fOut = fopen( argv[2], "wt" );

  fscanf( fIn, "%d", &T );

  for ( int t=1; t <= T; t++ )
  {
    n =0;
    fscanf( fIn, "%d", &N );
    for ( i=0; i<N; i++ )
    {
      fscanf( fIn, "%d %d", a+i, b+i );
    }
    for ( i=1; i<N; i++ )
    {
      for ( j=0; j<i; j++ )
      {
        n += iInterSect( a[i], b[i], a[j], b[j] );
        
      }
    }
    fprintf( fOut, "Case #%d: %d\n", t, n);
  }

  fclose( fIn );
  fclose( fOut );

	return 0;
}

