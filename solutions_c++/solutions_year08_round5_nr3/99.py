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
	vector<int> v(n);
	for (int i = 0; i < n; i++) scanf("%d ", &v[i]);
	return v;
}

int nextRowMask(int m, int stm) {
	int x = 0;
	for (int i = 0; m >> i; i++) if ((m>>i)&1) {
		if (i) x |= 1<<(i-1);
		x |= 1<<(i+1);
	}
	return x&stm;
}

int solveIt(vector<string> &s) {
	int R = s.size(), C = s[0].size();
	vector<int> bm(R, 0);
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) if (s[i][j] == 'x') bm[i] |= 1<<j;
	}

	int stm = (1<<C)-1;

	vector<int> prct(1<<C, 0);
	for (int i = 0; i < R; i++) {
		vector<int> crct(1<<C, 0);
		for (int j = 0; j <= stm; j++) if (!(j&bm[i])) {
			int nm = nextRowMask(j, stm);
			if (!(nm&j)) {
				int tct = 0;
				for (int k = 0; j >> k; k++) if ((j>>k)&1) tct++;
				int bct = 0;
				for (int k = 0; k <= stm; k++)
					if (!(nm&k) && prct[k] > bct)
						bct = prct[k];
				crct[j] = tct+bct;
			}
		}
		prct = crct;
	}

	int res = 0;
	for (int i = 0; i <= stm; i++) if (prct[i] > res) res = prct[i];
	return res;
}

int main() {
	int N = readIntLine();
	for (int cn = 1; cn <= N; cn++) {
		int Y, X;
		scanf("%d %d ", &Y, &X);
		vector<string> sts(Y);
		for (int i = 0; i < Y; i++) sts[i] = readLine();

		long long res = solveIt(sts);

		printf("Case #%d: %lld\n", cn, res);
	}
	return 0;
}

