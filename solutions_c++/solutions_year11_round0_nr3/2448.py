#include <iostream>
#include <vector>

using namespace std;

int main() {
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++) {
    int N;
    cin >> N;
    int xorsum = 0;
    int minc = 10000000;
    int sum = 0;
    for(int n = 0; n < N; n++) {
      int candy;
      cin >> candy;
      xorsum ^= candy;
      sum += candy;
      if(candy < minc)
	minc = candy;
    }
    if(xorsum) {
      cout << "Case #" << t << ": NO" << endl;
      continue;
    } else {
      cout << "Case #" << t << ": " << (sum-minc) << endl;
    }
  }

  return 0;
}
