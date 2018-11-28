#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <assert.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <functional>

using namespace std;

#define DEBUG false

#if !DEBUG
   #define cout fout
#endif

int main() {
	ofstream fout( "large-input.out" );
	ifstream fin( "large-input.in" );

	assert( fout != NULL );
	assert( fin != NULL );

   int numCases;
   fin >> numCases;

   for( int i = 0; i < numCases; i++ )
   {
      int numCandies;
      fin >> numCandies;

      int xorSum = 0, totalSum = 0;
      int minimumValue = 100000000;

      for( int j = 0; j < numCandies; j++ )
      {
         int candyValue;
         fin >> candyValue;

         xorSum ^= candyValue;
         minimumValue = min( minimumValue, candyValue );

         totalSum += candyValue;
      }

      cout << "Case #" << i + 1 << ": ";
      if( xorSum == 0 )
         cout << ( totalSum - minimumValue );
      else
         cout << "NO";
      cout << '\n';
   }

	return 0;
}

