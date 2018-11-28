#include <iostream>

int main()
{
   int T; std::cin >> T;

   for (int t = 0; t < T; ++t)
   {
      int N, K;
      std::cin >> N >> K;
      int msk = (1<<N)-1;
      std::cout << "Case #" << t+1 << ": " 
                << (((K & msk) == msk) ? "ON" : "OFF")
                << std::endl;
   }   
}
