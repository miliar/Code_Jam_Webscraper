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

const int MAXN = 55;

int R, C;
char mat[MAXN][MAXN];

int main(void)
{
  int T; scanf("%d", &T);

  for (int t = 1; t <= T; ++t) 
  {
    scanf("%d %d", &R, &C);
    for (int i = 0; i < R; ++i)
      scanf("%s", mat[i]);

    for (int i = 0; i < R - 1; ++i)
      for (int j = 0; j < C - 1; ++j)
        if (mat[i][j] == '#' && mat[i][j + 1] == '#' &&
            mat[i + 1][j] == '#' && mat[i + 1][j + 1] == '#') {
          mat[i][j] = '/';
          mat[i][j + 1] = '\\';
          mat[i + 1][j] = '\\';
          mat[i + 1][j + 1] = '/';
        }


    int possible = 1;
    for (int i = 0; i < R; ++i)
      for (int j = 0; j < C; ++j)
        if (mat[i][j] == '#') 
          possible = 0;

    printf("Case #%d:\n", t);
    if (!possible) 
      puts("Impossible");
    else {
      for (int i = 0; i < R; ++i)
        puts(mat[i]);
    }
  }

  return 0;
}
