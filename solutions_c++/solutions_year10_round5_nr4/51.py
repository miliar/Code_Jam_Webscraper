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

int tn, nt, b;

ll get(int m, int n, int f)
{
  ll res=0;
  if (n==0) return 1;
  for (int j=f; j<=n; j++)
  {
    int t=j, good=1, cd=0;

    while (t)
    {
      int r=t%b;
      if ((m>>(cd+r)) & 1) good=0;
      cd+=b;
      t/=b;
    }

    if (!good) continue;
    int m1=m;

    t=j;
    cd=0;
    while (t)
    {
      int r=t%b;
      m1|=(1<<(cd+r));
      cd+=b;
      t/=b;
    }
    
    res+=get(m1, n-j, j+1);
  }
  return res%1000000007;
}

int main(void)
{
   freopen("D-small-attempt1.in", "r", stdin);
   freopen("D-small-attempt1.out", "w", stdout);
   //freopen("D-large.in", "r", stdin);
   //freopen("D-large.out", "w", stdout);

   scanf("%d\n", &nt);
   for (tn=0; tn<nt; tn++)
   {
      //fprintf(stderr, "Case #%d: \n", tn+1);

      int n;
      scanf("%d%d", &n, &b);
      printf("Case #%d: ", tn+1);

      cout<<get(0, n, 1)<<endl;
   }
   return 0;
}
