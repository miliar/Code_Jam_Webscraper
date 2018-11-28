#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <fstream>

#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <utility>
#include <functional>

#include <cmath>
#include <cstring>
#include <ctime>
using namespace std;
const int NULA = 0;
const int MAXK = 5002;

struct node {
  int item;
  node *next, *prev;
  
  node( int Item = -1, node *Next = 0, node *Prev = 0 ) : item( Item ), next( Next ), prev( Prev ) {}
};
typedef node* link;

int T, K, n;
int d[ MAXK ];
int sol[ MAXK ];
link x = new node;

void remove_node( link &x, int i ) {
  sol[ x->item ] = i;
  static link next, prev;
  
  next = x->next;
  prev = x->prev;
  
  next->prev = prev;
  prev->next = next;
  delete x;
  x = next;
}

int main( void ) {
  scanf ( "%d", &T );
  double start;
  for( int t = 0; t < T; ++t ) {
    start = clock();
    printf( "Case #%d: ", t+1 );
    
    scanf( "%d%d", &K, &n );
    for( int i = 0; i < n; ++i ) 
      scanf( "%d", d + i );
    
    memset( sol, -1, sizeof( sol ) );

    node head( 1, 0, 0 );
    x = &head;
    x->item = 1;

    for( int i = 2; i <= K; ++i )
      x = ( x->next = new node( i, &head, x ) );
    head.prev = x;
    x = &head;

    int cnt, j;
    for( int i = 1; i <= K; ++i ) {
      j = i;
      for( cnt = 1; cnt < j; ++cnt )
        x = x->next;
      //      printf( "ubijam %d na %d mjestu\n", i, x->item );
      remove_node( x, i );
    }

    for( int i = 0; i < n; ++i )
      printf( "%d%c", sol[ d[ i ] ], i + 1 == n ? '\n' : ' ' );
    //    fprintf( stderr, "time: %.3lf (total: %.3lf)\n", ( clock() - start ) / CLK_TCK, clock() / (double)CLK_TCK );
  }
  
  return NULA;
}
