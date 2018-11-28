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
int MAXCOST = 200000 ;

struct tree
{
  int isAnd ;
  int isChange ;
  int cost[2] ;
};

tree nodes[12000] ;

void propage( int n, int LEAF )
{
  //cout << n << " " << LEAF << endl   ;
  if( n > LEAF )
    return ;
  
  propage( 2*n, LEAF ) ;
  propage( 2*n+1, LEAF );

  int addCost ;
  if( nodes[n].isChange )
    addCost = 1 ;
  else
    addCost = MAXCOST ;

  for( int op = 0 ; op <= 1 ; op ++ )
    {
      for( int r1 = 0 ; r1 <= 1 ; r1 ++ )
        for( int r2 = 0 ; r2 <= 1 ; r2 ++ )
          {
            int result ;
            if( op == 1 )
              result = r1*r2 ;
            else
              result = max( r1,r2 );
            int initPrice = nodes[2*n].cost[r1] + nodes[2*n+1].cost[r2] ;
            int finalPrice = initPrice + addCost*( op != nodes[n].isAnd ) ;
            
            //cout << n << " " << r1 << " " << r2 << " " << finalPrice << endl;
            
            nodes[n].cost[result] = min( nodes[n].cost[result], finalPrice  ) ; 

          }
      
    }
  
}

int main()
{
  cin >> NBTEST ;
  for( int TEST = 0 ; TEST < NBTEST ; TEST ++ )
    {
      int M ,V ;
      cin >> M >> V ;
      for( int n = 1 ; n <= (M-1)/2 ; n ++ )
        {
          int G,C ;
          cin >> G >> C ;
          nodes[n].isAnd = G ;
          nodes[n].isChange = C ;
          nodes[n].cost[0] = MAXCOST ;
          nodes[n].cost[1] = MAXCOST ;
        }

      for( int n = (M-1)/2 +1 ; n <= M ; n ++ )
        {
          int I ;
          cin >> I ;
          nodes[n].cost[I] = 0 ;
          nodes[n].cost[1-I] = MAXCOST ;
        }
      
      propage( 1 , (M-1)/2 );
      
      
      cout << "Case #" << (TEST+1) << ": " ;
      if( nodes[1].cost[V] == MAXCOST ) 
        cout << "IMPOSSIBLE" << endl ;
      else
        cout << nodes[1].cost[V] << endl ;
          
    }
}
