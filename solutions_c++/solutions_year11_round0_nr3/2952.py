#include <iostream>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <map>
#include <vector>
#include <set>

using namespace std;

#define PI acos(-1.)
#define EPS 1e-7
#define LL long long



int main() {
  // Declare members
  uint32_t num_case;
  cin >> num_case;

  for (int j = 1; j <= num_case; j++) {
    // Init members
    int num;

    cin >> num;
    vector<int> vals(num);


    LL min = pow(10, 6);
    LL item;
    LL sum = 0;
    LL sum_real = 0;
    for (int i = 0; i < num; i++) {
      cin >> item;
      sum ^= item;
      sum_real += item;
      if (item < min) min = item;
    }

    if (sum != 0) {
      cout << "Case #" << j << ": " << "NO" << endl;
    } else {
      cout << "Case #" << j << ": " << sum_real - min << endl;
    }
  }

  return 0;
}
