#include <iostream>
#include <vector>
using namespace std;

#define MOD 100003LL
#define MAX 505

long long f[555][555];
long long c[555][555];

void init() {
	memset(c, 0, sizeof(c));
	c[0][0] = 1;
	for (int j = 1; j <= MAX; j++) {
		c[0][j] = c[j][j] = 1;
		for (int i = 1; i < j; i++) {
			c[i][j] = c[i - 1][j - 1] + c[i][j - 1];
			c[i][j] %= MOD;
		}
//		for (int i = 0; i <= j; i++) cout << c[i][j] << " ";
//		cout << endl;
	}

	memset(f, 0, sizeof(f));
	for (int i = 2; i <= MAX; i++) f[i][1] = 1; 
	for (int i = 3; i <= MAX; i++) {
		for (int j = 2; j < i; j++) { // tinh f[i][j]: so i o vi tri thu j
			f[i][j] = 0;
			for (int k = 1; k < j; k++) if (j - k - 1 <= i - j - 1) {
				f[i][j] += f[j][k] * c[j - k - 1][i - j - 1] ;			
				f[i][j] %= MOD;
			}
		}
	}
}

long long process(int n) {
	long long res = 0;
	for (int j = 1; j <= n - 1; j++) {
		res += f[n][j];
		res %= MOD;
	}
	return res;
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("c.out", "w", stdout);
	
	init();

	int test;
	cin >> test;
	for (int i = 1; i <= test; i++) {
		int n;
		cin >> n;
		cout << "Case #" << i << ": " << process(n) << endl;
	}
	return 0;
}
