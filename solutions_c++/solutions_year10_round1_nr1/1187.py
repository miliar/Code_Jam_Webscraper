#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <fstream>
#include <cstring>
#include <numeric>

using namespace std;

vector <string> rightGravity(vector <string> box) {
  vector <string> ret(box.size(), string (box[0].size(), '.'));
  int i, j, n = box.size(), m = box[0].size();

  for (i=0; i<n; i++) {
    string line;
    for (j=0; j<m; j++)
      if (box[i][j] != '.')
        line += box[i][j];
    for (j=0; j<line.size(); j++)
      ret[i][m - line.size() + j] = line[j];
  }

  return ret;
}

vector <string> rotate(vector <string> box) {
  vector <string> ret(box.size(), string (box[0].size(), '.'));
  int i, j, n = box.size(), m = box[0].size();

  for (i=0; i<n; i++)
    for (j=0; j<m; j++)
      ret[j][n - 1 - i] = box[i][j];

  return ret;
}

bool inRange(int x, int y, vector <string> &box) {
  if (0 <= x && x <= box.size() && 0 <= y && y <= box[0].size())
    return true;
  return false;
}

string solve(vector <string> box, int K) {
  string ret = "Neither";
  int i, j, k, n = box.size();
  int R[n+1][n+1][4], B[n+1][n+1][4]; // horizonal, vector, lt to rb, rt to lb
  bool redOk = false, blueOk = false;

  for (i=0; i<=n; i++)
    for (j=0; j<=n; j++)
      for (k=0; k<4; k++)
        R[i][j][k] = B[i][j][k] = 0;

  box = rightGravity(box);
  box = rotate(box);

  for (i=0; i<n; i++)
    for (j=0; j<n; j++)
      if (box[i][j] == 'R') {
        int h = 1, v = 1, l = 1, r = 1;
        // horizonal
        if (inRange(i-1, j, box))
          h += R[i-1][j][0];
        // vertical
        if (inRange(i, j-1, box))
          v += R[i][j-1][1];
        // lt to rb
        if (inRange(i-1, j-1, box))
          l += R[i-1][j-1][2];
        // rt to lb
        if (inRange(i+1, j-1, box))
          r += R[i+1][j-1][3];
        R[i][j][0] = h, R[i][j][1] = v, R[i][j][2] = l, R[i][j][3] = r;
      } else if (box[i][j] == 'B') {
        int h = 1, v = 1, l = 1, r = 1;
        // horizonal
        if (inRange(i-1, j, box))
          h += B[i-1][j][0];
        // vertical
        if (inRange(i, j-1, box))
          v += B[i][j-1][1];
        // lt to rb
        if (inRange(i-1, j-1, box))
          l += B[i-1][j-1][2];
        // rt to lb
        if (inRange(i+1, j-1, box))
          r += B[i+1][j-1][3];
        B[i][j][0] = h, B[i][j][1] = v, B[i][j][2] = l, B[i][j][3] = r;
      }

  for (i=0; i<n; i++)
    for (j=0; j<n; j++)
      for (k=0; k<4; k++) {
        if (R[i][j][k] >= K)
          redOk = true;
        if (B[i][j][k] >= K)
          blueOk = true;
      }

  if (redOk && blueOk)
    ret = "Both";
  else if (!redOk && blueOk)
    ret = "Blue";
  else if (redOk && !blueOk)
    ret = "Red";

  return ret;
}

int main(void) {
  int probNum, i, j;

  cin >> probNum;

  for (i=0; i<probNum; i++) {
    int N, K;
    vector <string> box;
    string line;

    cin >> N >> K;
    cin.ignore();

    for (j=0; j<N; j++) {
      getline(cin, line);
      box.push_back(line);
    }

    cout << "Case #" << i + 1 << ": " << solve(box, K) << endl;
  }

  return 0;
}
