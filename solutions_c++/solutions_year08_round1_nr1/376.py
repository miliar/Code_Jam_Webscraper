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
	char sz[1000];
	fgets(sz, 1000, stdin);
	int l = strlen(sz);
	if (sz[l-1] == '\n') sz[l-1] = 0;
	return sz;
}

int readIntLine() {
	string s = readLine();
	return atoi(s.c_str());
}

int solveIt(vector<int> &a, vector<int> &b) {
	sort(a.begin(), a.end());
	sort(b.rbegin(), b.rend());

	int s = 0;
	for (int i = 0; i < a.size(); i++) s += a[i]*b[i];

	return s;
}

int main() {
	int N = readIntLine();
	for (int cn = 1; cn <= N; cn++) {
		int n;
		scanf("%d ", &n);

		vector<int> a(n), b(n);
		for (int i = 0; i < n; i++) scanf("%d ", &a[i]);
		for (int i = 0; i < n; i++) scanf("%d ", &b[i]);

		int res = solveIt(a, b);

		printf("Case #%d: %d\n", cn, res);
	}
	return 0;
}

