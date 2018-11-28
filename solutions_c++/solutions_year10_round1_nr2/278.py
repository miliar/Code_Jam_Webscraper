#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <cstring>
#include <cmath>

using namespace std;

int arr[100];
int dp[100][256][2][2];
bool known[100][256][2][2];

int D, I, M, N;

inline int insertCost(int target, int curr, int m) {
  return (((abs(target-curr))-1) / m) + 1;
}

int go(int idx, int last, int first, int insert) {
  if (idx == N) return 0;
  if (known[idx][last][first][insert]) return dp[idx][last][first][insert];
  known[idx][last][first][insert] = true;

  int best = 0x7fffffff;
  int curr = arr[idx];

  if (first) {
    best = min(best, go(idx+1, curr, 0, 1));
    best = min(best, D + go(idx+1, last, 1, 1));
    for (int target = 0; target <= 255; target++) {
      best = min(best, abs(target-curr) + go(idx+1, target, 0, 1));
    }
  } else {
    if (abs(curr-last) <= M) best = min(best, go(idx+1, curr, 0, 1));
    best = min(best, D + go(idx+1, last, 0, 1));
    for (int target = 0; target <= 255; target++) {
      if (M > 0 && insert) {
        best = min(best, insertCost(target, last, M) * I + go(idx, target, 0, 0));
      }
      if (abs(target-last) > M) continue;
      best = min(best, abs(target-curr) + go(idx+1, target, 0, 1));
    }
  }

  return dp[idx][last][first][insert] = best;
}

int main() {
  int cases; cin >> cases;
  for (int caseNo = 1; caseNo <= cases; caseNo++) {
    cin >> D >> I >> M >> N;
    for (int i = 0; i < N; i++) cin >> arr[i];

    memset(known, false, sizeof(known));
    cout << "Case #" << caseNo << ": " << go(0, 0, 1, 0) << endl;
  }
  return 0;
}

