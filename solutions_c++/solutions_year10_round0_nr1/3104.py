#include <iostream>
#include <cmath>
#include <string>
#include <fstream>
#include <sstream>

bool is_on(int n, int k)
{
   int a = (int)std::pow(2.0, n);

   return ((k % a) == (a - 1));
}

void output_case(int c, int n, int k)
{
   std::cout << "Case #" << c << ": "
             << (is_on(n, k) ? "ON" : "OFF")
             << std::endl;
}

int main()
{
   std::ifstream file("input.dat");

   int case_num = 0;

   std::string line;
   while (std::getline(file, line))
   {
      int n = 0;
      int k = 0;

      std::istringstream is(line);
      is >> n;

      if (is.good())
      {
         is >> k;
      }

      output_case(++case_num, n, k);
   }

   return 0;
}
