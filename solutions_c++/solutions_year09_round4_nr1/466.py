#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

int main() {
  int N, T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cin >> N;
    vector<int> last;
    for (int i = 0; i < N; ++i) {
      string row;
      cin >> row;
      int lastone = -1;
      for (int j = 0; j < N; ++j) {
        if (row[j] == '1') lastone = j;
      }
      last.push_back(lastone);
    }
    int count = 0;
    for (int i = 0; i < N; ++i) {
      if (last[i] > i) {
        for (int j = i+1; j < N; ++j) {
          if (last[j] <= i) {
            for (int k = j-1; k >= i; --k, ++count) {
              int tmp = last[k];
              last[k] = last[k+1];
              last[k+1] = tmp;
            }
            break;
          }
        }
      }
    }
    printf("Case #%d: %d\n", t, count);
  }
  return 0;
}
