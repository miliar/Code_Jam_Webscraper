#include <cmath>
#include <set>
#include <iostream>

int solve(int a, int b)
{
   const int d = floor(std::log10(a));
   const int power = std::pow(10., d);
   std::set<std::pair<int, int> > m;
   for(int i = a; i <= b; i++)
   {
      int v = i;
      for(int c = 0; c < d; c++)
      {
         const int f = v % 10;
         v = f * power + v / 10;
         if (f == 0 || v > b)
            continue;
         if(v > i)
            m.insert(std::make_pair(i, v));
      }
   }
   return m.size();
}


int main()
{
   int n;
   std::cin >> n;
   for(int i = 0; i < n; i++)
   {
      int a, b;
      std::cin >> a >> b;
      std::cout << "Case #" << i + 1 << ": " << solve(a, b) << std::endl;
   }
   return 0;
}
