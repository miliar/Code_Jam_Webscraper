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

char bac[110][110];
int r;

int main()
{
  int ntests;
  scanf(" %d", &ntests);
  for (int test=1; test<=ntests; ++test)
    {
      memset(bac, 0, sizeof(bac));
      scanf(" %d", &r);
      for (int i=0; i<r; ++i)
	{
	  int x0, y0, x1, y1;
	  scanf(" %d %d %d %d", &x0, &y0, &x1, &y1);
	  for (int j=x0; j<=x1; ++j)
	    for (int k=y0; k<=y1; ++k)
	      bac[j][k] = 1;
	}
      bool found = true;
      int nsteps = 0;
      while (found)
	{
	  ++nsteps;
	  found = false;
	  for (int i=100; i>=1; --i)
	    for (int j=100; j>=1; --j)
	      {
		if (bac[i-1][j] == 0 && bac[i][j-1] == 0)
		  bac[i][j] = 0;
		else if (bac[i-1][j] && bac[i][j-1])
		  bac[i][j] = 1;
		if (bac[i][j])
		  found = true;
	      }
	}
      printf("Case #%d: %d\n", test, nsteps);
    }
  return 0;
}
