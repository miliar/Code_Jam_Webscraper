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

#define ll long long

int tn, nt, n;

int get(int i, int j)
{
  if (i==j) return 0;
  if (i<j) swap(i, j);
  if (i>=2*j) return 1;
  if (get(i-j, j)) return 0;
  return 1;
}

int main(void)
{
   freopen("C-small-attempt1.in", "r", stdin);
   freopen("C-small-attempt1.out", "w", stdout);
   //freopen("C-large.in", "r", stdin);
   //freopen("C-large.out", "w", stdout);

   scanf("%d\n", &nt);

   for (tn=0; tn<nt; tn++)
   {
      fprintf(stderr, "Case #%d: \n", tn+1);

      int a1, a2, b1, b2;
      scanf("%d%d%d%d", &a1, &a2, &b1, &b2);

      int res = 0;
      for (int i=a1; i<=a2; i++)
        for (int j=b1; j<=b2; j++)
          res+=get(i, j);

      printf("Case #%d: %d", tn+1, res);
      printf("\n");
   }
   return 0;
}
