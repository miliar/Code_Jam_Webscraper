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
#include <iterator>

using namespace std;

constexpr int kMaxHeight = 1000000000;

int main()
{
  unsigned nbCases;
  cin >> nbCases;
  for( unsigned noCase = 1 ; noCase <= nbCases ; noCase++ )
    {
      int nbPeaks;
      cin >> nbPeaks;
      vector< int > highestPeaks( nbPeaks - 1 );
      for( auto &p: highestPeaks )
        {
          cin >> p;
          p--;
        }

      vector< int > peakHigh( nbPeaks );

      peakHigh[ nbPeaks - 1 ] = kMaxHeight / 2;

      bool isPossible = true;
      for( int i = nbPeaks - 2 ; i >= 0 ; i-- )
        {
          int minH = 0;
          int maxH = kMaxHeight;

          for( int j = i + 1 ; j < nbPeaks ; j++ )
            {
              int h;
              if( j != highestPeaks[ i ] )
                h = ( peakHigh[ j ] - peakHigh[ highestPeaks[ i ] ] ) * ( i - highestPeaks[ i ] ) / ( j - highestPeaks[ i ] ) + peakHigh[ highestPeaks[ i ] ];
              if( j < highestPeaks[ i ] )
                minH = max( minH, h );
              else if( j > highestPeaks[ i ] )
                maxH = min( maxH, h );
            }

          if( minH >= maxH )
            {
              isPossible = false;
              break;
            }

          if( minH < kMaxHeight / 2 && maxH > kMaxHeight / 2 )
            peakHigh[ i ] = kMaxHeight / 2;
          else if( minH >= kMaxHeight / 2 )
            peakHigh[ i ] = minH + ( maxH - minH ) / 1000;
          else if( maxH <= kMaxHeight / 2 )
            peakHigh[ i ] = maxH - ( maxH - minH ) / 1000;
        }

      cout << "Case #" << noCase << ":";
      if( isPossible )
        for( auto &i: peakHigh )
          cout << " " << i;
      // copy( peakHigh.begin(), peakHigh.end(), ostream_iterator< unsigned >( cout, " " ) );
      else
        cout << " Impossible";
      cout << endl;
    }
  return EXIT_SUCCESS;
}
