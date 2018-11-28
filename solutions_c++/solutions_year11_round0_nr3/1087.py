#include<iostream>
#include<stdlib.h>
#include<climits>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    int N, sum = 0, xor_sum = 0, min = INT_MAX;
    cin >> N;
    while (N--) {
      int C;
      cin >> C;
      sum += C;
      xor_sum ^= C;
      min = C < min ? C : min;
    }
    cout << "Case #" << t + 1 << ": "; 
    if (xor_sum != 0) {
      cout << "NO" << endl;
    } else {
      cout << sum - min << endl;
    }
    
  } 
 
  return 0;
}
