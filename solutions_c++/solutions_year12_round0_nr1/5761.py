// {{{ Boilerplate Code <--------------------------------------------------

#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

#define   FOR(i, a, b)    for ( typeof(a) i = (a) ; i < (b) ; ++i )
#define   REP(i, n)       FOR(i, 0, n)
#define   ALL(a)          (a).begin(), (a).end()

using namespace std;

typedef pair< int, int >  ii;
typedef long long         ll;

// }}}

char CODE['z'-'a'+1] = {
  'y',  
  'h', 
  'e',
  's',
  'o',
  'c',
  'v',
  'x',
  'd',
  'u',
  'i',
  'g',
  'l',
  'b',
  'k',
  'r',
  'z',
  't',
  'n',
  'w',
  'j',
  'p',
  'f',
  'm',
  'a',
  'q'
};

int main()
{
  int T, c;
  char G[101], S[101];

  scanf("%d\n", &T);

  REP(t, T)
  {
  
    gets(G);

    printf("Case #%d: ", t+1);
    
    c = 0;
    while ( G[c] != '\0' )
    {
      if ( G[c] != ' ' )
	S[c] = CODE[G[c] - 'a'];
      else
	S[c] = ' ';
      c++;
    }
    S[c] = '\0';

    puts(S);

  }

  return 0;
}
