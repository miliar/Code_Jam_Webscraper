#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
   unsigned long long T;
   cin >> T;
   for(unsigned long long i = 0; i < T; i++)
   {
      unsigned long long l, n, t, c;
      cin >> l >> t >> n >> c;
      vector<unsigned long long> stars;
      for(unsigned long long j = 0; j < c; j++)
      {
         unsigned long long x;
         cin >> x;
         stars.push_back(x);
      }

      vector<unsigned long long> fullStars;
      for(unsigned long long j = 0; j < n; j++)
      {
         fullStars.push_back(stars[j%stars.size()]);
      }

      for(unsigned long long j = 0; j < fullStars.size(); j++)
      {
         fullStars[j] *= 2;
      }
      /*
      std::cout << fullStars.size() << std::endl;
      for(unsigned long long j = 0; j < fullStars.size(); j++)
      {
         std::cout << fullStars[j] << " ";
      }
      std::cout << std::endl;
      */
      vector<unsigned long long> gains;
      unsigned long long dist = 0;
      for(unsigned long long j = 0; j < fullStars.size(); j++)
      {
        // std::cout << dist << std::endl;
         if(dist >= t)
            gains.push_back( fullStars[j] / 2 );
         else if( fullStars[j] + dist >= t )
            gains.push_back(  (dist + fullStars[j] - t) / 2 );
         else
            gains.push_back(0);
         dist += fullStars[j];
         
      }
      /*
      for(unsigned long long j = 0; j < gains.size(); j++)
      {
         std::cout << gains[j] << " ";
      }
      std::cout << std::endl;
      */
      unsigned long long answer = 0;
      for(unsigned long long j = 0; j < fullStars.size(); j++)
      {
         answer += fullStars[j];
      }

      for(unsigned long long j = 0; j < l; j++)
      {
         unsigned long long max = 0;
         unsigned long long maxI = 0;
         for(unsigned long long k = 0; k < gains.size(); k++)
         {
            if( gains[k] > max )
            {
               max = gains[k];
               maxI = k;
            }
         }
         gains[maxI] = 0;
         answer -= max;
      }

      std::cout << "Case #" << i+1 << ": " << answer << std::endl;
   }
}