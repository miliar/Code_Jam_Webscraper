
#include <tchar.h>
#include <fstream>
#include <iostream>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
  int T;
  ifstream input;
  ofstream output;
  string s;
  unsigned int n,k;

  // initialize
  if ( argc != 3 ) return -1;
  input.open( argv[1] );
  if ( !input ) return -1;
  output.open( argv[2] );
  input >> T;

  for ( int t=0; t < T; t++ )
  {
    input >> n;
    input >> k;

    s = (k & ((1 << n) -1 )) == ((1 << n) -1) ? "ON" : "OFF";
    output << "Case #" << t+1 << ": " << s.c_str() << endl;  
  }
  input.close();
  output.close();


	return 0;
}

