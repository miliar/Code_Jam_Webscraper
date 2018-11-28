#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
using namespace std;
static const double EPS = 1e-5;
typedef long long ll;

char new_table[105][105];
int N, K;

bool checkK(char color, int r_now, int c_now) {
  // upper-right
  int k;
  for (k = 1; ; ++k) {
    if (r_now-k < 1 || c_now+k > N) break;
    if (new_table[r_now-k][c_now+k] != color) break;
  }
  if (k == K) return true;

  // right
  for (k = 0; ; ++k) {
    if (c_now+k > N) break;
    if (new_table[r_now][c_now+k] != color) break;
  }
  if (k == K) return true;

  // down-right
  for (k = 0; ; ++k) {
    if (r_now+k > N || c_now+k > N) break;
    if (new_table[r_now+k][c_now+k] != color) break;
  }
  if (k == K) return true;
  
  // down
  for (k = 0; ; ++k) {
    if (r_now+k > N) break;
    if (new_table[r_now+k][c_now] != color) break;
  }
  if (k == K) return true;

  return false;
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cin >> N >> K;
    char table[N+2][N+2];
    for (int r = 1; r <= N; ++r) {
      cin >> table[r]+1;
    }

    for (int r = 1; r <= N; ++r) {
      int c_pos = N;
      for (int c = N; c >= 1; --c) {
	if (table[r][c] != '.') {
	  new_table[r][c_pos] = table[r][c];
	  --c_pos;
	}
      }
      for ( ; c_pos >= 1; --c_pos) {
	new_table[r][c_pos] = '.';
      }
    }

    bool red = false, blue = false;
    for (int c = 1; c <= N; ++c) {
      for (int r = 1; r <= N; ++r) {
	if (red && blue) break;
	if (new_table[r][c] == '.') continue;
	else if (new_table[r][c] == 'R' && !red) red = checkK(new_table[r][c], r, c);
	else if (new_table[r][c] == 'B' && !blue) blue = checkK(new_table[r][c], r, c);
      }
      if (red && blue) break;
    }
    cout << "Case #" << t << ": ";
    if (red && blue) cout << "Both" << endl;
    else if (red) cout << "Red" << endl;
    else if (blue) cout << "Blue" << endl;
    else cout << "Neither" << endl;
  }
}
