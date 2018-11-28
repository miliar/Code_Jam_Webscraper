#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main(/*unsigned long long argc, char **argv*/) {
  unsigned long long nb_test = 0;
  cin >> nb_test;
  for (unsigned long long test_i=1; test_i<=nb_test; test_i++) {
    // For each test case
    int result = 0;
    int nb_candies = 0;
    cin >> nb_candies;
    unsigned long long *tab_candies = new unsigned long long[nb_candies];
    for (int ci=0; ci<nb_candies; ci++) {
      cin >> tab_candies[ci];
      //cout << tab_candies[ci] << endl;
    }
    int sumXor = tab_candies[0];
    for (int ci=1; ci<nb_candies; ci++) {
      sumXor ^= tab_candies[ci];
    }
    if (sumXor != 0) {
      cout << "Case #" << test_i << ": NO" << endl;
    } else { // find the best split
      // Find min
      unsigned long long min=tab_candies[0];
      unsigned long long sum=0;
      for (int ci=0; ci<nb_candies; ci++) {
        if (tab_candies[ci]<min) {
          min = tab_candies[ci];
        }
        sum += tab_candies[ci];
      }
      result = sum - min;
      /*
      cout << "MAX : " << max << endl;
      // Get its most significant bit
      cout << "log2: " << log2(max) << endl;
      unsigned long long bitmask = 1 << int(log2(max));
      cout << "mask:" << bitmask << endl;
      for (int ci=0; ci<nb_candies; ci++) {
        if (tab_candies[ci] >= bitmask) {
          result += tab_candies[ci];
          //cout << tab_candies[ci] << endl;
          //cout << result << endl;
        }
      }*/
      cout << "Case #" << test_i << ": ";
      cout << result;
      cout << endl;
    }
  }

  return 0;
}
