#include <cctype>
#include <cstdio>
#include <map>
#include <string>

using namespace std;

struct node {
   map<string, node *> dict;

   ~node() {
      for( map<string, node *>::iterator it = dict.begin(); it != dict.end(); ++it ) 
         delete it->second;
   }
};

char *p;

int add( node *x ) {
   int ret = 0;
   while( *p == '/' ) {
      ++p;
      string s;
      while( isalpha(*p) || isdigit(*p) ) s += *p++;

      if( !x->dict.count( s ) ) {
         x->dict[s] = new node();
         ++ret;
      }
      x = x->dict[s];
   }
   return ret;
}

int main( void ) {
   int T;
   scanf( "%d", &T );
   for( int tt = 1; tt <= T; ++tt ) {
      int n, m;
      scanf( "%d%d", &n, &m );
      static char line[100001];
      gets( line );
      
      node *root = new node();

      for( int i = 0; i < n; ++i ) {
         gets( line );
         p = line;
         add( root );
      }
      int ret = 0;
      for( int i = 0; i < m; ++i ) {
         gets( line );
         p = line;
         ret += add( root );
      }
      printf( "Case #%d: %d\n", tt, ret );

      delete root;
   }
   return 0;
}
