#include <algorithm>
#include <fstream>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>
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

void chunk_pos(vector<int>& v, int x)
{
   for (int i = 0; i < v.size(); ++i)
   {
      if (x > v[i])
      {
         x -= v[i];
      }
      else if (x < v[i])
      {
         v[i] -= x;
         v.erase(v.begin(), v.begin()+i);
         return;
      }
      else
      {
         v.erase(v.begin(), v.begin()+i+1);
         return;
      }
   }

   v.clear();
}

int main(int argc, char* argv[])
{
   ifstream file_in("B.in");
   ofstream file_out("B.out");

   int count_test = 0;
   file_in >> count_test;

   for (int i = 0; i < count_test; ++i)
   {
      int boost_cnt = 0;
      long long delay = 0;
      int star_cnt = 0;
      int size_chunk = 0;
      int sum_chunk = 0;
      file_in >> boost_cnt >> delay >> star_cnt >> size_chunk;
      delay /= 2;

      vector<int> chunk;
      for (int j = 0; j < size_chunk; ++j)
      {
         int x = 0;
         file_in >> x;
         chunk.push_back(x);
         sum_chunk += x;
      }

      int chunk_cnt = star_cnt/size_chunk;
      int copy_chunk_cnt = chunk_cnt;
      vector<int> y_chunk;
      for (int j = 0; j < star_cnt%size_chunk; ++j)
      {
         y_chunk.push_back(chunk[j]);
      }

      vector<int> x_chunk(chunk);

      if (delay <= sum_chunk*chunk_cnt)
      {
         chunk_cnt -= delay/sum_chunk;
         if (delay%sum_chunk > 0)
         {
            chunk_pos(x_chunk, delay%sum_chunk);
            --chunk_cnt;
         }
      }
      else
      {
         chunk_pos(y_chunk, delay-(sum_chunk*chunk_cnt));
         chunk_cnt = 0;
      }

      vector<int> v;
      for (int j = 0; j < x_chunk.size(); ++j)
      {
         v.push_back(x_chunk[j]);
      }
      for (int j = 0; j < y_chunk.size(); ++j)
      {
         v.push_back(y_chunk[j]);
      }
      for (int j = 0; j < chunk_cnt; ++j)
      {
         for (int k = 0; k < chunk.size(); ++k)
         {
            v.push_back(chunk[k]);
         }
      }

      sort(v.begin(), v.end());

      long long profit = 0;
      for (int j = v.size(); boost_cnt>0; --j, --boost_cnt)
      {
         profit += v[j-1];
      }

      long long sum = 0;
      for (int j = 0; j < copy_chunk_cnt; ++j)
      {
         for (int k = 0; k < chunk.size(); ++k)
         {
            sum += chunk[k];
         }
      }

      for (int j = 0; j < y_chunk.size(); ++j)
      {
         sum += y_chunk[j];
      }
      sum *= 2;

      file_out << "Case #" << i+1 << ": " << sum-profit << "\n";	
   }

   file_in.close();
   file_out.close();

   return 0;
}
