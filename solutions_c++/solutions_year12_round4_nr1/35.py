#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;
typedef long long ll;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define FOR(i, s, t) for(i = (s); i < (t); i++)
#define RFOR(i, s, t) for(i = (s)-1; i >= (t); i--)

int f[10004];
int d[10004], l[10004];

int main()
{
  #ifdef __FIO
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  #endif
  int _;
  scanf("%d", &_);
  for(int i0 = 1; i0 <= _; i0++){
    printf("Case #%d: ", i0);
    int n;
    int i, j;
    scanf("%d", &n);
    d[0] = 0;
    for(i = 1; i <= n; i++)
      scanf("%d%d", &d[i], &l[i]);
    memset(f, -10, sizeof f);
    f[1] = d[1];
    for(i = 1; i <= n; i++)
      if(f[i] >= 0){
        f[i] = min(f[i], l[i]);
        for(j = i+1; j <= n; j++)
          if(d[i]+f[i] >= d[j])
            f[j] = max(f[j], d[j]-d[i]);
      }
    scanf("%d", &j);
    for(i = 1; i <= n; i++)
      if(f[i] >= 0 && d[i]+f[i] >= j)
        break;
    if(i <= n)
      printf("YES\n");
    else
      printf("NO\n");
  }
  return 0;
}
