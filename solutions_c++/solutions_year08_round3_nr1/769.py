#include <iostream>
using namespace std;

int main() {
  int N;
  cin >> N;
  for (int iii = 0; iii < N; iii++) {
    int P, K, L;
    cin >> P >> K >> L;
    int a[L];
    for (int i = 0; i < L; i++) {
      cin >> a[i];
    }
    sort(a, a+L, greater<int>() );
    int ans = 0;
    for (int i = 0; i < L; i++) {
      ans += a[i] * ((int)(i/K) + 1);
    }
    cout << "Case #" << iii+1 << ": " << ans << endl;
  }
}
