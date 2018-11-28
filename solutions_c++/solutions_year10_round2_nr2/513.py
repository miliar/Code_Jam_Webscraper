#include <iostream>
#include <vector>
#include <gmpxx.h>

typedef long long ll;

struct Chi
{
   ll x, v;
};

int main ()
{
   int C;
   std::cin >> C;
   for (int c = 1; c <= C; ++c)
   {
      ll N, K, B, T;
      std::cin >> N >> K >> B >> T;
      std::vector <Chi> chi (N);

      for (int i = 0; i < N; ++i)
         std::cin >> chi [i].x;

      for (int i = 0; i < N; ++i)
         std::cin >> chi [i].v;

      int good = 0, swaps = 0; 
      for (int i = 0; ; ++i)
      {
         if (good == K)
         {
            std::cout << "Case #" << c << ": " << swaps << std::endl;
            break;
         }

         if (i == N)
         {
            std::cout << "Case #" << c << ": " << "IMPOSSIBLE" << std::endl;
            break;
         }

         Chi &ch = chi [N - i - 1];
         if ((B - ch.x) <= ch.v * T)
         {
            swaps += i - good;
            ++good;
         }
      }
   }
}
