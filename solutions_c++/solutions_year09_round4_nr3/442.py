#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;
int N, K;
int price[16][32];
bool valid[16][16];
int memo[(1 << 16)];

bool check(int a, int b) {
  if (price[a][0] == price[b][0]) return false;
  if (price[a][0] < price[b][0]) {
    int temp = a;
    a = b;
    b = temp;
  }

  // price[a][0] > price[b][0]
  for (int i = 1; i < K; ++i) {
    if (price[a][i] <= price[b][i])
      return false;
  }
  return true;
}

int backtrack(int bm, int used, int idx) {
  if (bm == 0 && used == 0) return 0;
  if (used == 0) {
    for (int i = 0; i < N; ++i) {
      if (((1 << i) & bm) != 0) {
	return backtrack(bm - (1 << i), (1 << i), i);
      }
    }
  }

  int ret = 1 + backtrack(bm, 0, 0);
  for (int i = idx+1; i < N; ++i) {
    if (((1 << i) & bm) != 0) {
      bool ok = true;
      for (int j = 0; j <= idx; ++j) {
	if ((((1 << j) & used) != 0) && !valid[i][j]) {
	  ok = false;
	  break;
	}
      }

      if (ok) {
	ret = min(ret, backtrack(bm - (1 << i), used | (1 << i), i));
      }
    }
  }
  return ret;
}

int dp(int bm) {
  if (bm == 0) return 0;
  if (memo[bm] != -1) return memo[bm];

  int ret = 10000000;
  int must = 0;
  for (int i = 0; i < N; ++i) {
    if (((1 << i) & bm) != 0) {
      must = (1 << i);
      break;
    }
  }

  for (int next = bm; next > 0; next = (bm & (next-1))) {
    if ((next & must) == 0) continue;
    bool ok = true;
    for (int i = 0; i < N && ok; ++i) {
      if (((1 << i) & next) == 0) continue;
      for (int j = i+1; j < N; ++j) {
	if (((1 << j) & next) == 0) continue;
	if (!valid[i][j]) {
	  ok = false;
	  break;
	}
      }
    }

    if (ok) {
      ret = min(ret, 1+dp(bm-next));
    }
  }
  return memo[bm] = ret;
}

int main() {
  int numcase;
  cin >> numcase;
  for (int ncase = 1; ncase <= numcase; ++ncase) {
    cin >> N >> K;
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < K; ++j) {
	cin >> price[i][j];
      }
    }

    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < N; ++j) {
	valid[i][j] = check(i, j);
      }
    }

    memset(memo, -1, sizeof(memo));
    int ans = dp((1 << N) - 1);
    // int ans = backtrack((1 << N) - 1, 0, 0);
    cout << "Case #" << ncase << ": " << ans << endl;
  }
}
