#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <set>
#include <cassert>
#include <ctime>
#include <cstdlib>
#include <cmath>
#include <cstring>

#define eps 1e-9

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define sz(v)((v).size())

#define task_name "c"


using namespace std;
typedef long long ll;

#define maxn 1100

ll g[maxn], ne[maxn], add[maxn], was[maxn];
ll curr[maxn];

int main( void )
{
  freopen(task_name ".in", "r", stdin);
  freopen(task_name ".out", "w", stdout);

  int tn;
  scanf("%d", &tn);

  for (int tt = 1; tt <= tn; tt++)
  {
    int r, k, n;
    cin >> r >> k >> n;
    ll sum = 0;
    for (int i = 0; i < n; i++) {
      cin >> g[i];
    }

    for (int i = 0; i < n; i++) {
      sum += g[i];
    }
    
    ll res = 0;
    if (sum <= k) {
      res = sum * r;
    } else {
      for (int s = 0; s < n; s++) {
        add[s] = 0;
        int t = s;
        while ((add[s] + g[t]) <= k) {
          add[s] += g[t];
          if (++t == n) {
            t = 0;
          }
        }
        ne[s] = t;
        //cerr << s << ":" << ne[s] << ":" << add[s] << endl; 
      }

      memset(was, 0, sizeof(ll) * n);
      int s = 0, f = 1, i = 1;
      while (r--) {
        if (was[s] && f) {
          f = 0;
          res += (r / (i - was[s])) * (res - curr[s]);
          r %= (i - was[s]);
        }
        was[s] = i++;
        curr[s] = res;
        res += add[s];
        s = ne[s];
      }
    }

    printf("Case #%d: ", tt);
    cout << res << endl;
  }

   
  
  return 0;
}