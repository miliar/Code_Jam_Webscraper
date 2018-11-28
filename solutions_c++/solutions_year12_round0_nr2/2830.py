#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(void) {
  int T = 0;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    int N = 0;
    int S = 0;
    int p = 0;
    int sum = 0;
    cin >> N;
    cin >> S;
    cin >> p;
    for (int j = 0; j < N; ++j) {
      int total;
      cin >> total;
      int min = total / 3;
      int max = total - 2 * min;
      if (max >= p) {
        if (max - min == 2) {
          if (max - 1 >= p) {
            sum++;
          }
          else if (S) {
            S--;
            sum++;
          }
        }
        else {
          sum++;
        }
      }
      else if (S && min > 0 && max == min && max + 1 >= p) {
        S--;
        sum++;
      }
    }
    cout << "Case #" << i << ": " << sum << endl;
  }
  return 0;
}
