#include <iostream>

using namespace std;

int main(void) {
  long long t;
  cin >> t;
  for (int j = 0; j < t; j++) {
    long long n, k;
    cin >> n;
    cin >> k;
    cout << "Case #" << (j+1) << ": ";
    if ((k + 1) % (1 << n) == 0)
      cout << "ON";
    else
      cout << "OFF";
    cout << endl;
  }
}
