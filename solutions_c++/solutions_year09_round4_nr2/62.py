#include <string>
#include <vector>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <numeric>
#include <complex>

using namespace std;

const int INF = 1000000;
int best[50][50][50];
vector <string> grid;

int R, C, F;

bool open(int i, int j, int k, int x) {
  if (x < 0 || x >= C) return false;
  if (grid[i][x] == '#' && !(min(j, k) <= x && x <= max(j, k))) return false;
  return true;
}

bool can_go(int i, int j, int k, int x) {
  if (!open(i, j, k, x)) return false;
  if (grid[i+1][x] == '.') return false;
  return true;
}

int fall(int i, int x) {
  int fall_dist = 1;
  while (i+1 < R && grid[i+1][x] == '.') {
    i++;
    fall_dist++;
  }
  if (fall_dist > F) return -1;
  return i;
}

void just_fall(int i, int j, int k, int x, int cur_dig) {
  if (open(i, j, k, x)) {
    //cout << "just fall: " << i << " " << j << " " << k << " " << x << endl;
    int i2 = fall(i+1, x);
    if (i2 != -1)
      best[i2][x][x] <?= cur_dig;
  }
}

void dig_fall(int i2, int j2, int k2, int cur_dig) {
  int i3 = fall(i2, j2);
  if (i3 == i2)
    best[i2][j2][k2] <?= cur_dig;
  else if (i3 != -1)
    best[i3][j2][j2] <?= cur_dig;
}

int main(void)
{
  int N; cin >> N;
  for (int c = 1; c <= N; c++) {
    cin >> R >> C >> F;
    grid.resize(R);
    for (int i = 0; i < R; i++)
      cin >> grid[i];
    for (int i = 0; i < R; i++)
      for (int j = 0; j < C; j++)
	for (int k = 0; k < C; k++)
	  best[i][j][k] = INF;
    best[0][0][0] = 0;
    for (int i = 0; i < R-1; i++)
      for (int j = 0; j < C; j++)
	for (int k = 0; k < C; k++)
	  if (best[i][j][k] != INF) {
	    //cout << i << " " << j << " " << k << " " << best[i][j][k] << endl;
	    int cur_dig = best[i][j][k];
	    int left = j, right = j;
	    while (can_go(i, j, k, left))
	      left--;
	    left++;
	    while (can_go(i, j, k, right))
	      right++;
	    right--;
	    //cout << left << " " << right << endl;
	    // just fall off
	    just_fall(i, j, k, left-1, cur_dig);
	    just_fall(i, j, k, right+1, cur_dig);
	    // dig
	    for (int j2 = left; j2 <= right; j2++)
	      for (int k2 = j2; k2 <= right; k2++) {
		if (j2 != left) // fall into j2
		  dig_fall(i+1, j2, k2, cur_dig + k2-j2+1);
		if (k2 != right) // fall into k2
		  dig_fall(i+1, k2, j2, cur_dig + k2-j2+1);
	      }
	  }
    int ans = INF;
    for (int j = 0; j < C; j++)
      for (int k = 0; k < C; k++)
	ans <?= best[R-1][j][k];
    if (ans == INF)
      printf("Case #%d: No\n", c);
    else
      printf("Case #%d: Yes %d\n", c, ans);
  }
  return 0;
}
