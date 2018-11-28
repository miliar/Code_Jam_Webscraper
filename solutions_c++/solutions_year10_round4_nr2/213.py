#include <cstdio>
#include <cmath>
#include <string>
#include <iostream>
#include <vector>
#include <sstream>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int n, tn, nt;

int a[5025];
int d[5049][12];
int pr[5000];

int get(int x, int y)
{
  if (x>=(1<<n))
  {
    if ((n-a[x])-y<=0) return 0;
    return 1000000000;
  }
  if (d[x][y]!=-1) return d[x][y];
  int &res=d[x][y]=1000000000;

  res=min(res, pr[x]+get(x+x, y+1) + get(x+x+1, y+1));
  res=min(res, get(x+x, y) + get(x+x+1, y));

  return res;
}

int main(void)
{
   //freopen("B-small-attempt0.in", "r", stdin);
   //freopen("B-small-attempt0.out", "w", stdout);
   freopen("B-large.in", "r", stdin);
   freopen("B-large.out", "w", stdout);

   scanf("%d\n", &nt);
   for (tn=0; tn<nt; tn++)
   {
      //fprintf(stderr, "Case #%d: \n", tn+1);

      memset(d, -1, sizeof(d));
      scanf("%d", &n);
      for (int i=0; i<(1<<n); i++)
        scanf("%d", &a[i+(1<<n)]);

      for (int i=n-1; i>=0; i--)
        for (int j=(1<<i); j<(1<<(i+1)); j++)
          scanf("%d", &pr[j]);

      printf("Case #%d: ", tn+1);

      printf("%d\n", get(1, 0));
   }
   return 0;
}
