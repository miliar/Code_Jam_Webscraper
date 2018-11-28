#include <iostream>
using namespace std;



int main()
{
   int x;
   cin >> x;
   for(int i = 0; i < x; i++)
   {
      int n, d, g;
      cin >> n >> d >> g;

      /*
      for(int j = 0; j < d; j++)
      {
         //dx = 100y
         for(int k = 0; k < n; k++)//total
         {
            for(int l = 0; l < n - k; l++)//won
            {

            }
         }
      }
      */

      //find gcd
     //  std::cout << n << " " << d << " " << g << std::endl;
       int d1 = d;
      int dd = 100;
      for(int j = 2; j <=   d; j++)
      {
         if( d % j == 0 && dd % j == 0 )
         {
            d /= j;
            dd /= j;
            j = 1;
         }
      }
     
      //std::cout << d << " " << dd << std::endl;

      

      bool w = false;
      if( dd <= n && g != 100)
         w = true;
      if( d1 == 100 && g == 100)
         w = true;
      if( g == 0 && d != 0 )
         w = false;
      if( d == 0 && g != 100)
         w = true;
     


      //for(int j = 1; j <= n; j++)
     // {
       //  w |= j * (d / 100.0) == (g / 100.0);
     // }

      if(w)
         std::cout << "Case #" << i+1 << ": Possible" << std::endl;
      else
         std::cout << "Case #" << i+1  << ": Broken" << std::endl;
   }
}