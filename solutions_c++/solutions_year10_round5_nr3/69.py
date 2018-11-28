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

int main(void)
{
   freopen("C-small-attempt0.in", "r", stdin);
   freopen("C-small-attempt0.out", "w", stdout);
   //freopen("C-large.in", "r", stdin);
   //freopen("C-large.out", "w", stdout);

   scanf("%d\n", &nt);
   for (tn=0; tn<nt; tn++)
   {
      fprintf(stderr, "Case #%d: \n", tn+1);

      scanf("%d", &n);
      map <int, int> m;
      for (int i=0; i<n; i++)
      {
        int x, y;
        scanf("%d%d", &x, &y);
        m[x]=y;
      }

      int res=0;
      while (1)
      {
        map <int, int> m1;
        int good=0;
        for (map<int,int>::iterator p=m.begin(); p!=m.end(); p++)
        {
          int x=p->first;
          int y=p->second;
          if (y&1)
            m1[x]++;
          if (y>=2) {
            m1[x-1]+=y/2;
            m1[x+1]+=y/2;
            res+=y/2;
            good=1;
          }
        }
        if (!good)
          break;
        m=m1;
      }

      printf("Case #%d: ", tn+1);

      printf("%d\n", res);
   }
   return 0;
}
