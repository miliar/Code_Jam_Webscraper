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

vector< int > maxlen;
int n;
vector< int > d, l;

inline void solve(int testnum)
{
  scanf("%d", &n);
  maxlen.assign(n + 1, 0);
  d.resize(n);
  l.resize(n);
  
  for (int i = 0; i < n; i++)
    scanf("%d %d", &d[i], &l[i]);
  
  scanf("%d", &d[n]);
  l[n] = 1<<30;
  maxlen[0] = d[0];
  
  for (int i= 0 ;i < n ; i++)
  {
    int jumplen = maxlen[i];
    
    for (int j = i+1; j <= n; j++)
    {
      if (d[j] > d[i] + jumplen)
	break;
      
      maxlen[j] = max(maxlen[j], min(l[j], d[j] - d[i]));
    }
  }
  
  printf("Case #%d: ", testnum+1);
  if (maxlen[n] != 0)
    printf("YES\n");
  else
    printf("NO\n");
}

int main()
{
  int testkol;
  scanf("%d\n", &testkol);
  for (int i = 0; i < testkol; i++)
    solve(i);
}