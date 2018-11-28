# /*
this_md5="$(md5sum < "$0" | cut -d' ' -f1)"
last_md5="$(readelf -p SOURCE_FILE_HASH "${0%.cpp}" 2>/dev/null | awk '/\[ *0\]/ { print $3 }')"
if [ "$this_md5" != "$last_md5" ]; then
g++ -pipe -Wall -Wextra -std=c++0x -g -march=native -O3 -DTHIS_MD5="\"$this_md5\"" -o "${0%.cpp}" "$0" ||
exit 1
fi
exec "${0%.cpp}" "$@"
exit 1
# */
#ifndef THIS_MD5
#  define THIS_MD5 "not set"
#endif
char MD5[] __attribute__((section ("SOURCE_FILE_HASH"))) = THIS_MD5;

#include <cstdlib>
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

struct Vine
{
  Vine( unsigned i_pos = 0, unsigned i_length = 0 )
    : pos( i_pos ), length( i_length )
  {}

  unsigned pos;
  unsigned length;
};

struct State
{
  State( unsigned i_noVine, unsigned i_length )
    : noVine( i_noVine ), length( i_length )
  {}

  unsigned noVine;
  unsigned length;
};

int main()
{
  unsigned nbCases;
  cin >> nbCases;
  for( unsigned noCase = 1 ; noCase <= nbCases ; noCase++ )
    {
      unsigned nbVines;
      cin >> nbVines;
      vector< Vine > vines( nbVines );
      for( auto &v: vines )
        cin >> v.pos >> v.length;
      unsigned dist;
      cin >> dist;

      stack< State > st;
      st.push( State( 0, vines[0].pos ) );

      bool isSuccess = false;
      while( !st.empty() )
        {
          State s = st.top();
          st.pop();

          if( vines[ s.noVine ].pos + s.length >= dist )
            {
              isSuccess = true;
              break;
            }

          for( unsigned i = s.noVine + 1 ;
               i < vines.size() && vines[i].pos <= vines[s.noVine].pos + s.length ;
               i++ )
                 st.push( State( i, min( vines[i].pos - vines[s.noVine].pos, vines[i].length ) ) );
        }

        cout << "Case #" << noCase << ": " << ( isSuccess ? "YES" : "NO" ) << endl;
    }
  return EXIT_SUCCESS;
}
