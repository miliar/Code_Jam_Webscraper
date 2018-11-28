#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int t = 1; t < T+1; ++t) {
    int N;
    cin >> N;

    int flag = 0;
    vector<int> candy(N);
    for (int i = 0; i < N; ++i) {
      cin >> candy[i];
      flag ^= candy[i];
    }

    cout << "Case #" << t << ": ";
    if (flag) {
      cout << "NO" << endl;
    } else {
      cout << accumulate(candy.begin(), candy.end(), -(*min_element(candy.begin(), candy.end()))) << endl;
    }

  }
  return 0;
}
