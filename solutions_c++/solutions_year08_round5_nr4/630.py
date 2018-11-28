#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <set>
#include <cstdio>
#include <queue>
#include <list>

typedef unsigned long long ull ;
typedef long long ll ;


using namespace std ;

int NBTEST = 0 ;
int mapR[200][200] ;
int poss[200][200] ;

int H, W ;

int getNum(int x, int y)
{
  //cout << x << " " << y << endl ;

  if( x >= 0 && y >= 0 && x < W && y < H )
    {
      if( mapR[x][y] )
	{
	  if( x == W-1 && y == H-1 )
	    return 1 ;
	  
	  int & R = poss[x][y] ;
	  if( R != -1 )
	    return R ;

	  R = ( getNum( x+1,y+2) + getNum( x+2,y+1 ) ) % 10007 ;
	  
	  return R ;
	}
    }
  return 0 ;
}


int main()
{
  cin >> NBTEST ;
  for( int TEST = 0 ; TEST < NBTEST ; TEST ++ )
    {
      ll result = 0 ;

      for( int x = 0 ; x < 200 ; x ++ )
	for( int y = 0 ; y < 200 ; y ++ )
	  {
	    poss[x][y] = -1 ;
	    mapR[x][y] = 1 ;
	  }
      
      int R ;
      cin >> H >> W >> R ;
      for( int r = 0 ; r < R ; r ++ )
	{
	  int x,y;
	  cin >> y >> x ;
	  mapR[x-1][y-1] = 0 ;
	}
      
      result = getNum(0,0) ;
      
      cout << "Case #" << (TEST+1) << ": " << result << endl ;
    }
  
  return 0 ;
}
