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
#include <queue>
#include <iostream>
#include <iomanip>

using namespace std;

#undef min
#undef max
int min(int a, int b) { return a < b ? a : b; }
int max(int a, int b) { return a > b ? a : b; }

//vector<int> v;
//for(vector<int>::iterator it = v.begin(), end = v.end(); it != end; ++it)
//{
//}

bool find(const vector < vector<int> >& g, int n, int s)
{
   queue<int> q;
   q.push (s);
   vector<bool> used (n);
   used[s] = true;
   while (!q.empty())
   {
      int v = q.front();
      q.pop();

      for (size_t i=0; i < g[v].size(); ++i)
      {
         int to = g[v][i];

         if (to && !used[i])
         {
            used[i] = true;
            q.push (i);
         }
         else if (to)
         {
            return true;
         }
      }
   }
   return false;
}

void Solve()
{
   ifstream input("input.txt");
   ofstream output("output.txt");

   int testCount = 0;
   input >> testCount;

   for (int i = 0; i < testCount; ++i)
   {
      vector < vector<int> > g;
      int n = 0;
      input >> n;

      for (int j = 0; j < n; ++j)
      {
         g.push_back(vector<int>(n, 0));

         int m = 0;
         input >> m;
         for (int k = 0; k < m; ++k)
         {
            int x = 0;
            input >> x;
            g[j][x-1] = 1;
         }
      }

      output << "Case #" << i+1 << ": ";

      bool flag = false;
      for (int j = 0; j < n; ++j)
      {
         if (find(g, n, j))
         {
            output << "Yes\n";
            flag = true;
            break;
         }
      }

      if (!flag)
      {
         output << "No\n";
      }
   }
}
