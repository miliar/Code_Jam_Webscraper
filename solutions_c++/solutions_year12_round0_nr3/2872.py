#include <iostream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <vector>

using namespace std;

int main(void) {
  int T = 0;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    if (i != 1)
      cout << endl;
    int A = 0;
    int B = 0;
    int sum = 0;
    cin >> A;
    cin >> B;
    for (int j = A; j < B; ++j) {
      stringstream out;
      out << j;
      string num = out.str();
      int length = num.length();
      for (int k = 0; k < length - 1; ++k) {
        char tmp = num[length - 1];
        for (int l = length - 1; l > 0; --l)
          num[l] = num[l - 1];
        num[0] = tmp;
        int cmp = atoi(num.c_str());
        if (cmp > j && cmp <= B)
          sum++;
      }
    }
    cout << "Case #" << i << ": " << sum;
  }
  return 0;
}
