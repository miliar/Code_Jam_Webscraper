#include <cstdio>
#include <iostream>
#include <vector>
#include <memory.h>
#include <string.h>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <string>
using namespace std;

#define pb push_back
#define mp make_pair
#define sz(a) int((a).size())
#define forn(i, n) for (int i=0; i<(n); ++i)
#define foreach(it, a) for (__typeof((a).begin()) it=(a).begin(); it!=(a).end(); ++it)

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

const int maxn = 10005;

int a[maxn];
int n;

int main()
{
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);
  
  int tc; scanf("%d", &tc);
  for (int tt=1; tt<=tc; ++tt)
  {   
    scanf("%d", &n);
    forn (i, n) scanf("%d", a+i);
    int s = 0, x = 0, l = 1000000000;
    forn (i, n) 
      s += a[i], x ^= a[i], l = min(l, a[i]);
    printf("Case #%d: ", tt);
    if (x != 0) puts("NO");
    else printf("%d\n", s-l);
  }
  
  return 0;
}
