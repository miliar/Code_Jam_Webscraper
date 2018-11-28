#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <queue>
#include <set>
#include <ctime>

#define FOR(i,a,b) for(int i = (a); i < (b); i++)
#define FORIN FOR(i, 0, n)
#define FORV(x) for(int i = 0, __len = (x).size(); i < __len; i++)

#define MAXN 1001

using namespace std;
int t, n, w, l, r[MAXN], x[MAXN], y[MAXN];
bool found;

void init()
{
   found = false;
}

void read()
{
   cin >> n >> w >> l;
   for (int i = 0; i < n; i++)
      cin >> r[i];
}

void write(int casen)
{
   cout << "Case #" << casen << ": ";
   if (!found)
      cout << "NOT FOUND!!!" << endl;
   else
   {
      for (int i = 0; i < n - 1; i++)
         cout << x[i] << " " << y[i] << " ";
      cout << x[n - 1] << " " << y[n - 1] << endl;
   }
}

void solve()
{
   for (int s = 0; s < 1000000; s++)
   {
      for (int i = 0; i < n; i++)
      {
         x[i] = rand() % (w + 1);
         y[i] = rand() % (l + 1);
      }
      bool bad = false;
      for (int i = 0; i < n; i++)
      {
         for (int j = i + 1; j < n; j++)
         {
            if (sqrt(((double)(x[j] - x[i]) * (double)(x[j] - x[i]) + (double)(y[j] - y[i]) * (double)(y[j] - y[i]))) < (double)(r[i] + r[j]))
            {
               bad = true;
               break;
            }
         }
         if (bad)
            break;
      }
      if (!bad)
      {
         found = true;
         break;
      }
   }
}

int main()
{
   cin >> t;
   srand(time(NULL));
   for (int casen = 0; casen < t; casen++)
   {
      init();
      read();
      solve();
      write(casen + 1);
   }
   return 0;
}
