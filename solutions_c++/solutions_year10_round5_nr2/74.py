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

ll a[105];
int n, tn, nt;

int dp[1000005];
ll g[105];

int main(void)
{
   freopen("B-small-attempt0.in", "r", stdin);
   freopen("B-small-attempt0.out", "w", stdout);
   //freopen("B-large.in", "r", stdin);
   //freopen("B-large.out", "w", stdout);

   scanf("%d\n", &nt);
   for (tn=0; tn<nt; tn++)
   {
      fprintf(stderr, "Case #%d: \n", tn+1);

      ll l;
      cin >> l;
      scanf("%d", &n);
      ll d = 0;
      for (int i=0; i<n; i++)
      {
        cin>>a[i];
        d = __gcd(d, a[i]);
      }

      printf("Case #%d: ", tn+1);

      if (l%d != 0)
        puts("IMPOSSIBLE");
      else
      {
        for (int i=0; i<n; i++)
          a[i]/=d;
        l/=d;

        sort(a, a+n);

        g[0]=a[0];
        for (int i=0; i<n; i++)
          g[i]=__gcd(a[i], g[i-1]);

        memset(dp, 63, sizeof(dp));
        int inf = dp[0];
        dp[0]=0;
        for (int i=0; i<n; i++)
          for (int j=0; j<1000004-a[i]; j++)
            dp[j+a[i]]=min(dp[j+a[i]], 1+dp[j]);

        ll res=(ll)2e18;
        for (int j=0; j<=1000000; j++)
          if (dp[j]!=inf && (l-j)%a[n-1]==0)
            res=min(res, (l-j)/a[n-1] + dp[j]);

        cout<<res<<endl;
      }
   }
   return 0;
}
