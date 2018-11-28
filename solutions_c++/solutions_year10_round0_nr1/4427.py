// Qualification_A.cpp : Defines the entry point for the console application.
//

#include <vector>
#include <iostream>
#include <utility>


typedef std::vector <int>         IntVector;
typedef std::vector <std::string> StringVector;

typedef std::vector <IntVector>   IntVectorVector;

typedef std::pair <int, int>      IntPair;


bool solve (int N, int K)
{
   //if (K == 0)
   //   return N % 2;

   std::vector <bool> ons (N),
                      powers (N);

   powers [0] = true;

   for (int k = 0; k < K; ++k)
   {
      for (int n = 0; n < N; ++n)
         if (powers [n])
            ons [n] = !ons[n];

      bool powerOn = true;
      for (int n = 0; n < N; ++n)
      {
         powers [n] = powerOn;
         if (!ons [n])
            powerOn = false;
      }

   }

   return powers.back() && ons.back();
}
                                

int main(int argc, char* argv[])
{
   bool b = solve (1, 0);
        b = solve (1, 1);
        b = solve (4, 0);
        b = solve (4, 47);

   int T;

   std::cin >> T;
   for (int t = 0; t < T; ++t)
   {
      int N, K;
      std::cin >> N >> K;
      std::cout << "Case #" << t + 1 << ": ";
      if (solve (N, K))
         std::cout << "ON\n";
      else
         std::cout << "OFF\n";
   }
}

