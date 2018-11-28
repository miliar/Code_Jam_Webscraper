
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <set>

using namespace std;

int main() {
  int T; 
  cin >> T;
  for (int i=0; i<T; ++i) {
    int N, S, p;
    cin >> N >> S >> p;

    int high_edge = 3 * (p-1);
    int low_edge = high_edge - 1;
    // Deal with outliers.
    high_edge = high_edge > 0 ? high_edge : 0;
    low_edge = low_edge > 0 ? low_edge : 0;

    int total = 0;
    for (int j=0; j<N; ++j) {
      int score;
      cin >> score;
      if (p == 0) {
        // Special case, cutoff is zero: everyone wins.
        ++total;
      } else if (score == 0) {
        // Special case, no score (and cutoff nonzero): lose.
        continue;
      } else if (score > high_edge) {
        // Score above the edge case: win.
        ++total;
      } else if (S > 0 && score >= low_edge) {
        // Score is edge case. If we can spend a surprise: win.
        --S;
        ++total;
      }
    }
    cout << "Case #" << i+1 << ": " << total << endl;
  }
  return 0;
}

