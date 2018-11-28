#include <iostream>
#include <queue>

using namespace std;

int main() {
  int T;
  cin >> T;
  int r, n, k, t, s;
  for (int test = 1; test <= T; test++) {
    cin >> r >> k >> n;
    queue<int> q;
    for (int i = 0; i < n; i++) {
      cin >> t;
      q.push(t);
    }
    s = 0;
    while (r--) {
      t = 0;
      for (int i = 0; i < n; i++) {
        int p = q.front();
        if (t + p > k) {
          break;
        }
        t += p;
        q.pop();
        q.push(p);
      }
      s += t;
    }
    cout << "Case #" << test << ": " << s << endl;
  }
  return 0;
}
