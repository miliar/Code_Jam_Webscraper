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

#define OSS ostringstream
#define ISS istringstream
#define CAST(x,type)  *({OSS oss; oss << (x); ISS iss(oss.str()); static type _r; iss >> _r; &_r; })
#define ALL(a) (a).begin(), (a).end()

long long GCD(long long a, long long b) {
  if (b == 0) return a;
  return GCD(b, a % b);
}

struct Problem {
  long long N;
  int PD, PG;

  void Input() {
    scanf("%lld%d%d", &N, &PD, &PG);
  }

  void Solve() {
    if (PG == 0 && PD != 0) printf("Broken");
    else if (PG == 100 && PD != 100) printf("Broken");
    else {
      long long plusD = 100 / GCD(PD, 100);
      if (plusD <= N) printf("Possible");
      else printf("Broken");
    }
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
