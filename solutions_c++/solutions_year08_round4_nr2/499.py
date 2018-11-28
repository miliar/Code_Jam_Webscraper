#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <list>
#include <queue>
#include <set>
#include <map>

using namespace std;

typedef long long ll ;

int NBTEST ;

int x1,x2,y1,y2 ;
int N,M,A ;
bool found ;

void eval()
{
  for( x1 = 0 ; x1 <= N ; x1 ++ )
    for( y1 = 0 ; y1 <= M ; y1 ++ )
      for( x2 = 0 ; x2 <= N  ; x2 ++ )
        for( y2 = 0 ; y2 <= M ; y2 ++ )
          {
            if( abs( x1*y2 - x2*y1 ) == A )
              {
                found = true;
                return ;
              }
          }
  
}


int main()
{
  cin >> NBTEST ;
  for( int TEST = 0 ; TEST < NBTEST ; TEST ++ )
    {
      ll result = 0 ;
      
      found = false ;
      cin >> N >> M >> A ;
      
      eval() ;
      
      cout << "Case #" << (TEST+1) << ": " ;
      if( found )
        cout << 0 << " " << 0 << " " << x1 << " "<<y1 << " " << x2 << " " << y2  << endl ;
      else
        cout << "IMPOSSIBLE" << endl; 
    }
}
