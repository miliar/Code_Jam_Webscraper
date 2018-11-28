#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <set>
#include <map>

using namespace std;

int dbg;

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

int solveIt(vector<int> &v) {
	int ct = 0;
	for (int i = 0; i < v.size(); i++) {
		if (v[i] > i) {
			int j;
			for (j = i+1; j < v.size(); j++)
				if (v[j] <= i) break;
			int m = v[j];
			for (int k = j; k > i; k--) v[k] = v[k-1];
			v[i] = m;
			ct += j-i;
		}
	}
	return ct;
}

int main(int argc, char ** /*argv*/) {
	dbg = argc;
	int CCT = readIntLine();
	for (int cn = 1; cn <= CCT; cn++) {
		int N;
		scanf("%d ", &N);
		vector<int> v(N);
		for (int i = 0; i < N; i++) {
			string s = readLine();
			int j = N-1;
			while (j >= 0 && s[j] == '0') j--;
			v[i] = j;
		}

		long long res = solveIt(v);
		printf("Case #%d: %lld\n", cn, res);
	}
	return 0;
}

