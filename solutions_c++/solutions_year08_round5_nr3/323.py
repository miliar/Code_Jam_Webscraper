#include <vector>
#include <list>
#include <map>
#include <set>
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

using namespace std;

int T;

bool ok[10][10];
int prof[10];
int M, N;
int data[11][1 << 11];
int res;

void foo(int thisP, int level, int pos, int profile, int cnt) {
  while ((pos < N) && (thisP & (1 << pos))) pos++;
  if (pos >= N) data[level + 1][profile] = max(data[level + 1][profile], cnt);
  else {
    int mask = 0;
    if (pos < N - 1) mask += 1 << (pos + 1);
    if (pos) mask += 1 << (pos - 1);
    int tmp = profile | mask;
    foo(thisP, level, pos + 2, tmp, cnt + 1);
    foo(thisP, level, pos + 1, profile, cnt);
  }

}

int main() {
  cin >> T;
  for (int _caseN = 1; _caseN <= T; _caseN++) {
    cin >> M >> N;
    memset(data, 0, sizeof data);
    memset(prof, 0, sizeof prof);

    for (int m = 0; m < M; m++) for (int n = 0; n < N; n++) {
      char c = 0; while (c != '.' && c != 'x') cin >> c;
      int i = (c == '.') ? 0 : 1;
      prof[M - m - 1] <<= 1; prof[M - m - 1] += i;
      ok[M - m - 1][n] = (c == '.');
    }

    res = 0;
    for (int l = 0; l < M; l++) for (int i = 0; i < (1 << N); i++)
      foo((i | prof[l]), l, 0, prof[l + 1], data[l][i]);

    for (int i = 0; i < (1 << N); i++) res = max(res, data[M][i]);

    cout << "Case #" << _caseN << ": ";
    cout << res;
    cout << endl;
  }

  return 0;
}