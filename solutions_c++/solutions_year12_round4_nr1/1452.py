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
#include <inttypes.h>

// Macro
#define foreach(c, i) for (__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define mp make_pair
#define ALL(a) (a).begin(), (a).end()
#define OSS ostringstream
#define ISS istringstream
#define CAST(x,type)  *({OSS oss; oss << (x); ISS iss(oss.str()); static type _r; iss >> _r; &_r; })
#define ARRAY_SIZE(x) (sizeof(x) / sizeof( (x)[0]) )

using namespace std;

const int MAX_N = 10010;

void CommonInit() {
}

struct Problem {
  int N;
  int d[MAX_N], l[MAX_N], D;

  void Input() {
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
      scanf("%d %d", d + i, l + i);
    }
    scanf("%d", &D);
  }

  void Solve() {
    if (d[0] > l[0]) {
      printf("NO");
      return;
    }

    queue <pair<int, int> > q;
    q.push(mp(0, 0));
    while (!q.empty()) {
      int curD = q.front().first;
      int curI = q.front().second;
      q.pop();

      int len = d[curI] - curD;
      int reachable = d[curI] + len;
      if (reachable >= D) {
        printf("YES");
        return;
      }

      for (int i = curI + 1; i < N; i++) {
        if (d[i] <= reachable) {
          if (l[i] < d[i] - d[curI]) {
            q.push(mp(d[i] - l[i], i));
          } else {
            q.push(mp(d[curI], i));
          }
        } else {
          break;
        }
      }
    }
    printf("NO");
  }
};

int main() {
  int T;
  scanf("%d", &T);
  CommonInit();
  for (int testCase = 1; testCase <= T; ++testCase) {
    printf("Case #%d: ", testCase);
    Problem p;
    p.Input();
    p.Solve();
    printf("\n");
  }

  return 0;
}
