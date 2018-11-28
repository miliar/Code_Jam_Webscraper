#include <cstdio>
#include <iostream>
#include <string>
#include <memory.h>
#include <string.h>
#include <vector>
#include <algorithm>
#include <utility>
#include <cmath>
#include <set>
#include <sstream>
#include <map>
using namespace std;

#define mp make_pair
#define pb push_back
#define sz(a) int((a).size())
#define forn(i, n) for (int i=0; i<(n); ++i)

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

int n;
int m[1<<12];
int f[1<<12];


int main()
{
  freopen("b.in", "r", stdin);
  freopen("b.out", "w", stdout);

  int tc;
  scanf("%d", &tc);

  for (int tt=1; tt<=tc; ++tt)
  {
    printf("Case #%d:", tt);

    scanf("%d", &n);

    forn (i, (1<<n)) scanf("%d", &m[i]);
    forn (i, 3000) f[i] = 0;

    forn (i, n)
    {
      int k = 1<<(n-i-1);
      int x;
      forn (j, k) scanf("%d", &x);
    }


    forn (i, (1<<n))
    {
      int x = i, y = 0, cnt = n-m[i];
      for (int j=n-1; j>=0; --j)
      {
        if (cnt > 0) f[y] = 1, --cnt;
        if (x & (1<<j)) y = 2*y+2;
        else y = 2*y+1;
      }
    }
    
    int res = 0;
    forn (i, 3000) res += f[i];
    printf(" %d\n", res);

  }

  return 0;
}
