#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int A[100];

int dp[300][100];
int D, I, M, N;

int diff(int a, int b) { return a < b ? b - a : a - b; }

int ins_needed(int a, int b) {
  int d = diff(a, b);
  return max(0, (d - 1) / M);
}

int solve(int last, int x) {
  if(x == N) return 0;
  int& ref = dp[last][x];
  if(ref != -1) return ref;
  ref = D + solve(last, x + 1);
  for(int i = 0; i < 256; i++) {
    if(M == 0) {
      if(i == last) ref = min(ref, diff(A[x], i) + solve(i, x + 1));
    } else {
      ref = min(ref, I * ins_needed(last, i) + diff(A[x], i) + solve(i, x + 1));
    }
  }
  return ref;
}

int main() {
  int T; cin >> T;
  for(int t = 1; t <= T; t++) {
    cin >> D >> I >> M >> N;
    for(int i = 0; i < N; i++) {
      cin >> A[i];
    }
    memset(dp, -1, sizeof(dp));
    int result = 0x7FFFFFFF;
    for(int i = 0; i < 256; i++) {
      result = min(result, solve(i, 0));
    }
    cout << "Case #" << t << ": " << result << endl;
  }
}
