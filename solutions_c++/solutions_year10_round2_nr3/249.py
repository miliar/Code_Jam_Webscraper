#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

#define filename "C-large"

long long mod = 100003;
long long cnt[512][512];
long long C[512][512];

int main()
{
  freopen (filename ".in", "rt", stdin);
  freopen (filename ".out", "wt", stdout);
  
  memset (C, 0, sizeof(C));
  for (int n = 0; n <= 500; ++n) {
	  C[n][0] = 1;
	  C[n][n] = 1;
	  for (int m = 1; m < n; ++m)
		  C[n][m] = (C[n-1][m-1] + C[n-1][m]) % mod;
  }

  memset (cnt, 0, sizeof(cnt));
  for (int i = 2; i <= 500; ++i) {
	  cnt[i][1] = 1;
	  for (int j = 2; j < i; ++j) {
		  int m = i - j - 1;
		  for (int k = max(2*j-i, 1); k < j; ++k) {
			  int l = j - k - 1;
			  cnt[i][j] = (cnt[i][j] + cnt[j][k] * C[m][l]) % mod;
		  }
	  }
  }

  {
	  int T, n;
	  cin >> T;
	  for (int test = 1; test <= T; ++test) {	  
		  long long ans = 0;
		  cin >> n;
		  for (int i = 1; i < n; ++i)
			  ans = (ans + cnt[n][i]) % mod;
		  cout << "Case #" << test << ": " << ans << endl;
	  }
  }

  return 0;
}