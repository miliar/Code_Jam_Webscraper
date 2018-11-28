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

long long next(long long n) {
	if (n == 1)
		return 0;
	if (n == 0)
		return 2;	
	return n + 1;
}

long long getBase(long long n) {
	if (n <= 1)
		return 2;
	else
		return n + 1;
}

long long solve() {
	string s;
	cin >> s;
	map<char, long long> m;
	long long n = 1;
	m[s[0]] = 1;
	for (int i = 0; i < s.size(); i++)
		if (m.find(s[i]) == m.end()) {
			n = next(n);
			m[s[i]] = n;
		}	
	long long res = 0;
	long long base = getBase(n);
	for (int i = 0; i < s.size(); i++)
		res = base * res + m[s[i]];
	return res;
}

int main () {
	freopen("a.in", "r", stdin); freopen("a.out", "w", stdout);
	int nTests;
	scanf("%d", &nTests);
	for (int T = 1; T <= nTests; T++)
		printf("Case #%d: %lld\n", T, solve());
	fclose(stdin); fclose(stdout);
	return 0;
}
