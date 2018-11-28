#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main() {
	int t;
  cin >> t;
	for(int c = 1; c <= t; c++) {
    vector<string> matrix;
    for (int i = 0; i < 4; i++) {
      string s;
      cin >> s;
      matrix.push_back(s);
    }

    bool done = false;

    if (!done) {
      ostringstream os;
      for (int j = 0; j < 4; j++) {
        os << matrix[j][j];
      }

      string column = os.str();

      if ((count(column.begin(), column.end(), 'X') == 3 && count(column.begin(), column.end(), 'T') == 1) || 
        count(column.begin(), column.end(), 'X') == 4) {
        printf("Case #%d: X won", c);
        done = true;
      }
      if ((count(column.begin(), column.end(), 'O') == 3 && count(column.begin(), column.end(), 'T') == 1) || 
        count(column.begin(), column.end(), 'O') == 4) {
        printf("Case #%d: O won", c);
        done = true;
      }
    }

    for (int j = 0; j < 4; j++) {
        ostringstream os;
        for (int i = 0; i < 4; i++) {
          os << matrix[i][j];
        }

        string column = os.str();

        if ((count(column.begin(), column.end(), 'X') == 3 && count(column.begin(), column.end(), 'T') == 1) || 
          count(column.begin(), column.end(), 'X') == 4) {
          printf("Case #%d: X won", c);
          done = true;
        }
        if ((count(column.begin(), column.end(), 'O') == 3 && count(column.begin(), column.end(), 'T') == 1) || 
          count(column.begin(), column.end(), 'O') == 4) {
          printf("Case #%d: O won", c);
          done = true;
        }
    }

    if (!done) {
      ostringstream os;
      for (int j = 3; j >= 0; j--) {
        os << matrix[3 - j][j];
      }

      string column = os.str();

      if ((count(column.begin(), column.end(), 'X') == 3 && count(column.begin(), column.end(), 'T') == 1) || 
        count(column.begin(), column.end(), 'X') == 4) {
        printf("Case #%d: X won", c);
        done = true;
      }
      if ((count(column.begin(), column.end(), 'O') == 3 && count(column.begin(), column.end(), 'T') == 1) || 
        count(column.begin(), column.end(), 'O') == 4) {
        printf("Case #%d: O won", c);
        done = true;
      }
    }

    for (int i = 0; i < 4 && !done; i++) {
      string line = matrix[i];
      if ((count(line.begin(), line.end(), 'X') == 3 && count(line.begin(), line.end(), 'T') == 1) || 
        count(line.begin(), line.end(), 'X') == 4) {
        printf("Case #%d: X won", c);
        done = true;
      }
      if ((count(line.begin(), line.end(), 'O') == 3 && count(line.begin(), line.end(), 'T') == 1) || 
        count(line.begin(), line.end(), 'O') == 4) {
        printf("Case #%d: O won", c);
        done = true;
      }
    }

    if (!done) {
      bool empty = true;
      for (int i = 0; i < 4 && empty; i++) {
        for (int j = 0; j < 4 && empty; j++) {
          empty = matrix[i][j] != '.';
        }
      }

      if (empty) {
        printf("Case #%d: Draw", c);
        done = true;
      }
    }

    if (!done) {
      printf("Case #%d: Game has not completed", c);
    }

    if (c < t)
      printf("\n");
	}
	return 0;
}
