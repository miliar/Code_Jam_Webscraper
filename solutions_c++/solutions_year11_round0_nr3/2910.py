#include <iostream>
#include <algorithm>
using namespace std;
int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    int N;
    cin >> N;
    int arr[N];
    for (int j = 0; j < N; ++j) {
      cin >> arr[j];
    }
    sort(arr, arr + N);
    int x = 0, y = arr[0], res = 0;
    for (int j = 1; j < N; ++j) {
      x ^= arr[j];
      res += arr[j];
    }
    cout << "Case #" << (i + 1) << ": ";
    if (!(x ^ y)) {
      cout << res << endl;
    } else {
      cout << "NO" << endl;
    }
  }
  return 0;
}
