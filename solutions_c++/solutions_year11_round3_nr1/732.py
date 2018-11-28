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
      size_t R, C;
      std::cin >> R >> C;

      std::vector<int> tiles(R * C, 0);
      for (size_t l = 0; l != R * C; ++l)
      {
         char c;
         std::cin >> c;
         if (c == '.')
            continue;

         tiles[l] = 1;
      }

      while (replace(tiles, C));

      char ar[2] = { '/', '\\' };

      std::cout << "Case #" << tc + 1 << ":";
      if (std::find(tiles.begin(), tiles.end(), 1) != tiles.end())
         std::cout << std::endl << "Impossible" << std::endl;
      else
      {
         for (size_t l = 0; l != tiles.size(); ++l)
         {
            if (l % C == 0)
               std::cout << std::endl;

            if (tiles[l] == 0)
               std::cout << '.';
            else
               std::cout << ar[tiles[l] - 2];
         }

         std::cout << std::endl;
      }
   }
}