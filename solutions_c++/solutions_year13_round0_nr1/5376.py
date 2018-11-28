/*
 *
 * File:   ATicTacToeTomek.cpp
 * Author: Andy Y.F. Huang
 * Created on April 12, 2013, 7:07 PM
 */

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <complex>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <valarray>
#include <vector>

#ifdef AZN
#include "Azn.cpp"
#endif

using namespace std;

namespace ATicTacToeTomek {
#define SIZE 4
char grid[11][11];

char win() {
  for (int r = 1; r <= SIZE; r++)
    if (grid[r][1] != '.' && grid[r][1] == grid[r][2] && grid[r][2] == grid[r][3] && grid[r][3] == grid[r][4])
      return grid[r][1];
  for (int c = 1; c <= SIZE; c++)
    if (grid[1][c] != '.' && grid[1][c] == grid[2][c] && grid[2][c] == grid[3][c] && grid[3][c] == grid[4][c])
      return grid[1][c];
  if (grid[1][1] != '.' && grid[1][1] == grid[2][2] && grid[2][2] == grid[3][3] && grid[3][3] == grid[4][4])
    return grid[1][1];
  if (grid[1][4] != '.' && grid[1][4] == grid[2][3] && grid[2][3] == grid[3][2] && grid[3][2] == grid[4][1])
    return grid[1][4];
  return '?';
}

void solve(int test_num) {
  int tr, tc, empty = 0;
  memset(grid, '.', sizeof (grid));
  for (int r = 1; r <= SIZE; r++) {
    scanf("%s", grid[r] + 1);
    grid[r][SIZE + 1] = '.';
    for (int c = 1; c <= SIZE; c++)
      if (grid[r][c] == 'T')
        tr = r, tc = c;
    empty += count(grid[r] + 1, grid[r] + SIZE + 1, '.');
  }
  grid[tr][tc] = 'X';
  char winner = win();
  printf("Case #%d: ", test_num);
  if (winner != '?') {
    printf("%c won\n", winner);
    return;
  }
  grid[tr][tc] = 'O';
  winner = win();
  if (winner != '?') {
    printf("%c won\n", winner);
    return;
  }
  if (empty == 0) puts("Draw");
  else puts("Game has not completed");
}

void solve() {
  #ifdef AZN
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  freopen("azn.txt", "w", stderr);
  #endif
  int tests;
  scanf("%d", &tests);
  for (int i = 1; i <= tests; i++)
    solve(i);
}
}

int main() {
  ATicTacToeTomek::solve();
  return 0;
}

