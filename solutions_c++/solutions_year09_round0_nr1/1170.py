#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define pb push_back
#define mp make_pair
#define all(v) v.begin(),v.end()

const int N = 5050;
int L, D;
string s[N];

int solve(const string &pattern) {
	vector<vector<bool> > can(L, vector<bool>(26));
	int pos = 0;
	bool in = false;
	for (int i = 0; i < pattern.size(); i++) {
		switch (pattern[i]) {
			case '(':
				in = true;
				break;
			case ')':
				in = false;
				++pos;
				break;
			default:
				can[pos][(int)(pattern[i] - 'a')] = true;
				if (!in)
					++pos;
				break;
		}
	}
	assert(pos == L);
	
	int res = 0;
	for (int i = 0; i < D; i++) {
		bool ok = true;
		for (int j = 0; j < L; j++)
			if (!can[j][(int)(s[i][j] - 'a')]) {
				ok = false;
				break;
			}
		if (ok)
			++res;
	}
	return res;
}

int main () {
	freopen("a.in", "r", stdin); freopen("a.out", "w", stdout);
	scanf("%d%d", &L, &D);
	int nTests;
	scanf("%d", &nTests);
	for (int i = 0; i < D; i++) {
		char buf[N];
		scanf("%s", buf);
		s[i] = string(buf);
	}
	for (int T = 1; T <= nTests; T++) {
		char buf[N];
		scanf("%s", buf);
		printf("Case #%d: %d\n", T, solve(string(buf)));
	}
	fclose(stdin); fclose(stdout);
	return 0;
}
