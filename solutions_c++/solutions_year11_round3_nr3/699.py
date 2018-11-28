#include <list>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <string>
#include <math.h>
#include <algorithm>
#include <limits>

bool replace(std::vector<int> & tiles, size_t c)
{
   std::vector<int>::iterator it = std::find(tiles.begin(), tiles.end(), 1);

   if (it == tiles.end())
      return false;

   size_t t = it - tiles.begin();
   size_t x = t % c;
   size_t y = t / c;
   size_t rows = tiles.size() / c;

   if (x == c - 1 || y == rows - 1)
      return false;

   int r = x + 1 + y * c;
   int b = x + (y + 1)* c;
   int br = x + 1 + (y + 1) * c;
   
   if (tiles[r] == 1 && tiles[b] == 1 && tiles[br] == 1)
   {
      tiles[t] = 2;
      tiles[br] = 2;
      tiles[r] = 3;
      tiles[b] = 3;
      return true;
   }
   else
      return false;
}

int main()
{
   size_t T;
   std::cin >> T;

   for (size_t tc = 0; tc != T; ++tc)
   {
      size_t N, L, H;
      std::cin >> N >> L >> H;

      std::vector<size_t> freqs(N);
      for (size_t l = 0; l != N; ++l)
         std::cin >> freqs[l];

      std::vector<char> pos(H - L + 1, 1);
      for (size_t l = 0; l != N; ++l)
      {
         for (size_t k = 0; k != pos.size(); ++k)
         {
            size_t f = k + L;

            if (f < freqs[l])
               pos[k] &= (freqs[l] % f == 0);
            else
               pos[k] &= (f % freqs[l] == 0);
         }
      }

      std::vector<char>::iterator it = std::find(pos.begin(), pos.end(), 1);
      if (it == pos.end())
         std::cout << "Case #" << tc + 1 << ": NO" << std::endl;
      else
         std::cout << "Case #" << tc + 1 << ": " << (it - pos.begin()) + L << std::endl;
   }
}