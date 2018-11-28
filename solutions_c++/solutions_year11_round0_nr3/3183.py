#include <iostream>
#include <vector>
using namespace std;

int main()
{
   int T;
   cin >> T;
   for(int i = 0; i < T; i++)
   {
      int N;
      cin >> N;
      vector< int > candy;
      for(int j = 0; j < N; j++)
      {
         int x;
         cin >> x;
         candy.push_back( x );
      }

      int maxSean = -1;
      for(int j = 0; j < 1 << N; j++)//enumerate partitions (won't work for large test case)
      {
    //     std::cout << j << std::endl;
         int sean = 0;
         int patrick = 0;
         int sum = 0;
         bool s = false;
         bool p = false;

         for(int k = 0; k < N; k++)
         {
            if((j >> k) % 2)//sean's pile
            {
               s = true;
              // std::cout << "s";
               sean = sean ^ candy[k]; 
               sum += candy[k];
            }
            else
            {
               p = true;
             //  std::cout << "p";
               patrick = patrick ^ candy[k];
            }
         }

      //   std::cout << sean << " " << patrick << " " << sum << std::endl;

         if(sean == patrick && sum > maxSean && s && p)
            maxSean = sum;
      }
      
      std::cout << "Case #" << i+1 << ": ";
      if(maxSean == -1)
         std::cout << "NO" << std::endl;
      else
         std::cout << maxSean << std::endl;
   }
}