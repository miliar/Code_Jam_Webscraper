#include <cstdio>
#include <string>
#include <sstream>
#define MAXT 2000000
using namespace std;

typedef unsigned int uint;

int t[ MAXT + 1 ];


inline bool compare( string sN, int shift, string sB )
{
  int i, is = sN.size();
  for(i=0; i<is; i++)
  {
    int diff = sN[i] - sN[(i+shift)%is];
    if( diff > 0 )
      return false;
    if( diff < 0 )
      break;
  }
  if( i == is )
    return false;
  
  for(i=0; i<is; i++)
  {
    int diff = sB[i] - sN[(i+shift)%is];
    if( diff < 0 )
      return false;
    if( diff > 0 )
      break;
  }
  
  return true;
}


int main()
{
  int ilz;
  scanf("%i", &ilz);
  for(int xz=1; xz<=ilz; xz++)
  {
    int A, B;
    scanf("%i%i", &A, &B);
    
    int ans = 0;
    
    ostringstream ssB;
    ssB << B;
    string sB = ssB.str();
    
    for(int i=0; i<=MAXT; i++)
      t[ i ] = -1;
    
    for(int n=A; n<B; n++)
    {
      ostringstream ssN;
      ssN << n;
      string sN = ssN.str();
      for(uint i=1, is=sN.size(); i<is; i++)
        if( compare( sN, i, sB ) )
        {
          string s2 = sN.substr( i ) + sN.substr( 0, i );
          istringstream is( s2 );
          int i2;
          is >> i2;
          if( t[ i2 ] != n )
            ans++;
          t[ i2 ] = n;
        }
    }
    printf("Case #%i: %i\n", xz, ans);
  }
  return 0;
}

