#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <iterator>

int main(int argc, char* argv[])
{
   int numTestCases = 0;
   std::cin >> numTestCases;

   for ( int i = 0; i < numTestCases; ++i )
   {
      int numNumbers = 0;
      std::cin >> numNumbers;

      int sortedValues = 0;
      for ( int n = 0; n < numNumbers; n++ )
      {
         int goroNum = 0;
         std::cin >> goroNum;

         if ( goroNum == n + 1 )
         {
            ++sortedValues;
         }
      }

      std::cout << "Case #" << i + 1 << ": " << numNumbers - sortedValues << ".0000" << std::endl;
   }

	return 0;
}

