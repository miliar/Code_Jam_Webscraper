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

vector<int> readVI() {
	int n;
	scanf("%d ", &n);
	vector<int> v(n*2);
	for (int i = 0; i < n*2; i++) scanf("%d ", &v[i]);
	return v;
}

vector<int> solveIt(int n, vector<vector<int> > &c) {
	int l = 1<<n, best = -1, bm = 1000000;

	for (int i = 0; i < l; i++) {
		int m = 0;
		for (int j = 0; j < n; j++) if ((i>>j)&1) m++;
		if (m > bm) continue;

		bool ok = true;
		for (int j = 0; j < c.size() && ok; j++) {
			bool ok2 = false;
			for (int k = 0; !ok2 && k < c[j].size(); k += 2) {
				if (((i>>(c[j][k]-1))&1) == c[j][k+1]) {
					ok2 = true;
				}
			}
			if (!ok2) ok = false;
		}
		if (ok) {
			best = i;
			bm = m;
		}
	}
	if (best < 0) return vector<int>();
	vector<int> res(n);
	for (int i = 0; i < n; i++) res[i] = (best>>i)&1;
	return res;
}

int main() {
	int N = readIntLine();
	for (int cn = 1; cn <= N; cn++) {
		int n, m;
		scanf("%d %d ", &n, &m);

		vector<vector<int> > c(m);
		for (int i = 0; i < m; i++) c[i] = readVI();

		vector<int> res = solveIt(n, c);

		if (res.empty()) {
			printf("Case #%d: IMPOSSIBLE\n", cn);
		} else {
			printf("Case #%d:", cn);
			for (int i = 0; i < res.size(); i++)
				printf(" %d", res[i]);
			printf("\n");
		}
	}
	return 0;
}

