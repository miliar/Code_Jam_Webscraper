#include <iostream>

int main ()
{
   long long T, K, N; 
   std::cin >> T;
   for (int c = 1; c <= T; ++c)
   {
      std::cin >> N >> K;
      long long mask = (1 << N) - 1;
      std::cout << "Case #" << c << ": "
                << ((K & mask) == mask ? "ON" : "OFF") << "\n";
   }
}
