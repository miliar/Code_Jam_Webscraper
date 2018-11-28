#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; i ++) {
    int N;
    cin >> N;
    int value[N];

    for (int i = 0; i < N; i ++)
      cin >> value[i];

    int sum = 0;
    int total = 0;
    for (int i = 0; i < N; i ++) {
      sum ^= value[i];
      total += value[i];
    }

    cout << "Case #" << i + 1 << ": ";
    if (sum != 0) {
      cout << "NO" << endl;
    } else {
      vector<int> v;
      for (int i = 0; i < N; i ++) {
	v.push_back(value[i]);
      }
      sort(v.begin(), v.end());
      cout << total - v[0] << endl;
    }

  }

  return 0;
}
