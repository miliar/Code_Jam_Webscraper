#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <set>
#include <string>

using namespace std;

const int MAX_NAME_LEN = 110;

int S = 0;
set<string > names;

int solve() {
	int Q = 0;
	int res = 0;
	set<string > cnames(names);

	scanf("%d\n", &Q);
	for (int i = 0; i < Q; ++i) {
		char name[MAX_NAME_LEN] = {0};
		gets(name);
		string s(name);
		if (cnames.end() != cnames.find(s)) {
			if (1 == cnames.size()) {
				++res;
				cnames.insert(names.begin(), names.end());
			}
			cnames.erase(s);
		}
	}

	return res;
}

int main(void) {
	int N = 0;

	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);

	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		names.erase(names.begin(), names.end());
		scanf("%d\n", &S);
		for (int j = 0; j < S; ++j) {
			char name[MAX_NAME_LEN] = {0};
			gets(name);
			string s(name);
			names.insert(s);
		}
		printf("Case #%d: ", i + 1);
		int res = solve();
		printf("%d\n", res);
	}

	return 0;
}
