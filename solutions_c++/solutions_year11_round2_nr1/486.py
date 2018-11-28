#include <algorithm>
#include <cassert>
#include <string>
#include <vector>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cctype>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <list>
#include <functional>
#include <numeric>
#include <bitset>
#include <ext/hash_set>
#include <ext/hash_map>
#include <stdexcept>
using namespace std;

bool won[128][128], played[128][128];
double numwon[128], numplayed[128], wp[128], owp[128], oowp[128];

int main() {
  int cases;
  scanf("%i", &cases);
  for (int numcase = 1; numcase <= cases; ++numcase) {
    printf("Case #%i:\n", numcase);
    int n;
    scanf("%i", &n);

    fill(&numplayed[0], &numplayed[n], 0);
    fill(&numwon[0], &numwon[n], 0);
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j) {
        char c; scanf(" %c", &c);
        won[i][j] = (c == '1');
        played[i][j] = (c != '.');
        if (won[i][j]) ++numwon[i];
        if (played[i][j]) ++numplayed[i];
      }
    for (int i = 0; i < n; ++i)
      wp[i] = numwon[i] / numplayed[i];
    for (int i = 0; i < n; ++i) {
      owp[i] = 0;
      for (int j = 0; j < n; ++j) if (played[i][j]) {
        owp[i] += (numwon[j] - won[j][i]) / (numplayed[j] - 1);
      }
      owp[i] /= numplayed[i];
    }
    for (int i = 0; i < n; ++i) {
      oowp[i] = 0;
      for (int j = 0; j < n; ++j) if (played[i][j])
        oowp[i] += owp[j];
      oowp[i] /= numplayed[i];
    }

    for (int i = 0; i < n; ++i)
      printf("%.10lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
  }
  return 0;
}
