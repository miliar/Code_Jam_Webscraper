
#include <tchar.h>
#include <fstream>
#include <iostream>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
  int T;
  ifstream input;
  ofstream output;
  char szLine[200];

  const char aExInp[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi_rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd_de kr kd eoya kw aej tysr re ujdr lkgc jvqz";
  const char aExOut[] = "our language is impossible to understand_there are twenty six factorial possibilities_so it is okay if you want to just give upzq";
  char aMapping[256];

  // initialize
  for ( int i='a'; i<='z'; i++ ) aMapping[i] = toupper(i);
  for ( int i=0; i < sizeof(aExInp); i++ ) aMapping[aExInp[i]] = aExOut[i];
//  for ( int i='a'; i<='z'; i++ ) printf("%c", aMapping[i] );


  if ( argc != 3 ) return -1;
  input.open( argv[1] );
  if ( !input ) return -1;
  output.open( argv[2] );
  input >> T;
  input.getline( szLine, 200, '\n' );

  for ( int t=0; t < T; t++ )
  {
    input.getline( szLine, 200, '\n' );
    for ( int i=0, n=strlen(szLine); i < n; i++ )
    {
      szLine[i] = aMapping[szLine[i]];
    }
    output << "Case #" << t+1 << ": " << szLine << endl;  
  }
  input.close();
  output.close();

  return 0;
}

