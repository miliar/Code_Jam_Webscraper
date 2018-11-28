#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>

using namespace std;

const int inf = 100000;

vector< int > y;
vector< int > next;
int n;

inline bool rec(int x)
{
  if (x == -1)
  {
    return true;
  }
  
  int q = next[x];
  
  int downbound = -inf;
  int upbound = inf;
  
  for (int i = x+1; i < q; i++)
  {
    int x1 = i;
    int y1 = y[i];
    int x2 = q;
    int y2 = y[q];
    
    downbound = max(downbound, int(y2 - (y2-y1)*1.0/(x2-x1)*(x2-x)) + 10);
  }
  
  for (int i = q+1; i < n; i++)
  {
    int x1 = i;
    int y1 = y[i];
    int x2 = q;
    int y2 = y[q];
    
    upbound = min(upbound, int(y2 - (y2-y1)*1.0/(x2-x1)*(x2-x)) - 10);
  }
  
  if (upbound < downbound)
    return false;
  
  y[x] = upbound;
  if (rec(x-1))
    return true;
  y[x] = downbound;
  if (rec(x-1))
    return true;
  return false;
}

inline void solve(int testnum)
{
  scanf("%d", &n);
  y.resize(n);
  next.resize(n);
  next[n-1] = -1;
  for (int i =0 ; i< n-1; i++)
  {
    scanf("%d", &next[i]);
    next[i]--;
  }
  
  y[n-1] = 0;
  y[n-2] = 0;
  
  printf("Case #%d: ", testnum+1);
  
  if (rec(n-3))
  {
    int minheight = 1<<30;
    for (int i = 0; i < n; i++)
      minheight = min(minheight, y[i]);
    for (int i = 0; i < n; i++)
      y[i] -= minheight;
    
    for (int i = 0; i < n; i++)
      printf("%d ", y[i]);
    printf("\n");
  }
  else
  {
    printf("Impossible\n");
  }
}

int main()
{
  int testkol;
  scanf("%d\n", &testkol);
  for (int i = 0; i < testkol; i++)
    solve(i);
}