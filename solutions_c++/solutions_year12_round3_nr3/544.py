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

struct entry
{
   entry(long long count = 0, long long value = 0) : count(count), value(value) {}
   long long count;
   long long value;
};

long long maximum = 0;

bool my_find(const vector<entry>& v1, int s1,
             const vector<entry>& v2, int s2, long long cur_count2,
             long long sum)
{
   for (int i = s1; i < v1.size(); ++i)
   {
      long long cur_count1 = v1[i].count;

      long long prev_sum = sum;
      long long prev_cur_count2 = cur_count2;

      for (int j = s2; j < v2.size(); ++j)
      {
         if (j != s2)
         {
            cur_count2 = v2[j].count;
         }

         if (cur_count1 <= 0)
         {
            break;
         }

         if (v1[i].value == v2[j].value)
         {
            long long minimum = min(cur_count1, cur_count2);
            sum += minimum;
            cur_count1 -= minimum;
            cur_count2 -= minimum;

            my_find(v1, i+1, v2, j, cur_count2, sum);
         }
      }
      sum = prev_sum;
      cur_count2 = prev_cur_count2;
   }

   maximum = max(maximum, sum);
   sum = 0;

   return true;
}

void Solve()
{
   ifstream input("input.txt");
   ofstream output("output.txt");

   int testCount = 0;
   input >> testCount;

   for (int i = 0; i < testCount; ++i)
   {
      int n = 0, m = 0;
      input >> n >> m;
      vector<entry> box, toy;

      for (int j = 0; j < n; ++j)
      {
         long long x = 0, y = 0;
         input >> x >> y;
         box.push_back(entry(x, y));
      }


      for (int j = 0; j < m; ++j)
      {
         long long x = 0, y = 0;
         input >> x >> y;
         toy.push_back(entry(x, y));
      }

      long long sum = 0;
      my_find(box, 0, toy, 0, toy[0].count, sum);

      output << "Case #" << i+1 << ": " << maximum << "\n";
      maximum = 0;
   }
}
