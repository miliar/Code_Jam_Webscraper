#include <stdafx.h>

#include <algorithm>
#include <iostream>
#include <fstream>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <assert.h>

using namespace std;

#undef min
#undef max
int min(int a, int b) { return a < b ? a : b; }
int max(int a, int b) { return a > b ? a : b; }

//vector<int> v;
//for(vector<int>::iterator it = v.begin(), end = v.end(); it != end; ++it)
//{
//}

int numDigits(int number)
{
   int digits = 0;
   if (number < 0) digits = 1; // remove this line if '-' counts as a digit
   while (number)
   {
      number /= 10;
      digits++;
   }
   return digits;
}

int exp(int exp)
{
   int x = 1;
   for (int i = 0; i < exp; ++i)
   {
      x *= 10;
   }
   return x;
}


void Solve()
{
   ifstream input("input.txt");
   ofstream output("output.txt");

   int testCount = 0;
   input >> testCount;

   for (int i = 0; i < testCount; ++i)
   {
      int A = 0;
      int B = 0;

      input >> A >> B;

      int res = 0;

      for (int n = A; n < B; ++n)
      {
         set<int> s;
         int m = n;
         int num = numDigits(m);
         int pow = exp(num-1);

         int zeros = 0;
         for (int k = 1; k < num; ++k)
         {
            int last = m%10;
            m = m/10;

            if (last == 0)
            {
               ++zeros;
               continue;
            }

            m = m + last*pow;

            if (n < m && m <= B)
            {
               s.insert(m);
            }
         }
         res += s.size();
      }

      output << "Case #" << i+1 << ": " << res << "\n";	
   }
}
