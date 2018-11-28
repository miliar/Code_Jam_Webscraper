#include <list>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <string>
#include <math.h>
#include <algorithm>
#include <limits>

typedef unsigned __int64 uint64_t;

int main()
{
   size_t T;
   std::cin >> T;

   for (size_t tc = 0; tc != T; ++tc)
   {
      uint64_t L, t, N, C;
      std::cin >> L >> t >> N >> C;

      std::vector<uint64_t> dists(C);
      for (uint64_t l = 0; l != C; ++l)
         std::cin >> dists[l];

      std::vector<uint64_t> distances(N + 1, 0);
      for (size_t l = 1; l != N + 1; ++l)
         distances[l] = distances[l - 1] + dists[(l - 1) % C];

      if (L == 0)
      {
         std::cout << "Case #" << tc + 1 << ": " << distances[N] * 2;
      }
      else if (L == 1)
      {
         uint64_t max_time = 0;
         for (size_t l = 0; l != N; ++l)
         {
            // set boost here
            uint64_t time = distances[l] * 2;
            if (time > t)
               max_time = std::max(dists[l % C], max_time);
            else if (time + dists[l % C] * 2 > t)
               max_time = std::max(dists[l % C] - ((t - time) / 2), max_time);
         }

         std::cout << "Case #" << tc + 1 << ": " << distances[N] * 2 - max_time;
      }
      else if (L == 2)
      {
         uint64_t max_time = 0;
         for (size_t l = 0; l + 1 < N; ++l)
         {
            for (size_t k = l + 1; k < N; ++k)
            {
               uint64_t time1 = distances[l] * 2;
               if (time1 > t)
               {
                  max_time = std::max(dists[l % C] + dists[k % C], max_time);
               }
               else if (time1 + dists[l % C] * 2 > t)
               {
                  max_time = std::max(dists[l % C] - ((t - time1) / 2) + dists[k % C], max_time);
               }
               else
               {
                  uint64_t time2 = distances[k] * 2;
                  if (time2 > t)
                     max_time = std::max(dists[k % C], max_time);
                  else if (time2 + dists[k % C] * 2 > t)
                     max_time = std::max(dists[k % C] - ((t - time2) / 2), max_time);
               }
            }
         }

         std::cout << "Case #" << tc + 1 << ": " << distances[N] * 2 - max_time;
      }

      std::cout << std::endl;
   }
}