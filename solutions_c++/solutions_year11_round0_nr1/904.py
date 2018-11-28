#include <iostream>
using namespace std;

int T, N;
int dp[2];
int buf[2];
int total;
int nCase;

int main() {
  FILE *file = freopen("A-large.in", "r", stdin);
  FILE *file2 = freopen("A-large.out", "w", stdout);
  cin >> N;
  nCase = 1;
  while (N--) {
    dp[0] = dp[1] = 1;
    buf[0] = buf[1] = 0;
    total = 0;
    cin >> T;
    char c[10];
    int s;
    while (T--) {
      cin >> c >> s;
      int step = 0;
      if (c[0] == 'O') {
        step = abs(s - dp[0]);
        if (step > buf[0]) {
          step -= buf[0];
        } else {
          step = 0;
        }
        ++step;
        total += step;
        buf[1] += step;
        buf[0] = 0;
        dp[0] = s;
      } else {
        step = abs(s - dp[1]);
        if (step > buf[1]) {
          step -= buf[1];
        } else {
          step = 0;
        }
        ++step;
        total += step;
        buf[0] += step;
        buf[1] = 0;
        dp[1] = s;
      }
    }
    cout << "Case #" << nCase++ << ": " << total << endl;
  }
}
