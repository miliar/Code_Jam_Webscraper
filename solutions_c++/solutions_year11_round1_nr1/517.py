#include <iostream>
#include <stdio.h>
using namespace std;

int T, nCase;
long long N;
int Pd, Pg;

int main() {
  FILE *file = freopen("A-large.in", "r", stdin);
  FILE *file2 = freopen("A-large.out", "w", stdout);
  nCase = 1;
  cin >> T;
  while (T--) {
    cin >> N >> Pd >> Pg;
    cout << "Case #" << nCase++ << ": ";
    bool flag = false;
    for (int i = 1; i <= N && i <= 100; i++) {
      int tmp = i * Pd;
      if (tmp % 100 == 0) {
        flag = true;
        break;
      }
    }
    if (!flag) {
      cout << "Broken" << endl;
      continue;
    }
    if (Pg == 0 && Pd > 0) {
      cout << "Broken" << endl;
      continue;
    }
    if (Pg == 100 && Pd < 100) {
      cout << "Broken" << endl;
      continue;
    }
    cout << "Possible" << endl;
  }
}
