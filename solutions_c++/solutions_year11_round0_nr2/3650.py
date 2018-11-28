
#include <tchar.h>
#include <fstream>
#include <iostream>

using namespace std;

char bCombine[26*26];
bool bOppose[26*26];

int Index( char a, char b )
{
  return (a-'A')*26 + (b-'A');
}


int _tmain(int argc, _TCHAR* argv[])
{
  int T;
  FILE *fIn,*fOut;
  int C, D, N;
//  char acIn[200];
  char acList[200];
  char c,c1,c2,c3;

  if ( argc != 3 ) return -1;
  fIn = fopen( argv[1], "rt" );
  fOut = fopen( argv[2], "wt" );

  fscanf( fIn, "%d", &T );

  for ( int t=0; t < T; t++ )
  {
    for ( int i=0; i<26*26; i++ )
    {
      bCombine[i] = 0;
      bOppose[i] = false;
    }
    fscanf( fIn, "%d ", &C );
    for ( int i=0; i < C; i++ )
    {
      fscanf( fIn, "%c%c%c ", &c1, &c2, &c3 );
      bCombine[Index(c1,c2)] = c3;
      bCombine[Index(c2,c1)] = c3;
    }
    fscanf( fIn, "%d ", &D );
    for ( int i=0; i < D; i++ )
    {
      fscanf( fIn, "%c%c ", &c1, &c2 );
      bOppose[Index(c1,c2)] = true;
      bOppose[Index(c2,c1)] = true;
    }
    fscanf( fIn, "%d ", &N );

    int iList=0;
    for ( int i=0; i < N; i++ )
    {
      fscanf( fIn, "%c", acList+iList );
      while ( iList && (c = bCombine[Index(acList[iList],acList[iList-1])]) )
      {
        acList[--iList] = c;
      }
      for ( int j=0; j < iList; j++ )
      {
        if ( bOppose[Index(acList[j],acList[iList])] )
        {
          iList = -1;
          break;
        }
      }
      iList++;
    }
    fprintf( fOut, "Case #%d: [", t+1 );
    for ( int i=0; i<iList; i++ )
    {
      if ( i ) fprintf( fOut, ", " );
      fprintf( fOut, "%c", acList[i] );
    }
    fprintf( fOut, "]\n" );
  }

  fclose( fIn );
  fclose( fOut );

	return 0;
}

