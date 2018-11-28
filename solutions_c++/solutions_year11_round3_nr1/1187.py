

#include <tchar.h>
#include <fstream>
#include <iostream>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
  int T, R, C;
  FILE *fIn,*fOut;
  char aTiles[50*50];
  char line[50];
  bool bFailure;

  if ( argc != 3 ) return -1;
  fIn = fopen( argv[1], "rt" );
  fOut = fopen( argv[2], "wt" );

  fscanf( fIn, "%d", &T );

  for ( int t=0; t < T; t++ )
  {
    fscanf( fIn, "%d %d\n", &R, &C );
    for ( int r=0; r < R; r++ ) {
      for ( int c=0; c < C; c++ ) {
        fscanf( fIn, "%c", aTiles + (r*C+c) );
      }
      fscanf( fIn, "\n" );
    }
    bFailure = false;
    for ( int r=0; r < R; r++ ) {
      for ( int c=0; c < C; c++ ) {
        if ( aTiles[r*C+c] == '#' )
        {
          if ( r == R-1 || c == C-1 ) {
            bFailure = true;
            break;
          }
          if ( aTiles[r*C+c+1] != '#' || aTiles[(r+1)*C+c] != '#' || aTiles[(r+1)*C+c+1] != '#' ) {
            bFailure = true;
            break;
          }
          aTiles[r*C+c] = '/';
          aTiles[r*C+c+1] = '\\';
          aTiles[(r+1)*C+c] = '\\';
          aTiles[(r+1)*C+c+1] = '/';
        }
      }
      if ( bFailure ) break;
    }
    if ( bFailure ) {
      fprintf( fOut, "Case #%d:\nImpossible\n", t+1 );
    }
    else {
      fprintf( fOut, "Case #%d:\n", t+1 );
      for ( int r=0; r < R; r++ ) {
        for ( int c=0; c < C; c++ ) {
          fprintf( fOut, "%c", aTiles[r*C+c] );
        }
        fprintf( fOut, "\n" );
      }
    }
  }

  fclose( fIn );
  fclose( fOut );

	return 0;
}


