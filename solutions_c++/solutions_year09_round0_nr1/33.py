#include <cstdio>
#include <string>
#include <vector>

using namespace std;

struct node {
   node *p[26];

   node() { memset( p, 0, sizeof p ); }
} nodes[75000], *alloc = nodes;

int L, D, N;
char buff[10000];

vector<int> links[16];

int rec( node *t, int i ) {
   if( !t ) return 0;
   if( i == L ) return 1;
   
   int ret = 0;
   for( vector<int>::iterator it = links[i].begin(); it != links[i].end(); ++it ) 
      ret += rec( t->p[*it], i+1 );
   return ret;
}

int main( void ) {
   scanf( "%d%d%d", &L, &D, &N );
   
   node *root = alloc++;

   for( int i = 0; i < D; ++i ) {
      scanf( "%s", buff );
      
      node *t = root;
      for( int j = 0; j < L; ++j ) {
         int x = buff[j]-'a';
         if( !t->p[x] ) t->p[x] = alloc++;
         t = t->p[x];
      }
   }

   for( int i = 0; i < N; ++i ) {
      scanf( "%s", buff );

      char *p = buff;
      for( int j = 0; j < L; ++j ) {
         links[j].clear();
         if( islower( *p ) ) 
            links[j].push_back( *p-'a' );
         else 
            for( ++p; *p != ')'; ++p )
               links[j].push_back( *p-'a' );
         ++p;
      }

      printf( "Case #%d: %d\n", i+1, rec( root, 0 ) );
   }
   
   return 0;
}
