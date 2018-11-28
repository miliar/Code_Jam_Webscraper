

#include <tchar.h>
#include <fstream>
#include <iostream>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
  int T, N, L, H;
  FILE *fIn,*fOut;
  int aNotes[10000];
  bool bSuccess;
  int i,f;

  if ( argc != 3 ) return -1;
  fIn = fopen( argv[1], "rt" );
  fOut = fopen( argv[2], "wt" );

  fscanf( fIn, "%d", &T );

  for ( int t=0; t < T; t++ )
  {
    fscanf( fIn, "%d %d %d", &N, &L, &H );
    for ( i=0; i < N; i++ )
    {
      fscanf( fIn, "%d ", aNotes+i );
    }
    bSuccess = false;
    for ( f=L; f <=H; f++ )
    {
      for ( i=0; i<N; i++ )
      {
        if ( f % aNotes[i] != 0 && aNotes[i] % f != 0 ) break;
      }
      if ( i == N ) 
      {
        bSuccess = true;
        break;
      }
    }
    if ( bSuccess )
    {
      fprintf( fOut, "Case #%d: %d\n", t+1, f );  
    }
    else
    {
      fprintf( fOut, "Case #%d: NO\n", t+1 );
    }
  }

  fclose( fIn );
  fclose( fOut );

	return 0;
}


