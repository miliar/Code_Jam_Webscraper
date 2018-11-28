#include <string>
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <queue>
#include <cassert>

using namespace std;

const int MAXN = 1000;

int main(void) {
  int T; scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    int A[MAXN], B[MAXN];
    memset(B, 0, sizeof B);
    int N; scanf("%d", &N);
    for (int i = 1; i <= N; ++i)
      scanf("%d", &A[i]);
    int ret = 0;
    for (int i = 1; i <= N; ++i) {
      if (B[i]) continue;
      int len = 1;
      for (int j = A[i]; j != i; ++B[j], j = A[j]) 
        ++len;
      if (len > 1)
        ret += len;
    }
    printf("Case #%d: %d\n", t, ret);

  }
  return 0;
}
