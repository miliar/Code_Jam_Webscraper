#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

const int MAX_N = 64;

ll c[MAX_N][MAX_N];

double expected(int n, int k)
{
	vector<double> exp(n + 1);
	exp[n] = 0;
	for (int i = n - 1; i >= 0; --i) {
		ll a = c[n][k] - c[i][k];
		double b = c[n][k];
		for (int j = i + 1; j <= n && j <= i + k; ++j) 
			b += exp[j] * c[n - i][j - i] * c[i][k - (j - i)];
		exp[i] = b / a;
	}
	return exp[0];
}

int main()
{
	memset(c, 0, sizeof(c));
	c[0][0] = 1;
	for (int i = 1; i < MAX_N; ++i) {
		c[i][0] = 1;
		for (int j = 1; j < MAX_N; ++j) 
			c[i][j] = c[i - 1][j] + c[i - 1][j - 1];
	}
	
	int T;
	cin >> T;
	for (int ncases = 1; ncases <= T; ++ncases) {
		int n;
		int k;
		cin >> n >> k;
		printf("Case #%d: %.7f\n", ncases, expected(n, k));
	}
	
	return 0;
}
