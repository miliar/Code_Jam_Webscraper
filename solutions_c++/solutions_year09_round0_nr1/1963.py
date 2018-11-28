#include <cstring>
#include <cstdio>
#include <set>

#define maxl 16
#define maxd 5000

using namespace std;

int l, d, n;

char rijeci[maxd][maxl];
int moze[maxd];

void load() {
   scanf( "%d%d%d", &l, &d, &n );
   for( int i = 0; i < d; ++i ) scanf( "%s\n", rijeci[i] );
}

int solve() {
   set< char > S;
   char ln[1000];
   int p = 0;   
   memset( moze, 0, sizeof moze );
   fgets( ln, 1000, stdin );
   
   for( int i = 0; i < l; ++i ) {
      S.clear();      

      if( ln[p] == '(' ) {
         for( ++p; ln[p] != ')'; ) S.insert( ln[p++] );
         ++p;
      } else S.insert( ln[p++] );

      for( int j = 0; j < d; ++j )
         if( !S.count( rijeci[j][i] ) ) moze[j] = 1;
   }
   
   int ret = 0;
   for( int i = 0; i < d; ++i ) ret += (moze[i] == 0);
   return ret;
}

int main(void) {
   load();
   for( int i = 0; i < n; ++i ) printf( "Case #%d: %d\n", i+1, solve() );
   return 0;
}
