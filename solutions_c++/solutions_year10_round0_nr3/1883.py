#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int const SIZE = 1000;
  int groups[SIZE];
  int dp[SIZE];
  int next[SIZE];

  int t;
  cin >> t;
  for (int tests = 0; tests < t; ++tests) {
    int r, k, n;
    scanf("%d %d %d", &r, &k, &n);
    long long sum = 0;
    for (int i = 0; i < n; ++i) {
      scanf("%d", &groups[i]);
      sum += groups[i];
    }
    
    long long result = 0;
    int pos = 0;
    int current = 0;
    for (int i = 0; i < n; ++i) {
      int prev = pos;
      current = 0;
      int cnt = 0;
      while (current + groups[pos] <= k && cnt < n) {
        current += groups[pos];
        ++pos;
        if (pos == n)
          pos = 0;
        ++cnt;
      }

      dp[prev] = current;
      next[prev] = pos;
      //result += current;
    }

    pos = 0;
    for (int i = 0; i < r; ++i) {
      result += dp[pos];
      pos = next[pos];
    }

    printf("Case #%d: ", tests + 1);
    cout << result << "\n";
  }

  return 0;
}