#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <assert.h>
using namespace std;
int T, N, K;
string board[51], rboard[51], ans[2][2];
void rotate() {
  for (int i = 0; i < N; ++i)
    for (int j = 0; j < N; ++j)
      rboard[i][j] = board[N-1-j][i];
  for (int j = 0; j < N; ++j) {
    int bottom = N-1;
    for (int i = N-1; i >= 0; --i) {
      if (rboard[i][j] != '.') {
	if (i == bottom) {
	  bottom--;
	  continue;
	}
	rboard[bottom--][j] = rboard[i][j];
	rboard[i][j] = '.';
      }
    }
  }
}
bool checkwin(char c) {
  for (int i = 0; i < N; ++i)
    for (int j = 0; j + K - 1 < N; ++j) {
      int bad = false;
      for (int k = 0; k < K; ++k)
	if (rboard[i][j+k] != c) {
	  bad = true;
	  break;
	}
      if (!bad)
	return true;
    }
  for (int j = 0; j < N; ++j)
    for (int i = 0; i + K - 1 < N; ++i) {
      int bad = false;
      for (int k = 0; k < K; ++k)
	if (rboard[i+k][j] != c) {
	  bad = true;
	  break;
	}
      if (!bad)
	return true;
    }
  for (int i = 0; i + K - 1 < N; ++i)
    for (int j = 0; j + K - 1 < N; ++j) {
      int bad = false;
      for (int k = 0; k < K; ++k)
	if (rboard[i+k][j+k] != c) {
	  bad = true;
	  break;
	}
      if (!bad)
	return true;
    }
  for (int i = 0; i + K - 1 < N; ++i)
    for (int j = N-1; j - K + 1 >= 0; --j) {
      int bad = false;
      for (int k = 0; k < K; ++k)
	if (rboard[i+k][j-k] != c) {
	  bad = true;
	  break;
	}
      if (!bad)
	return true;
    }
  return false;
}
int main() {
  cin >> T;
  ans[0][1] = "Red", ans[1][0] = "Blue", ans[1][1] = "Both", ans[0][0] = "Neither";
  for (int rr = 1; rr <= T; ++rr) {
    cin >> N >> K;
    int bwin = 0, rwin = 0;
    for (int i = 0; i < N; ++i) {
      cin >> board[i];
      rboard[i] = string(N, '.');
    }
    rotate();
    bwin = checkwin('B'), rwin = checkwin('R');
    cout << "Case #" << rr << ": " << ans[bwin][rwin] << endl;
  }
  return 0;
}
