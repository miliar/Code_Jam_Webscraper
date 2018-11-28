#include <iostream>
using namespace std;

int testcase;
int n;

int main(int argc, char *argv[]) {
  cin >> testcase;
  for (int tn = 1; tn < testcase+1; ++tn) {
    cin >> n;
    int x = 0;
    int minvalue = 2100000000;
    int sum = 0;
    for (int i = 0; i < n; ++i) {
      int temp;
      cin >> temp;
      sum += temp;
      minvalue = min(minvalue, temp);
      x = x ^ temp;
    }
    cout << "Case #" << tn << ": ";
    if (x == 0) {
      cout << sum - minvalue << endl;
    } else {
      cout << "NO" << endl;
    }
  }
  return 0;
}
