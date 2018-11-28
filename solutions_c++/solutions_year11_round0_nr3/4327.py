#include <iostream>
#include <bitset>
#include <math.h>
using namespace std;
int main() {
  int T;
  cin >> T;
  int i;
  for (i = 1; i <= T; i++) {
    int N;
    cin >> N;
    int j, arr[N];
    for (j = 0; j < N; j++) {
      cin >> arr[j];
    }
    int sum = 0;
    for (j = 0; j < N; j++) {
      sum ^= arr[j];
    }
    if (sum) {
      cout << "Case #" << i << ": " << "NO" << endl;
      continue;
    }
    int y = pow(2, N)-1;
    int k;
    int maxSum = 0;
    for (k = 1; k < y; k++) {
      bitset<1000> b(k);
      int l;
      int sum1 = 0, sum2 = 0;
      int sum3 = 0, sum4 = 0;
      for (l = 0; l < N; l++) {
        if (b[l]) {
          sum1 ^= arr[l]; 
          sum2 += arr[l];
        } else {
          sum3 ^= arr[l];
          sum4 += arr[l];
        }}
/*
      cout << b << endl;
        cout << sum1 << endl;
        cout << sum2 << endl;
        cout << sum3 << endl;
        cout << sum4 << endl;*/
      if (sum1 == sum3) {
        if (sum2 > sum4) {
          if (sum2 > maxSum)
            maxSum = sum2;
        } else {
          if (sum4 > maxSum)
            maxSum = sum4;
        }

      }
    }
    
  cout << "Case #" << i << ": " << maxSum << endl;
  }
  return 0;
}