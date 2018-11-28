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

#define eps 1e-9

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define sz(v)((v).size())

#define task_name "b"


using namespace std;

typedef long long ll;

#define maxn 55

ll x[maxn], v[maxn];

int main( void )
{
  freopen(task_name ".in", "r", stdin);
  freopen(task_name ".out", "w", stdout);

  int tn;
  scanf("%d", &tn);

  for (int tt = 1; tt <= tn; tt++)
  {
    printf("Case #%d: ", tt);

    int n, k, b, t;
    cin >> n >> k >> b >> t;
    for (int i = 0; i < n; i++) {
      cin >> x[i];
    }
    for (int i = 0; i < n; i++) {
      cin >> v[i];
    }

    int res = 0, curr = 0, add = 0;
    for (int i = n - 1; i >= 0 && curr < k; i--) {
       if ((b - x[i]) <= t * v[i]) {
         res += add;
         curr++;
       } else {
         add++;
       }
    }
    if (curr == k) {
      printf("%d\n", res);
    } else {
      printf("IMPOSSIBLE\n");
    }
  }

   
  
  return 0;
}