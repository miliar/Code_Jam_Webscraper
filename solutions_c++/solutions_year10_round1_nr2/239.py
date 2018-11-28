#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

int val[110];
int tab[110][300];
int costd, costi, m, n;

int go(int l, int v)
{
  if (tab[l][v] != -1)
    return tab[l][v];
  if (l == 0)
    return tab[l][v] = 0;
  
  int ans = 0x7fffffff;

  // do nothing
  if (abs(val[l-1] - v) <= m)
    ans = min(ans, go(l-1, val[l-1]));

  // deletion
  ans = min(ans, costd + go(l-1, v));

  // substitution
  for (int i=0; i<256; ++i)
    if (abs(v - i) <= m)
      ans = min(ans, abs(val[l-1] - i) + go(l-1, i));

  // insertion
  if (val[l-1] < v)
    for (int i=v-1; i>val[l-1]; --i)
      if (abs(v - i) <= m)
	ans = min(ans, costi + go(l, i));
  if (val[l-1] > v)
    for (int i=val[l-1]-1; i>v; --i)
      if (abs(v - i) <= m)
	ans = min(ans, costi + go(l, i));
  
  return tab[l][v] = ans;
}

int main()
{
  int ntests;
  scanf(" %d", &ntests);
  for (int test=0; test<ntests; ++test)
    {
      scanf(" %d %d %d %d", &costd, &costi, &m, &n);
      for (int i=0; i<n; ++i)
	scanf(" %d", &val[i]);
      memset(tab, -1, sizeof(tab));
      int ans = 0x7fffffff;
      for (int i=0; i<256; ++i)
	ans = min(ans, go(n, i));

      // for (int i=0; i<n; ++i)
      // 	{
      // 	  for (int j=0; j<10; ++j)
      // 	    printf("%d ", tab[i][j]);
      // 	  printf("\n");
      // 	}
      
      printf("Case #%d: %d\n", test+1, ans);
    }
  return 0;
}
