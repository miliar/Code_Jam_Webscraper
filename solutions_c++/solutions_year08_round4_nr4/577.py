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
#pragma comment(linker, "/STACK:64000000")

#define pb push_back
#define mp make_pair
#define all(v) v.begin(),v.end()

int calc(const string &s) {
	int res = 1;
	char cur = s[0];
	for (int i = 1; i < s.size(); i++) {
		if (s[i] != cur) {
			cur = s[i];
			res++;
		}
	}
	return res;
}

int check(const vector<int> &perm, const string &s) {
	string res = "";
	int k = perm.size();
	for (int step = 0; step * k < s.size(); step++) {
		string z = s.substr(k * step, k);
		string u(k, 'x');
		for (int i = 0; i < k; i++)
			u[perm[i]] = z[i];
		res.append(u);
	}
	return calc(res);
}

int solve() {
	int k;
	string s;
	cin >> k >> s;
	vector<int> perm(k);
	for (int i = 0; i < k; i++)
		perm[i] = i;
	int res = 1000000000;
	do {
		res = min(res, check(perm, s));
	} while (next_permutation(all(perm)));
	return res;
}

int main () {
	freopen("d.in", "r", stdin); freopen("d.out", "w", stdout);
	int nTests;
	scanf("%d", &nTests);
	for (int T = 1; T <= nTests; T++)
		printf("Case #%d: %d\n", T, solve());
	fclose(stdin); fclose(stdout);
	return 0;
}
