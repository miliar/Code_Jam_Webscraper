#include <iostream>
#include <string.h>
#include <string>
#include <algorithm>
using namespace std;

#define inf 1000000

int i, j, k, n, l, f, x;
int t, T, res;

char a[50005];

int b[10];

string s, s1, r;

string permut(string x) {
	string r;
	int i;
	r.resize(n);
	for (i = 0; i < n; i ++) {
		r[i] = x[b[i]];
	}
	return r;
}

int main() {
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	cin >> T;
	for (t = 1; t <= T; t ++) {
		cin >> n;
		memset(a, 0, sizeof(a));
		cin >> a;
		l = strlen(a);
		s = a;
		
		for (i = 0; i < n; i ++) {
			b[i] = i;
		}
		res = inf;
		while (1) {
			s1.clear();
			for (i = 0; i < l; i += n) {
				s1 += permut(s.substr(i, n));
			}
			x = 1;
			for (i = 1; i < l; i ++) {
				if (s1[i] != s1[i-1]) {
					x ++;
				}
			}
			if (x < res) {
				res = x;
			}
			f = next_permutation(b, b + n);
			if (f == 0) {
				break;
			}
		}
		cout << "Case #" << t << ": ";
		cout << res << endl;
	}
	return 0;
}




