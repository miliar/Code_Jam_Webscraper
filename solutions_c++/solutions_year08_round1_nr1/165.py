#include <stdio.h>
#include <stdlib.h>

int ca, n, x[1000], y[1000];

int cmp(const void* a, const void* b)
{
  if (*((int*)a)<*((int*)b)) return -1;
  if (*((int*)a)>*((int*)b)) return 1;
  return 0;
}

int main()
{
  scanf(" %d ", &ca);
  for(int cs=1; cs<=ca; cs++)
    {
      scanf(" %d ", &n);
      for(int i=0; i<n; i++)
	scanf(" %d ", x+i);
      for(int i=0; i<n; i++)
	scanf(" %d ", y+i);
      qsort(x, n, sizeof(int), cmp);
      qsort(y, n, sizeof(int), cmp);
      long long res=0;
      for(int i=0; i<n; i++)
	res+=((long long)x[i])*((long long)y[n-i-1]);
      printf("Case #%d: %lli\n", cs, res);
    }
  return 0;
}
