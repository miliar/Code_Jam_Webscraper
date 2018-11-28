#include <iostream>
#include <string>
#include <cstring>
#include <cassert>
#include <algorithm>
using namespace std;

#define FOR(i, a, b) for (int i = (a), _b = (b); i < _b; ++i)
#define REP(i, n) FOR(i, 0, (n))

char c;
int n, row[100];

int find(int i) {
  FOR(ii, i, n) 
    if (row[ii] <= i) return ii;
  assert(0);
  return -1;
}

int process(int i1, int i2) {
  for (int i = i2 - 1; i >= i1; --i)
    swap(row[i], row[i + 1]);

  return i2 - i1;
}

int main() {
  int N;
  cin >> N;
  for (int C = 1; C <= N; C++) {
    memset(row, 0, sizeof row);

    cin >> n;
    REP(i, n) REP(j, n) {
      cin >> c;
      if (c == '1') row[i] = j;
    }
    
    int ans = 0;
    REP(i, n) {
      int ii = find(i);
      ans += process(i, ii);
    }
    cout << "Case #" << C << ": " << ans << endl;
  }
}
