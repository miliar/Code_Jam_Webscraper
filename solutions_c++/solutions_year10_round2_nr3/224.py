#include <cstdio>
#include <cmath>
#include <iostream>

using namespace std;

void func();

typedef unsigned long long ull;

ull comb[510][510];
ull dp[510][510];

int main() {
  freopen("in.in", "r", stdin);
  freopen("output.out", "w", stdout);

	for (int i = 0; i < 501; i++) {
		comb[i][0] = 1;
		comb[i][i] = 1;
		for (int j = 1; j < i; j++) {
			comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % 100003;
		}
	}

	for (int i = 2; i <= 500; i++) {
		dp[i][1] = 1;
		for (int j = 2; j < i; j++) {
			dp[i][j] = 0;
			for (int k = 1; k < j; k++) {
				dp[i][j] = (dp[i][j] + dp[j][k] * comb[i-j-1][j-k-1]) % 100003;
			}
		}
	}

  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; i++) {
  	cout << "Case #" << i << ":";
  	func();
  }

  fclose(stdin);
  fclose(stdout);
}

// WRITE ALL CODE BELOW THIS

void func() {
	int n;
	scanf("%d", &n);
	ull res = 0;
	for (int i = 1; i < n; i++) {
		res = (res+dp[n][i]) % 100003;
	}
	cout << " " << res << endl;
}
