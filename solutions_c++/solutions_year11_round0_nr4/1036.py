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


int main()
{
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);
  int tc; scanf("%d", &tc);
  for (int tt=1; tt<=tc; ++tt)
  {
    int n, x, r = 0;
    scanf("%d", &n);
    forn (i, n) scanf("%d", &x), r += i+1 != x;
    printf("Case #%d: %.10f\n", tt, 1.0*r);    
  }
  
  return 0;
}
