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
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define REP(i,n) for ((i) = 0; (i) < (int)(n); (i)++)
// Type
#define OSS ostringstream
#define ISS istringstream
#define CAST(x,type)  *({OSS oss; oss << (x); ISS iss(oss.str()); static type _r; iss >> _r; &_r; })

#define MAXV 10001

int main() {
  int T;
  scanf("%d", &T);
  for (int testCase = 1; testCase <= T; ++testCase) {
    printf("Case #%d: ", testCase);

    int N; scanf("%d", &N);
    vector<int> elements(N);
    set<int> correct;
    for (int i = 0; i < N; ++i) {
      scanf("%d", &elements[i]);
      if (i + 1 == elements[i]) correct.insert(i);
    }

    double ans = 0.0;
    for (int i = 0; i < N; ++i) {
      if (correct.count(i) == 0) {
        int count = 1;
        int next = elements[i];
        while (next != i + 1) {
          count++;
          correct.insert(next - 1);
          next = elements[next - 1];
        }
        correct.insert(i);
        ans += count;
      }
    }
    printf("%f\n", ans);
  }
  return 0;
}
