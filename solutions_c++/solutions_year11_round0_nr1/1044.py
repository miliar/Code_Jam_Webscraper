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

const int maxn = 105;

int a[maxn], b[maxn];
int n;

int main()
{
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);
  
  int tc; scanf("%d", &tc);
  for (int tt=1; tt<=tc; ++tt)
  {
    scanf("%d", &n);
    forn (i, n)
    {
      string s; cin >> s >> a[i];
      b[i] = s == "O" ? 0 : 1;
    }    
    int res = 0, x[2] = {1, 1}, t[2] = {0, 0};
//    forn (i, n) printf("%d %d\n", a[i], b[i]);
    forn (i, n)
    {
//      printf("[%d %d] [%d %d] = %d\n", x[0], t[0], x[1], t[1], res);
      int have = res-t[b[i]];
      int need = abs(a[i]-x[b[i]]);
      x[b[i]] = a[i];
      need -= have;
      if (need < 0) need = 0;      
      res += need+1;
      t[b[i]] = res;
    }
    printf("Case #%d: %d\n", tt, res);
      

  }
  
  return 0;
}
