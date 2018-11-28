#include <iostream>
#include <cmath>

using namespace std;

int findNext(int num, int amount) {
  double num_digits = 0.0;
  int temp = num;
  while (temp != 0) {
    temp = temp / 10;
    num_digits++;
  }
  int x = ((int)(pow(10.00, (double)amount)));
  int digits = num % x;
  int ans = num / x;
  return digits * pow(10.00, num_digits - amount) + ans;
}

int main(int argc, char** argv) {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    int A;
    cin >> A;
    int B;
    cin >> B;
    int ans = 0;
    for (int j = A; j <=B; ++j) {
      int next = -1;
      int amount = 1;
      while (next != j) {
        next = findNext(j, amount);
        amount++;
        if (next > j && next <=B) {
          ans++;
        }
      } 
    }
    cout << "Case #" << (i+1) << ": " << ans << endl;
  }
  return 0;
}
