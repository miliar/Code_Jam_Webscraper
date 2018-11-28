
#include <tchar.h>
#include <fstream>
#include <iostream>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
  int T,N,S,p;
  int ts,n,r,s;
  ifstream input;
  ofstream output;

  // initialize
  if ( argc != 3 ) return -1;
  input.open( argv[1] );
  if ( !input ) return -1;
  output.open( argv[2] );
  input >> T;

  for ( int t=0; t < T; t++ )
  {
    input >> N;
    input >> S;
    input >> p;
    n = 0;
    for ( int i=0; i < N; i++ )
    {
      input >> ts;
      s = (ts+2)/3;
      r = ts % 3;
      if ( r == 1 )
      {
        if ( s >= p ) n++;
      }
      else
      {
        if ( s >= p )
        {
          n++;
        }
        else
        {
          if ( s+1 == p && s > 1 && S )
          {
            n++;
            S--;
          }
        }
      }
    }
    output << "Case #" << t+1 << ": " << n << endl;  
  }
  input.close();
  output.close();

  return 0;
}

