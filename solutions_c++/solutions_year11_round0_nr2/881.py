#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <ctype.h>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

map<pair<char,char>,char> trans;
map<pair<char,char>,bool> forbid;
vector<char> r;
pair<char,char> p;
char a[500];

int main() {
  int T, ca;
  int N, i, C, j, k;

  scanf("%d\n", &T );
  for ( ca = 1; ca <= T; ca++ ) {
    trans.clear();
    forbid.clear();

    scanf("%d\n", &C );

    for ( i = 0; i < C; i++ ) {
      scanf("%s", a );

      trans[ make_pair( a[0], a[1] ) ] = a[2];
      trans[ make_pair( a[1], a[0] ) ] = a[2];
    }

    scanf("%d\n", &C );
    for ( i = 0; i < C; i++ ) {
      scanf("%s", a );
      
      forbid[ make_pair( a[0], a[1] ) ] = true;
      forbid[ make_pair( a[1], a[0] ) ] = true;
    }

    r.clear();
    scanf("%d %s\n", &C, a );
    for ( i = 0; i < C; i++ ) {
      if ( r.size() == 0 ) {
	r.push_back( a[i] );
	continue;
      }

      p = make_pair( a[i], r[r.size()-1] );
      /* Did it get transformed? */
      if ( trans.find( p ) != trans.end() ) {
	r.pop_back();
	r.push_back( trans[ p ] );
      }
      else {
	k = 0;
	for ( j = 0; j < r.size(); j++ ) {
	  if ( forbid.find( make_pair( r[j], a[i] ) ) != forbid.end() ) {
	    r.clear();
	    k = 1;
	    break;
	  }
	}

	if ( !k )
	  r.push_back( a[i] );
      }
    }

    printf("Case #%d: [", ca );
    for ( i = 0; i < r.size(); i++ ) {
      if ( i == 0 )
	printf("%c", r[i] );
      else
	printf(", %c", r[i] );
    }
    printf("]\n");
  }

  return 0;
}
