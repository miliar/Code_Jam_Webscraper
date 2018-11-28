#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int mod = 100003;

int f[502][502];
int ans[502];
int c[502][502];


int main (int argc, char * const argv[])
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	memset(f, 0xff, sizeof(f));
	for (int i = 0; i < 501; i++) {
		c[i][0] = 1;
		for (int j = 1; j <= i; j++) {
			c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % mod;
		}
	}
	f[2][1] = 1;
	ans[2] = 1;
	for (int i = 3; i <= 501; i++) {
		f[i][1] = 1;
		ans[i] = 1;
		for (int j = 2; j < i; j++) {
			for (int k = max(1, 2 * j - i); k < j; k++) {
				if (f[j][k] != -1) {
					if (f[i][j] < 0) f[i][j] = 0;
					f[i][j] = (f[i][j] + f[j][k] * c[i - j - 1][j - k - 1]) % mod;
				}
			}
			if (f[i][j] > 0) ans[i] = (ans[i] + f[i][j]) % mod;
		}	}
	
	int test;
	cin >> test;
	for (int t = 1; t <= test; t++) {
		int n;
		cin >> n;
		cout << "Case #" << t << ": " << ans[n] << endl;
	}
}
