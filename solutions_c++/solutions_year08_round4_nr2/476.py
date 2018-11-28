#include <string>
#include <vector>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <numeric>
#include <complex>

using namespace std;

char isprod[10001];
int divisor[10001];

int main(void)
{
  int C;
  cin >> C;
  /*
  for (int x = 0; x <= 100; x++)
    for (int y = x; y <= 100; y++)
      divisor[x*y] = x;
  */
  cerr << "done" << endl;
  for (int c = 1; c <= C; c++) {
    memset(isprod, 0, sizeof(isprod));
    int N, M, A;
    cin >> N >> M >> A;
    int n = min(N, M), m = max(N, M);
    for (int x = 0; x <= n; x++)
      for (int y = x; y <= m; y++) {
	int p = x*y;
	isprod[p] = 1;
	divisor[p] = x;
      }
    int x1 = -1, y1, x2, y2;
    int NM = N*M;
    for (int p = 0; ; p++) {
      int P = p+A;
      if (P > NM) break;
      if (isprod[p] && isprod[P]) {
	x1 = divisor[p]; y2 = p > 0 ? p/x1 : 0;
	if (x1 > N || y2 > M) swap(x1, y2);
	x2 = divisor[P]; y1 = P/x2;
	if (x2 > N || y1 > M) swap(x2, y1);
	break;
      }
    }
    if (x1 >= 0)
      printf("Case #%d: 0 0 %d %d %d %d\n", c, x1, y1, x2, y2);
    else
      printf("Case #%d: IMPOSSIBLE\n", c);
  }
}
