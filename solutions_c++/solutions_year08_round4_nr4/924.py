#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>

using namespace std;

int n, k, best, len;
string s;
int perm[20];
int taken[20];

string change ()
{
   int groups = s.size()/k;
   string toret;
   for (int i = 0; i < groups; i++)
      for (int j = 0; j < k; j++)
         toret[i*k+j] = s[i*k+perm[j]];
   return toret;
}

void dothing()
{
   string news = change();
   int sol = 1;
   int i = 1;
   while (1)         
   {
      while (i < len && news[i] == news[i-1])
         i++;
      if (i == len)
         break;
      sol++;
      i++;
   }
   if (sol < best)
      best = sol;
}

void permut(int col)
{
   if (col == k)
   {
      dothing();
      return;
   }
   
   for (int i = 0; i < k; i++)
   {
      if (!taken[i])
      {
         taken[i] = 1;
         perm[col] = i;
         permut(col+1);
         taken[i] = 0;
      }
   }
   
}

int main ()
{
   cin >> n;
   
   for (int testCase = 1; testCase <= n; testCase++)
   {
      cin >> k;
      cin >> s;
      len = s.size();
      best = len;

      permut(0);

      cout << "Case #" << testCase << ": " << best << endl;
   }
   
   return 0;
}
