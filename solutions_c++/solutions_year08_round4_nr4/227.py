#include <iostream>
#include <algorithm>

using namespace std;

int test;

int k;
char s[100000];
char d[100000];

int a[20];

int calc(char *s, int l) {
	int res = 0;
	char c = 0;
	for (int i = 0; i < l; i++) {
		if (s[i] != c) res++;
		c = s[i];
	}
	return res;
}

void solve() {
	cin >> k >> s;
	for (int i = 0; i < k; i++) a[i] = i;
	int l = strlen(s);
	int res = l;
	do {
		for (int i = 0; i < l; i+=k) for (int j = 0; j < k; j++) d[i+j] = s[i+a[j]];
		res = min(res, calc(d, l));
	} while (next_permutation(a, a + k));
	cout << "Case #" << test << ": " << res << endl;
}

int main() {
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	int T; cin >> T;
	for (test = 1; test <= T; test++)
		solve();
	fclose(stdout);
	return 0;
}