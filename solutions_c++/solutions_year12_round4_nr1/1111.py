
#include <tchar.h>
#include <fstream>
#include <iostream>

using namespace std;

int len[10000],pos[10000],s[10000];
int T,N,D;

int _tmain(int argc, _TCHAR* argv[])
{
  ifstream input;
  ofstream output;

  if ( argc != 3 ) return -1;
  input.open( argv[1] );
  if ( !input ) return -1;
  output.open( argv[2] );
  input >> T;
  int x;

  for ( int t=1; t <= T; t++ ) 
  {
    input >> N;
    for ( int i=0; i < N; i++ )
    {
      input >> pos[i];
      input >> len[i];
      s[i]=0;
    }
    input >> D;

    for ( int i=N-1; i >= 0; i-- )
    {
      if ( D-pos[i] <= len[i] )
      {
        s[i] = D-pos[i];
      }
      for ( int j=i+1; j<N; j++ )
      {
        x = pos[j]-pos[i];
        if ( x > len[i] ) break;
        if ( s[j]>0 && s[j] <= x )
        {
          x = pos[j]-pos[i];
          if ( !s[i] ) 
          {
            s[i] = x;
          }
          else
          {
            if ( x < s[i] ) s[i] = x;
          }
        }
      }
    }

    if ( s[0] > 0 && pos[0] >= s[0] )
    {
      output << "Case #" << t << ": " << "YES" << endl;  
    }
    else
    {
      output << "Case #" << t << ": " << "NO" << endl;  
    }
  }
  input.close();
  output.close();

  return 0;
}

