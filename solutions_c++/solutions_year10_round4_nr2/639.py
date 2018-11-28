#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <functional>
#include <sstream>
#include <iostream>
#include <ctime>
#include <algorithm>
using namespace std;

#define DEBUG(x...) printf(x)
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define _foreach(it, b, e) for(__typeof__(b) it = (b); it != (e); ++it)
#define foreach(x...) _foreach(x)

typedef long long int huge;

const int inf = 0x3f3f3f3f;
const huge hugeinf = 0x3f3f3f3f3f3f3f3fll; // sao dois L's!!!
const double eps = 1e-9;

// em caso de emergencia
#define _inline(f...) inline f() __attribute__((always_inline)); f

int tab[4000];
int cost[4000];

int n;
int p;

int res;
int calc(int v, int lvl)
{
  if (v >= n-1)
    return tab[v];
  int ans = min(calc(2*v+1, lvl-1), calc(2*v+2, lvl-1));
  if (ans <= lvl)
    {
      //printf("adding: %d\n", cost[v]);
      res += cost[v];
    }
  return ans;
}

int main()
{
  int ntests;
  scanf(" %d", &ntests);
  for (int test=1; test<=ntests; ++test)
    {
      scanf(" %d", &p);
      n = (1<<p);
      for (int i=0; i<n; ++i)
	scanf(" %d", &tab[n-1+i]);
      for (int i=0; i<p; ++i)
	for (int j=0; j<(1<<(p-i-1)); ++j)
	  scanf(" %d", &cost[(1<<(p-i-1))+j-1]);
      res = 0;
      calc(0, p-1);
      printf("Case #%d: %d\n", test, res);
    }
  return 0;
}
