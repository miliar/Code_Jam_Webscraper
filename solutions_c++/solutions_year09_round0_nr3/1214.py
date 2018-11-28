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

const string w = "welcome to code jam";

int solve(const string &s) {
	vector<vector<int> > a(s.size(), vector<int>(w.size()));
	for (int i = 0; i < s.size(); i++)
		for (int j = 0; j < w.size(); j++) {
			if (i > 0)
				a[i][j] += a[i - 1][j];
			if (s[i] == w[j]) {
				if (j > 0)
					a[i][j] += a[i][j - 1];
				else
					a[i][j] += 1;
			}
			a[i][j] %= 10000;
		}
	return a[s.size() - 1][w.size() - 1];
}

int main () {
	freopen("c.in", "r", stdin); freopen("c.out", "w", stdout);
	int nTests;
	scanf("%d", &nTests);
	getchar();
	for (int T = 1; T <= nTests; T++) {
		char buf[1024];
		gets(buf);
		int r = solve(string(buf));
		printf("Case #%d: %d%d%d%d\n", T, (r / 1000) % 10, (r / 100) % 10, (r / 10) % 10, r % 10);
	}
	fclose(stdin); fclose(stdout);
	return 0;
}
