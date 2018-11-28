#include <iostream>
#include <cstring>

using namespace std;

const int N = 1000;
int g[N];
bool known[N];
int last[N];
unsigned long long gain[N];

unsigned long long go(int R, int k, int n) {
  memset(known, false, sizeof(known));

  int curr = 0;
  int r = 0;
  unsigned long long res = 0;
  while (r < R) {
    if (known[curr]) {
      int cycleSize = r - last[curr];
      unsigned long long cycleGain = res - gain[curr];

      int rem = R - r;
      int cycles = rem / cycleSize;
      res += cycles * cycleGain;
      r += cycles * cycleSize;
      if (r == R) return res;

      memset(known, false, sizeof(known));
    }

    known[curr] = true;
    last[curr] = r;
    gain[curr] = res;

    int lastPos = curr;
    int cap = k;
    while (true) {
      if (cap >= g[curr]) {
        cap -= g[curr];
        res += g[curr];
        curr++;
        if (curr == n) curr = 0;
      } else break;
      if (lastPos == curr) break;
    }
    r++;
  }
  return res;
}

int main() {
  int t; cin >> t;
  for (int caseNo = 1; caseNo <= t; caseNo++) {
    int R, k, n; cin >> R >> k >> n;
    for (int i = 0; i < n; i++) cin >> g[i];

    cout << "Case #" << caseNo << ": " << go(R, k, n) << endl;
  }
  return 0;
}

