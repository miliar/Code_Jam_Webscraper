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

const int MAXN = 110;

char mat[MAXN][MAXN];
int opponents[MAXN], won[MAXN];
double wp[MAXN], owp[MAXN], oowp[MAXN];

int main(void)
{
  int T; scanf("%d", &T);

  for (int t = 1; t <= T; ++t) 
  {
    int N; scanf("%d", &N);

    for (int i = 0; i < N; ++i)
      scanf("%s", mat[i]);

    for (int i = 0; i < N; ++i) {

      opponents[i] = won[i] = 0;

      for (int j = 0; j < N; ++j) {
        opponents[i] += mat[i][j] != '.';
        won[i] += mat[i][j] == '1';
      }

      wp[i] = (double) won[i] / (double) opponents[i];
    }

    for (int i = 0; i < N; ++i) {

      owp[i] = 0;

      for (int j = 0; j < N; ++j)
        if (mat[i][j] != '.') {
          int _won = won[j];
          if (mat[j][i] == '1') --_won;
          owp[i] += (double) _won / (double) (opponents[j] - 1);
        }

      owp[i] /= opponents[i];
    }

    for (int i = 0; i < N; ++i) {

      oowp[i] = 0;

      for (int j = 0; j < N; ++j)
        if (mat[i][j] != '.')
          oowp[i] += owp[j];

      oowp[i] /= opponents[i];
    }

    printf("Case #%d:\n", t);

    for (int i = 0; i < N; ++i)
      printf("%.7lf\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
  }

  return 0;
}
