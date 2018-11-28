#include <stdafx.h>

#include <algorithm>
#include <fstream>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#undef min
#undef max
int min(int a, int b) { return a < b ? a : b; }
int max(int a, int b) { return a > b ? a : b; }

//vector<int> v;
//for(vector<int>::iterator it = v.begin(), end = v.end(); it != end; ++it)
//{
//}

void Solve()
{
   ifstream input("input.txt");
   ofstream output("output.txt");

   int testCount = 0;
   input >> testCount;

   for (int i = 0; i < testCount; ++i)
   {
      int N = 0;
      int S = 0;
      int p = 0;
      vector<int> arr;

      input >> N >> S >> p;

      for (int j = 0; j < N; ++j)
      {
         int x = 0;
         input >> x;
         arr.push_back(x);
      }

      int res = 0;

      for (int j = 0; j < N; ++j)
      {
         int x = arr[j] / 3;
         if (arr[j] % 3 == 0) // 0
         {
            if (x >= p)
            {
               ++res;
            }
            else if (x >= 1 && x + 1 >= p && S > 0)
            {
               ++res;
               --S;
            }
         } 
         else if (arr[j] % 3 == 1) // 1
         {
            if (x + 1 >= p)
            {
               ++res;
            }
            //else if (x >= 1 && x + 1 + 1 >= p && S > 0)
            //{
            //   ++res;
            //   --S;
            //}
         }
         else if (arr[j] % 3 == 2) // 1
         {
            if (x + 1 >= p)
            {
               ++res;
            }
            else if (x + 1 + 1 >= p && S > 0)
            {
               ++res;
               --S;
            }
         }

      }

      output << "Case #" << i+1 << ": " << res << "\n";	
   }
}
