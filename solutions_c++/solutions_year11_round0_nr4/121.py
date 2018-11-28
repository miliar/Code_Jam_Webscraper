#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>

using namespace std;

int cycLen(vector<int> &pos, int s) {
  int len = 0;
  while (pos[s] != s) {
    ++len;
    swap(s, pos[s]);
    }
  return len;
  }

int main() {
  cout << fixed << setprecision(6);

  int T; cin >> T;
  for (int cNum = 1; cNum <= T; ++cNum) {
    int N; cin >> N;

    vector<int> perm(N);
    for (int i = 0; i < N; ++i) {
      cin >> perm[i];
      --perm[i];
      }

    vector<int> pos(N);
    for (int i = 0; i < N; ++i)
      pos[perm[i]] = i;

    double ans = 0;
    for (int i = 0; i < N; ++i)
      if (pos[i] != i)
        ans += cycLen(pos, i);

    cout << "Case #" << cNum << ": " << ans << '\n';
    }
  }
