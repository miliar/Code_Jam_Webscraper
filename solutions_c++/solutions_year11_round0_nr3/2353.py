#include <iostream>
#include <vector>
using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int Ti = 1; Ti <= T; Ti++) {
    int N;
    cin >> N;
    vector<int> candy(N);
    for (int i = 0; i < N; i++) {
      cin >> candy[i];
    }

    int ans = 0;
    for (int i = 0; i < N; i++) {
      int s = 0, t = 0;
      for (int j = 0; j < N; j++) {
        if (i != j) {
          s ^= candy[j];
          t += candy[j];
        }
      }
      if (s == candy[i]) {
        ans = max(ans, t);
      }
    }
    cout << "Case #" << Ti << ": ";
    if (ans == 0) {
      cout << "NO";
    } else {
      cout << ans;
    }
    cout << endl;
  }
  return 0;
}
