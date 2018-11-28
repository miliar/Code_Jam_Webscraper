#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <string>
#include <algorithm>

#define FOREACH(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define REP(i, n) for(int i = 0; i < (n); i++)
#define CLEAR(a) memset(a, 0, sizeof(a))

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int C = 1; C <= T; C++) {
    int n, k;
    cin >> n >> k;
    int w = (1<<n)-1;
    cout << "Case #" << C << ": " << (((w&k) == w) ? "ON" : "OFF") << endl;
  }
}
