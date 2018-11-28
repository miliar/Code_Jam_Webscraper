
#include <tchar.h>
#include <fstream>
#include <iostream>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
  int T;
  FILE *fIn,*fOut;
  int N;
  char c;
  int iButton;
  int aButton[200];
  char aRobot[200];
  int iRobO, iRobB, iTRobO, iTRobB;
  bool bAdvance;

  if ( argc != 3 ) return -1;
  fIn = fopen( argv[1], "rt" );
  fOut = fopen( argv[2], "wt" );

  fscanf( fIn, "%d", &T );

  for ( int t=0; t < T; t++ )
  {
    fscanf( fIn, "%d ", &N );
    for ( int i=0; i < N; i++ )
    {
      fscanf( fIn, "%c %d ", aRobot+i, aButton+i );
    }
    iRobO = iRobB = 1;
    int s;
    int iSeq = 0;
    for ( s = 0; iSeq < N; s++ )
    {
      bAdvance = false;
      for ( int i=iSeq; i < N; i++ )
      {
        if ( aRobot[i] == 'O' ) 
        {
          iTRobO = aButton[i];
          break;
        }
      }
      for ( int i=iSeq; i < N; i++ )
      {
        if ( aRobot[i] == 'B' ) 
        {
          iTRobB = aButton[i];
          break;
        }
      }
      if ( iTRobO < iRobO ) 
      {  
        iRobO--;
      }
      else
      {
        if ( iTRobO > iRobO ) 
        {
          iRobO++;
        }
        else
        {
          if ( aRobot[iSeq] == 'O' )
          {
            bAdvance = true;
          }
        }
      }

      if ( iTRobB < iRobB ) 
      {  
        iRobB--;
      }
      else
      {
        if ( iTRobB > iRobB ) 
        {
          iRobB++;
        }
        else
        {
          if ( aRobot[iSeq] == 'B' )
          {
            bAdvance = true;
          }
        }
      }
      if ( bAdvance ) iSeq++;
    }

    fprintf( fOut, "Case #%d: %d\n", t+1, s );
  }

  fclose( fIn );
  fclose( fOut );

	return 0;
}

