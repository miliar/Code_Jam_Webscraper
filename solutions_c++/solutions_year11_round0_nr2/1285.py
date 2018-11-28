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

const int MAXN = 100;
const int MAXC = 256;

int main(void) {
  int T; scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    int combine[MAXC][MAXC];
    memset(combine, 0, sizeof combine);
    int C; scanf("%d", &C);
    for (int i = 0; i < C; ++i) {
      char a, b, c;
      scanf(" %c%c%c", &a, &b, &c);
      combine[a][b] = combine[b][a] = c;
    }
    int opposed[MAXC][MAXC];
    memset(opposed, 0, sizeof opposed);
    int D; scanf("%d", &D);
    for (int i = 0; i < D; ++i) {
      char a, b;
      scanf(" %c%c", &a, &b);
      opposed[a][b] = opposed[b][a] = 1;
    }
    int element[MAXN]; int n = 0;
    int N; scanf("%d", &N);
    for (int i = 0; i < N; ++i) {
      char a; scanf(" %c", &a);
      element[n++] = a;
      if (n > 1 && combine[element[n - 1]][element[n - 2]]) {
        element[n - 2] = combine[element[n - 1]][element[n - 2]];
        n--;
      }
      for (int j = 0; j < n - 1; ++j) 
        if (opposed[element[n - 1]][element[j]])
          n = 0;
    }
    printf("Case #%d: ", t);
    printf("[");
    for (int i = 0; i < n; ++i) {
      if (i) printf(", ");
      printf("%c", element[i]);
    }
    printf("]\n");
  }
  return 0;
}
