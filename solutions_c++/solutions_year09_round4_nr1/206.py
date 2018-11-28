#include <iostream>
#include <vector>
using namespace std;

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    int N; cin >> N;
    vector<int> v;
    for (int i = 0; i < N; i++) {
      string s;
      cin >> s;
      bool f = false;
      for (int j = N-1; j >= 0; j--)
        if (s[j] == '1') {
          v.push_back(j);
          f = true;
          break;
        }
      if (!f) v.push_back(0);
    }

    vector<int> vm(N, -1);
    for (int i = 0; i < N; i++)
      for (int j = 0; j < N; j++)
        if (v[j] <= i) {
          vm[j] = i;
          v[j] = 1000000;
        }
    v = vm;

    int res = 0;
    while (true) {
      int p = -1;
      for (int i = 0; i < N; i++)
        if (v[i] > i) {
          p = i;
          break;
        }

      if (p == -1) break;

      for (int j = p+1; j < N; j++)
        if (v[j] <= p) {
          // cout << "Moving " << j << " to " << cur << endl;
          for (int k = j-1; k >= p; k--) {
            int temp = v[k];
            v[k] = v[k+1];
            v[k+1] = temp;
            res++;
          }
          break;
        }
    }

    cout << "Case #" << c << ": " << res << endl;
  }
  return 0;
}
