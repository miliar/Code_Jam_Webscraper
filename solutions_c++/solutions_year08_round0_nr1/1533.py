#include <cstdio>
#include <map>
#include <string>
#include <vector>
using namespace std;

int solve() {
	int n, q;

	scanf("%d\n", &n);
	vector<string> engines(n);
	for (int i = 0; i < n; i++) {
        char buf[255];
		gets(buf);
		engines[i] = string(buf);
	}

	scanf("%d\n", &q);
	map<string, int> occur;
	int res = 0, got = 0;	
	for (int i = 0; i < q; i++) {
		char buf[255];
		gets(buf);
		string query(buf);

		if (occur[query] == 0) got++;
		if (got == n) {
			res++;
			got = 1;
			for (int j = 0; j < n; j++)
				occur[engines[j]] = 0;
		}
		occur[query]++;
	}
	return res;
}

int main () {
	freopen("a.in", "r", stdin); freopen("a.out", "w", stdout);
	int nTests;
	scanf("%d", &nTests);
	for (int T = 1; T <= nTests; T++)
		printf("Case #%d: %d\n", T, solve());	
	fclose(stdin); fclose(stdout);
	return 0;
}
