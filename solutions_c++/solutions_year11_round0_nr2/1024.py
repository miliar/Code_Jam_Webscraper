#include <iostream>
#include <vector>

using namespace std;

int T,N,C,D;

char combine[256][256];
char opposed[256][256];
char buf[101];
char isBase[256];
int baseElementCount[9];
char baseElements[] = "XQUERASDF";

vector<char> list;

int main() {
  isBase['Q'] = 1;
  isBase['W'] = 2;
  isBase['E'] = 3;
  isBase['R'] = 4;
  isBase['A'] = 5;
  isBase['S'] = 6;
  isBase['D'] = 7;
  isBase['F'] = 8;

  cin >> T;
  for (int t = 1; t <= T; ++t) {
    // Reset everything
    list.clear();
    for (int i = 0; i < 256; ++i) {
      for (int j = 0; j < 256; ++j) {
        combine[i][j] = 0;
        opposed[i][j] = 0;
      }
    }

    for (int i = 0; i < 9; ++i) {
      baseElementCount[i] = 0;
    }

    // Read in the input
    cin >> C;
    for (int i = 0; i < C; ++i) {
      cin >> buf;
      combine[buf[0]][buf[1]] = buf[2];
      combine[buf[1]][buf[0]] = buf[2];
    }

    cin >> D;
    for (int i = 0; i < D; ++i) {
      cin >> buf;
      opposed[buf[0]][buf[1]] = 1;
      opposed[buf[1]][buf[0]] = 1;
    }

    cin >> N;
    cin >> buf;

    for (int i = 0; i < N; ++i) {
      char cur = buf[i];
      int sz = list.size();
      if (sz > 0) {
        // Check to see if there is a combining possible
        if (combine[list.back()][cur]) {
          char newElement = combine[list.back()][cur];
          --baseElementCount[isBase[list.back()]];
          list.pop_back();
          list.push_back(newElement);
        } else {
          int j;
          for (j = 1; j <= 9; ++j) {
            if (baseElementCount[j] > 0 && opposed[cur][baseElements[j]]) {
              list.clear();
              for (int k = 0; k < 9; ++k) {
                baseElementCount[k] = 0;
              }
              break;
            }
          }
          if (j > 9) {
            list.push_back(cur);
            ++baseElementCount[isBase[cur]];
          }
        }
      } else {
        list.push_back(cur);
        ++baseElementCount[isBase[cur]];
      }
    }
    cout << "Case #" << t << ": [";
    for (int i = 0; i < list.size(); ++i) {
      cout << list[i];
      if (i < list.size() - 1) {
        cout << ", ";
      }
    }
    cout << "]" << endl;
  }
}
