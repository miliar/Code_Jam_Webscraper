#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <map>
using namespace std;

int main()
{
  int N;
  cin >> N;
  for (int a = 1; a <= N; a++) {
    int p, k, l;
    cin >> p >> k >> l;

    long long freq[l];
    for (int i = 0; i < l; i++) {
      int t;
      cin >> freq[i];
    }
    sort(freq, freq+l, greater<int>());

    long long ans = 0;
    bool flag = false;
    for (int i = 0; i < l; i++) {
      ans += freq[i] * (i / k + 1);
    }

    if (flag) {
      cout << "Case #" << a << ": Impossible" << endl;
    }
    else {
      cout << "Case #" << a << ": " << ans << endl;
    }
  }

  return 0;
}
