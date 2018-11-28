#include <cstdio>
#include <cassert>
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

int n, tn, nt, m;

int a[1000005];
int b[15];

ll pow(ll x, ll p, ll mod)
{
  ll res=1;
  while (p) {
    if (p&1) res=(res*x)%mod;
    x=(x*x)%mod;
    p>>=1;
  }
  return res;
}

int check(long long p)
{
  if (b[m-1]==b[m-2]) {
    return b[m-1];
  }
  assert(b[0]!=b[1] && m>=3);
  ll x=(b[2]-b[1]+p)%p;
  ll y=(b[1]-b[0]+p)%p;
//  cerr<<x<<" "<<y<<endl;
  ll A=((x*pow(y, p-2, p))%p+p)%p;
  assert(A != 0);
  ll B=((b[1]-A*b[0])%p+p)%p;
//  cerr<<A<<" "<<B<<" "<<p<<" "<<b[0]<<" "<<b[1]<<endl;
  for (int i=0; i<m-1; i++)
    if ((A*b[i]+B)%p != b[i+1])
      return -1;
  return ((A*b[m-1]+B)%p+p)%p;

}

int main(void)
{
   //freopen("A-small-attempt2.in", "r", stdin);
   //freopen("A-small-attempt2.out", "w", stdout);
   freopen("A-large.in", "r", stdin);
   freopen("A-large.out", "w", stdout);

   for (int i=2; i<=1000; i++)
     if (!a[i])
       for (int j=i*i; j<=1000000; j+=i)
         a[j]=1;

   scanf("%d\n", &nt);
   for (tn=0; tn<nt; tn++)
   {
      fprintf(stderr, "Case #%d: \n", tn+1);

      scanf("%d%d", &n, &m);
      int mi=0;
      for (int i=0; i<m; i++)
      {
        scanf("%d", &b[i]);
        if (b[i]>mi) mi=b[i];
      }
      int d=1;
      for (int i=0; i<n; i++)
        d*=10;

      int ans=-1, nans=0;
      printf("Case #%d: ", tn+1);
      
      if (m==1) nans=2;
      if (m==2 && b[m-1]!=b[m-2]) nans=2;
      for (int pr=mi+1; pr<d && nans<2; pr++)
        if (!a[pr])
        {
          int t=check(pr);
          if (t != ans && t!=-1) {
            ans=t;
            nans++;
          }
        }

      if (nans == 2)
        puts("I don't know.");
      else
        printf("%d\n", ans);
      assert(nans);
   }
   return 0;
}
