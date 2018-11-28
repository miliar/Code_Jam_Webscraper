
#include <tchar.h>
#include <fstream>
#include <iostream>
#include <iomanip>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
  const int MaxLineLength = 500;
  int N;
  unsigned int nLine, nCount;
  char szLine[MaxLineLength+1];
  const char szPhrase[] = "welcome to code jam";
  const int nPhrase = sizeof( szPhrase )-1;
  int aPhraseIndices[nPhrase];
  int iLine, iPhrase;
  bool bStop;

  ifstream input;
  ofstream output;

  // initialize
  if ( argc != 3 ) return -1;
  input.open( argv[1] );
  if ( !input ) return -1;
  output.open( argv[2] );
  input.getline( szLine, MaxLineLength+1 );
  N = atoi( szLine );

  // process lines
  for ( int i=0; i < N; i++ )
  {
    input.getline( szLine, MaxLineLength+1 );
    nLine = strlen( szLine );
    iLine = 0;
    iPhrase = 0;
    nCount = 0;
    bStop = false;

    while ( !bStop )
    {
      if ( szLine[iLine] == szPhrase[iPhrase] )
      {
        aPhraseIndices[iPhrase++] = iLine;
        if ( iPhrase == nPhrase ) 
        {
          nCount++;
          iPhrase--;
        }
      }
      iLine++;
      while ( iLine == nLine )
      {
        if ( !iPhrase ) 
        {
          bStop = true;
          break;
        }
        iLine = aPhraseIndices[--iPhrase]+1;
      }
    }
    output << "Case #" << i+1 << ": " << setfill('0') << setw(4) << ( nCount % 10000 ) << endl;  
  }

  input.close();
  output.close();

	return 0;
}

