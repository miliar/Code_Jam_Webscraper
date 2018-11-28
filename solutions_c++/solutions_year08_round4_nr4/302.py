#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <map>

using namespace std;

string readLine() {
	char sz[100000];
	fgets(sz, 100000, stdin);
	int l = strlen(sz);
	if (sz[l-1] == '\n') sz[l-1] = 0;
	return sz;
}

int readIntLine() {
	string s = readLine();
	return atoi(s.c_str());
}

vector<int> readVI() {
	int n;
	scanf("%d ", &n);
	vector<int> v(n);
	for (int i = 0; i < n; i++) scanf("%d ", &v[i]);
	return v;
}

long long solveIt(int k, string &s) {
	vector<int> ip(k);
	for (int i = 0; i < k; i++) ip[i] = i;

	int ms = s.size(), b = s.size()/k;
	do {
		int ct = 0, pch = 0;
		for (int j = 0; j < b; j++) {
			for (int i = 0; i < k; i++) {
				int ch = s[j*k+ip[i]];
				if (ch != pch) ct++;
				pch = ch;
			}
		}
		if (ct < ms) ms = ct;
	} while (next_permutation(ip.begin(), ip.end()));

	return ms;
}

int main() {
	int N = readIntLine();
	for (int cn = 1; cn <= N; cn++) {
		int k;
		string s;
		k = readIntLine();
		s = readLine();

		long long res = solveIt(k, s);

		printf("Case #%d: %lld\n", cn, res);
	}
	return 0;
}

