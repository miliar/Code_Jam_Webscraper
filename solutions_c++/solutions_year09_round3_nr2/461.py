
#include <tchar.h>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <math.h>


using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
  int T, N;
  ifstream input;
  ofstream output;
  char c;
  long long res;
  int i;
  __int64 X,Y,Z,Vx,Vy,Vz;
  typedef double A[500];
  A aX,aY,aZ,aVx,aVy,aVz;
  int x;
  double time,distance,d;


  // initialize
  if ( argc != 3 ) return -1;
  input.open( argv[1] );
  if ( !input ) return -1;
  output.open( argv[2] );

  input >> T;

  for ( int t=0; t < T; t++ )
  {
    input >> N;
    X=Y=Z=Vx=Vy=Vz =0;
    for ( int i=0; i < N; i++ )
    {
      input >> x; X += x;  aX[i] = x;
      input >> x; Y += x;  aY[i] = x;
      input >> x; Z += x;  aZ[i] = x;
      input >> x; Vx += x; aVx[i] = x;
      input >> x; Vy += x; aVy[i] = x;
      input >> x; Vz += x; aVz[i] = x;
    }
    if ( Vx*X + Vy*Y + Vz*Z == 0 )
    { 
      time =0;
    }
    else
    {
      time = -((double)(Vx*X + Vy*Y + Vz*Z))/((double)(Vx*Vx + Vy*Vy + Vz*Vz));
    }
    if ( time < 0 ) time = 0;
    distance = 0;
    d = 0 ;
    for ( int i=0; i < N; i++ )
    {
      d += aX[i]+time*aVx[i];
    }
    distance += ( d / (double)N ) * ( d / (double)N );
    d = 0 ;
    for ( int i=0; i < N; i++ )
    {
      d += aY[i]+time*aVy[i];
    }
    distance += ( d / (double)N ) * ( d / (double)N );
    d = 0 ;
    for ( int i=0; i < N; i++ )
    {
      d += aZ[i]+time*aVz[i];
    }
    distance += ( d / (double)N ) * ( d / (double)N );
    distance = sqrt( distance );
   
    output << "Case #" << t+1 << ": " << setprecision( 10 ) << distance << " " << time << endl;  
  }
  input.close();
  output.close();

	return 0;
}

