#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
   int t;
   cin >> t;
   for(int i = 0; i < t; i++)
   {
      unsigned long long n,l,h;
      cin >> n >> l >> h;
      std::vector< unsigned long long > others;
      for(int j = 0; j < n; j++)
      {
         unsigned long long x;
         cin >> x;
         others.push_back(x);
      }
      
      unsigned long long answer = 0;
      for(unsigned long long j = l; j <= h; j++)
      {
         bool good = true;
         for(size_t k = 0; k < others.size(); k++)
         {
            good &= j % others[k] == 0 || others[k] % j == 0; 
         }
         if(good)
         {
            answer = j;
            break;
         }
      }
      if(answer == 0)
      std::cout << "Case #" << i+1 << ": " << "NO" << std::endl;
      else
         std::cout << "Case #" << i+1 << ": " << answer << std::endl;
   }
}