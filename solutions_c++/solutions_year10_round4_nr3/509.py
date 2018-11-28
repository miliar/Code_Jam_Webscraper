#include <algorithm>
#include <cstdio>
#include <set>

using namespace std;

typedef pair<int,int> par;

int main( void ) {
   int T;
   scanf( "%d", &T );
   for( int tt = 1; tt <= T; ++tt ) {
      int R;
      scanf( "%d", &R );
      set<par> alive, olds, babies;
      for( int r = 0; r < R; ++r ) {
         int x1, y1, x2, y2;
         scanf( "%d%d%d%d", &x1, &y1, &x2, &y2 );
         for( int x = x1; x <= x2; ++x ) 
            for( int y = y1; y <= y2; ++y ) 
               babies.insert( par(x,y) );
      }
               
      int ret = 0;
      for( ; alive.size() || babies.size(); ++ret ) {
         for( set<par>::iterator it = babies.begin(); it != babies.end(); ++it ) 
            alive.insert( *it );
         for( set<par>::iterator it = olds.begin(); it != olds.end(); ++it ) 
            alive.erase( *it );      
   
         set<par> new_babies, new_olds;
         for( set<par>::iterator it = babies.begin(); it != babies.end(); ++it ) {
            par SW = par(it->first-1, it->second+1);
            par NE = par(it->first+1, it->second-1);
            par S = par(it->first, it->second+1);
            par E = par(it->first+1, it->second);
            par N = par(it->first, it->second-1);
            par W = par(it->first-1, it->second);
            if( alive.count(SW) && !alive.count(S) ) new_babies.insert( S );
            if( alive.count(NE) && !alive.count(E) ) new_babies.insert( E );
            if( !alive.count(N) && !alive.count(W) ) new_olds.insert(*it);
         }
         for( set<par>::iterator it = olds.begin(); it != olds.end(); ++it ) {
            par S = par(it->first, it->second+1);
            par E = par(it->first+1, it->second);               
            par SW = par(it->first-1, it->second+1);
            par NE = par(it->first+1, it->second-1);
            if( alive.count(S) && !alive.count(SW) ) new_olds.insert(S);
            if( alive.count(E) && !alive.count(NE) ) new_olds.insert(E);
         }
         
         babies.swap( new_babies );
         olds.swap( new_olds );
      }
      printf( "Case #%d: %d\n", tt, ret-1 );
   }
   return 0;
}
