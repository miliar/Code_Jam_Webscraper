#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool checkCompat(int stockLines[16][25], int i, int j, int k) {
  if (stockLines[i][0] > stockLines[j][0]) swap(i, j);
  for (int p = 0; p < k; ++p)
    if (stockLines[i][p] >= stockLines[j][p]) return false;
  return true;
  }

bool compatGroup(bool compat[16][16], int M, int k) {
  vector<int> membs;
  int p = 0;
  while (M) {
    if (M & 1) membs.push_back(p);
    M >>= 1; ++p;
    }
  int S = membs.size();
  for (int i = 0; i < S; ++i)
    for (int j = i+1; j < S; ++j)
      if (!compat[membs[i]][membs[j]]) return false;
  return true;
  }

int main() {
  int T; cin >> T;
  for (int cc = 1; cc <= T; ++cc) {
    int n, k; cin >> n >> k;
    int stockLines[16][25];
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < k; ++j)
        cin >> stockLines[i][j];
    bool compat[16][16] = {false};
    for (int i = 0; i < n; ++i)
      for (int j = i+1; j < n; ++j)
        compat[i][j] = compat[j][i] = checkCompat(stockLines, i, j, k);
    bool compG[1 << 16] = {false};
    for (int i = 0; i < (1 << n); ++i)
      compG[i] = compatGroup(compat, i, k);
    int minG[1 << 16];
    for (int i = 0; i < (1 << n); ++i) {
      if (compG[i]) minG[i] = 1;
      else {
        minG[i] = n;
        for (int j = 1; 2*j < i; ++j)
          if (((j & i) == j) && compG[j]) {
            int t = 1 + minG[i^j];
            if (t < minG[i]) minG[i] = t;
            }
        }
      }
    cout << "Case #" << cc << ": " << minG[(1 << n)-1] << endl;
    }
  }