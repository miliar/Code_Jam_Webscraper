#include <cstdio>
#include <algorithm>
using namespace std;

int N, S, p, t[ 100 + 1 ];

int diff2[][2] = { { 3, 0 }, { 2, 1 }, { 1, 2 } };
int diff3[][3] = { { 2, 0, 1 }, { 1, 0, 2 }, { 1, 1, 1 } };


int solve( int v )
{
  for(int pi=p; pi<=v/3+1; pi++)
    for(int j=0; j<3; j++)
      if( diff2[ j ][ 0 ] * pi + diff2[ j ][ 1 ] * ( pi - 1 ) == v )
        return 1;
  
  if( S == 0 )
    return 0;
  
  for(int pi=max(p,2); pi<=v/3+2; pi++)
    for(int j=0; j<3; j++)
      if( diff3[ j ][ 0 ] * pi + diff3[ j ][ 1 ] * ( pi - 1 ) + diff3[ j ][ 2 ] * ( pi - 2 ) == v )
      {
        S--;
        return 1;
      }
  
  return 0;
}


int main()
{
  int ilz;
  scanf("%i", &ilz);
  for(int xz=1; xz<=ilz; xz++)
  {
    scanf("%i%i%i", &N, &S, &p);
    int ans = 0;
    for(int i=0; i<N; i++)
    {
      scanf("%i", &t[i]);
      ans += solve( t[i] );
    }
    printf("Case #%i: %i\n", xz, ans);
  }
  return 0;
}

