#include <iostream>

#define NMAX 1000
#define BMAX 20

using namespace std;

int T, N;
int candy[BMAX];

int main() {
  cin >> T;
  for (int t = 0; t < T; ++t) {
    // Clear data
    for (int j = 0; j < BMAX; ++j) {
      candy[j] = 0;
    }
    
    // Read data
    cin >> N;
    int total = 0;
    int min = -1;
    for (int i = 0; i < N; ++i) {
      int temp;
      cin >> temp;
      if (min == -1 || min > temp) {
        min = temp;
      }
      total += temp;
      for (int j = 0; j < BMAX; ++j) {
        if ((1<<j) & temp) {
          candy[j] += 1;
        }
      }
    }

    // Run through the bits
    bool encounteredInconsistency = false;
    for (int i = 0; i < BMAX; ++i) {
      if (candy[i] % 2 != 0) {
        encounteredInconsistency = true;
        break;
      }
    }

    if (encounteredInconsistency) {
      cout << "Case #" << (t+1) << ": NO" << endl;
    } else {
      cout << "Case #" << (t+1) << ": " << (total - min) << endl;
    }
  }
}
