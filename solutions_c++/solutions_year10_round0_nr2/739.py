#include <iostream>
#include <vector>

using namespace std;

long long gcf(long long a, long long b) {
  if (b > a) return gcf(b, a);
  if (a % b == 0) return b;
  return gcf(b, a % b);
}

int main () {
  int C;
  cin >> C;
  for (int i = 0; i < C; ++i) {
    int N;
    cin >> N;
    vector<long long> t, dt;
    t.reserve(N);
    dt.reserve(N - 1);
    for (int j = 0; j < N; ++j) {
      long long tj;
      cin >> tj;
      t.push_back(tj);
      if (j > 0) {
        long long dtj = t[j] - t[j - 1];
        if (dtj < 0) {
          dtj *= -1;
        }
        if (dtj != 0) {
          dt.push_back(dtj);
        }
      }
    }
    long long dtgcf = dt[0];
    for (int j = 1; j < dt.size(); ++j) {
      dtgcf = gcf(dt[j], dtgcf);
    }
    if (dtgcf == 1 || t[0] % dtgcf == 0) {
      cout << "Case #" << i + 1 << ": 0" << endl;
    } else {
      long long ans = dtgcf - (t[0] % dtgcf);
      cout << "Case #" << i + 1 << ": " << ans << endl;
    }
  }
  return 0;
}
