
#include <tchar.h>
#include <fstream>
#include <iostream>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
  int T;
  ifstream input;
  ofstream output;
  int aiChars[256];
  char c;
  long long res = 0;
  int i;
  int n;
  int nChars;
  int iSymbol;
  
  char ac[64];



  // initialize
  if ( argc != 3 ) return -1;
  input.open( argv[1] );
  if ( !input ) return -1;
  output.open( argv[2] );

  input >> T;
  input.getline( ac, 63 );

  for ( int t=0; t < T; t++ )
  {
    for ( int i=0; i<256; i++ ) {aiChars[i] =0;}
    input.getline( ac, 63 );
    n = strlen(ac);
    nChars =0;
    iSymbol = 1;
    res =0;
    for ( size_t i=0; i < n; i++ )
    {
      if ( !aiChars[ac[i]] ) nChars++;
      aiChars[ac[i]]--; 
    }
    if ( nChars == 1 ) nChars++;
    for ( size_t i=0; i < n; i++ )
    {
      if ( aiChars[ac[i]] < 0 ) 
      {
        aiChars[ac[i]] = iSymbol;
        switch (iSymbol)
        {
          case 0: iSymbol = 2; break;
          case 1: iSymbol = 0; break;
          default: iSymbol++;
        }
      }
    }
    for ( size_t i=0; i < n; i++ )
    {
      res *= nChars;
      res += aiChars[ac[i]];
    }

    output << "Case #" << t+1 << ": " << res << endl;  
  }
  input.close();
  output.close();


	return 0;
}

