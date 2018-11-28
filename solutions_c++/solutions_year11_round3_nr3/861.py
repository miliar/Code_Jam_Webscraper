#include <string>
#include <vector>
#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

#define rep(i,n) for (int (i) = 0; (i) < (int)(n); (i)++)
#define REP(i,a,n) for (int(i) = a; (i) < (int)(n); (i)++)
#define iter_type(c) __typeof((c).begin())
#define repi(c, i) for (iter_type(c) i = (c).begin(); i != (c).end(); ++i)
#define pb push_back
#define mp make_pair

#define OSS ostringstream
#define ISS istringstream
#define CAST(x,type)  *({OSS oss; oss << (x); ISS iss(oss.str()); static type _r; iss >> _r; &_r; })
#define ALL(a) (a).begin(), (a).end()
#define ll long long

ll GCD(ll a, ll b) {
  if (b==0) return a;
  return GCD(b,a%b);
}

ll LCM(ll a, ll b) {
  cout << b << endl;
  return b*a/GCD(a,b);
}

bool ok(ll a, ll b) {
  if (a % b == 0) return true;
  if (b % a == 0) return true;
  return false;
}

struct Problem {
  ll N, L, H;
  ll FS[10010];

  void Input() {
    scanf("%llu%llu%llu", &N, &L, &H);
    rep(i, N) scanf("%llu", &FS[i]);
  }

  void Solve() {
    ll lcm = 1;
    ll ans = L;
    for (; ans <= H; ++ans) {
      bool valid = true;
      rep(i, N) {
        if (!ok(ans, FS[i])) {
          valid = false;
          break;
        }
      }
      if (valid) {
        printf("%llu", ans);
        return;
      }
    }
    printf("NO");
  }
};

int main() {
  int T;
  scanf("%d", &T);
  for (int testCase = 1; testCase <= T; ++testCase) {
    printf("Case #%d: ", testCase);
    Problem p;
    p.Input();
    p.Solve();
    printf("\n");
  }

  return 0;
}
