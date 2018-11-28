
#include <tchar.h>
#include <fstream>
#include <iostream>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
  int T,A,B;
  int n,x,k=77,f,f2,u;
  int a[10],ia;
  ifstream input;
  ofstream output;
  bool bHaveAlready;

  // initialize
  if ( argc != 3 ) return -1;
  input.open( argv[1] );
  if ( !input ) return -1;
  output.open( argv[2] );
  input >> T;

  for ( int t=1; t <= T; t++ ) 
  {
    input >> A;
    input >> B;
    n = 0;
    if ( A > 9 )
    {
      u = 10;
      while ( u <= A ) u*=10;
      u /= 10;
      for ( k=A; k < B; k++ )
      {
        ia = 0;
        for ( f=10, f2=u; f<=u; )
        {
          x = k/f+f2*(k % f);
          if ( x > k && x <= B ) {
            bHaveAlready = false;
            for ( int i=0; i<ia; i++ )
            {
              if ( x == a[i] )
              {
                bHaveAlready = true;
                break;
              }
            }
            if ( !bHaveAlready )
            {
              n++;
              a[ia++] = x;
            }
          }
          f *= 10;
          f2 /= 10;
        }
      }
    }
    
    output << "Case #" << t << ": " << n << endl;  
  }
  input.close();
  output.close();

  return 0;
}

