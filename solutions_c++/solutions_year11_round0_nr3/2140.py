#include <list>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <string>
#include <math.h>

int main()
{
   size_t T = 0;
   std::cin >> T;

   for (size_t tc = 1; tc != T + 1; ++tc)
   {
      size_t N = 0;
      std::cin >> N;

      std::vector<size_t> piles(N);
      for (size_t l = 0; l != N; ++l)
         std::cin >> piles[l];

      size_t sum = 0;
      for (size_t l = 0; l != N; ++l)
         sum ^= piles[l];

      if (sum != 0)
         std::cout << "Case #" << tc << ": NO" << std::endl;
      else
      {
         __int64 res = 0;
         size_t mn = -1;
         for (size_t l = 0; l != N; ++l)
         {
            if (piles[l] < mn)
               mn = piles[l];

            res += piles[l];
         }

         res -= mn;

         std::cout << "Case #" << tc << ": " << res << std::endl;
      }
   }

   return 0;
}

