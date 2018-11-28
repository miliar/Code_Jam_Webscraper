#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;

int T;
long long n, pd, pg;

long long gcd(long long x, long long y) {
  if (x < y) swap(x, y);
  if (x % y == 0) return y;
  else return gcd(y, x % y);
}

int main() {

  freopen("A-large.in", "rt", stdin);
  freopen("A-large.out", "wt", stdout);
  
  scanf("%d", &T);
  for(int cT = 0; cT < T; cT ++) {
  /*  scanf("%d%d%d", &n, &pd, &pg);
    bool ok = false;
    for(int D = 1; D <= n; D++)
      if (D * pd % 100 == 0) {ok = true; break; }
    if (pg == 100 && pd < 100) ok = false;
    if (pg == 0 && pd > 0) ok = false;
    printf("Case #%d: ", cT+1);
    if (ok) puts("Possible"); else puts("Broken");*/
    
    scanf("%lld%lld%lld", &n, &pd, &pg);
    bool ok = false;
    long long expect = -1;
    if (pd == 0) expect = 1;
    else expect = 100 / gcd(100, pd);
    
    if (expect <= n) ok = true;
    if (pg == 100 && pd < 100) ok = false;
    if (pg == 0 && pd > 0) ok = false;
    printf("Case #%d: ", cT+1);
    if (ok) puts("Possible"); else puts("Broken");
    
  }

  
  return 0;

}
