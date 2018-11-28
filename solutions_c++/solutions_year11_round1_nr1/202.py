#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cassert>
#include <memory.h>
#include <cstdlib>
#include <iostream>
#include <cmath>

using namespace std;

typedef long long ll;
typedef long double dbl;

#define x first
#define y second
#define pnt pair <int, int>
#define mp make_pair
#define pb push_back
#define forn(i, n) for (int i = 0; i < (int)(n); i++)

int T;
ll N;
int pd, pg;

int main() {
  cin >> T;
  forn (q, T) {
    cin >> N >> pd >> pg;
    int a1 = pd, b1 = 100, a2 = pg, b2 = 100;
    int d = __gcd(a1, b1);
    a1 /= d, b1 /= d;
    d = __gcd(a2, b2);
    a2 /= d, b2 /= d;

    printf("Case #%d: ", q + 1);
    int bad = 0;
    if (a1 == 0 && a2 != 0) bad = 1;
    if (a2 == b2 && a1 != b1) bad = 1;
    if (a2 == 0 && a1 != 0) bad = 1;
    if (b1 <= N && !bad) puts("Possible"); else puts("Broken");
    
    
  }

  return 0;
}

