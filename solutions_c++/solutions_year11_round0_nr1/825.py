
#include <map>
#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
using namespace std;

string next() {
	string res;
	cin >> res;
	return res;
}

int parseInt(string s) {
	int res;
	sscanf(s.c_str(), "%d", &res);
	return res;
}

inline int abs(int x) {
	return x > 0 ? x : -x;
}

int main() {
	int testsCount = parseInt(next());
	for (int test = 0; test < testsCount; ++test) {
		int n = parseInt(next());
		map<string, int> positionAt;
		map<string, int> availableAt;
		positionAt["O"] = 1, availableAt["O"] = 0;
		positionAt["B"] = 1, availableAt["B"] = 0;
		int res = 0;
		for (int i = 0; i < n; ++i) {
			string who = next();
			int where = parseInt(next());
			int need = abs(positionAt[who] - where);
			availableAt[who] += need + 1;
			string other = (who == "B" ? "O" : "B");
			if (availableAt[other] >= availableAt[who])
				availableAt[who] = availableAt[other] + 1;
			positionAt[who] = where;
			res = max(res, availableAt[who]);
		}
		printf("Case #%d: %d\n", test + 1, res);
	}
	return 0;
}