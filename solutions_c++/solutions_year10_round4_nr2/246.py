#include <iostream>
#include <cstring>
using namespace std;
typedef long long ll;

ll C[20][1050][20], M[1050], P[20][1020];

ll dp(int r, int c, int m) {
  ll &N = C[r][c][m];
  if (N != -1) return N;
  if (!r) return M[c] >= m ? 0 : 1000000000;
  N = dp(r-1, c*2, m+1) + dp(r-1, c*2+1, m+1);
  N = min(N, P[r][c] + dp(r-1, c*2, m) + dp(r-1, c*2+1, m));
  return N;
}

int main() {
  int nt, T = 1, p;
  cin >> nt;
  while (nt-- && cin >> p) {
    for (int i = 0; i < (1<<p); ++i)
      cin >> M[i];
    for (int i = 0; i < p; ++i)
      for (int j = 0; j < (1<<(p-i-1)); ++j)
	cin >> P[i+1][j];

    memset(C, -1, sizeof C);
    cout << "Case #" << T++ << ": " << dp(p, 0, 0) << endl;
  }
}
