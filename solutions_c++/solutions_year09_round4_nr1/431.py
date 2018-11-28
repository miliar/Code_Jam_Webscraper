#include <iostream>
#include <string>
#include <utility>

using namespace std;

struct matRow {
  string row; int last;
  };

int main() {
  int T; cin >> T;
  for (int cc = 1; cc <= T; ++cc) {
    int N; cin >> N;
    matRow matrix[40];
    for (int i = 0; i < N; ++i) {
      cin >> matrix[i].row;
      matrix[i].last = N-1;
      while ((matrix[i].last > 0) && (matrix[i].row[matrix[i].last] == '0')) --matrix[i].last;
      }
    int swaps = 0;
    for (int i = 0; i < N; ++i) {
      int j = i;
      while (matrix[j].last > i) ++j;
      while (j > i) {
        swap(matrix[j], matrix[j-1]); ++swaps;
        --j;
        }
      }
    cout << "Case #" << cc << ": " << swaps << endl;
    }
  }