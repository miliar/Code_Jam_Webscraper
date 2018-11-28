#include <iostream>

using namespace std;

int T, N, nCase;
int num[1010];
int sum;

int main() {
  FILE *file = freopen("C-large.in", "r", stdin);
  FILE *file2 = freopen("C-large.out", "w", stdout);
  cin >> T;
  nCase = 1;
  while (T--) {
    sum = 0;
    cin >> N;
    int flag = 0;
    for (int i = 0; i < N; i++) {
      cin >> num[i];
      flag ^= num[i];
    }
    cout << "Case #" << nCase++ << ": ";
    if (flag) {
      cout << "NO" << endl;
    } else {
      sort(num, num + N);
      for (int i = 1; i < N; i++) {
        sum += num[i];
      }
      cout << sum << endl;
    }
  }
}
