#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <iterator>

int baby_add( long x, long y )
{
   return x ^ y;
}

int best_result_part2( std::vector<long> & candies )
{
   if ( std::accumulate( candies.begin(), candies.end(), 0, baby_add ) != 0 )
   {
      return 0;
   }

   std::sort( candies.begin(), candies.end() );

   return std::accumulate( candies.begin() + 1, candies.end(), 0 );
}

void DoTestCase( int caseNum )
{
   long result = 0;

   int numCandy = 0;
   std::cin >> numCandy;

   std::vector<long> candies;
   for ( int i = 0; i < numCandy; ++i )
   {
      int candyCount;
      std::cin >> candyCount;
      candies.push_back( candyCount );
   }

   result = best_result_part2( candies );

   std::cout << "Case #" << caseNum << ": ";

   if ( result == 0 )
   {
      std::cout << "NO" << std::endl;
   }
   else
   {
      std::cout << result << std::endl;
   }
}

int main(int argc, char* argv[])
{
   int numTestCases = 0;
   std::cin >> numTestCases;

   for ( int i = 0; i < numTestCases; ++i )
   {
      DoTestCase( i + 1 );
   }

   std::cin >> numTestCases;
	return 0;
}

