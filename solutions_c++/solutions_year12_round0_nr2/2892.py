#include <algorithm>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <bitset>
#include <cstring>
#include <climits>
#include <deque>
#include <utility>
#include <complex>
#include <numeric>
#include <functional>
#include <stack>
#include <iomanip>
#include <ctime>

using namespace std;

typedef vector<string> vstr;
typedef vector<int> vint;
typedef vector<pair<int, int> > vpair;
typedef pair<int, int> pint;
typedef vector<vector<int> > v_vint;

#define oo (int)1<<28
#define mp make_pair
#define pb push_back
#define ll long long
#define sz(v) (int)v.size()

vint v;
int N, S, P, memo[101][101];

bool sur(int x, int y, int z) {
	if (abs(x - y) > 1)
		return true;
	if (abs(x - z) > 1)
		return true;
	if (abs(z - y) > 1)
		return true;

	return false;
}

int dp(int s, int ind) {
	if (ind >= sz(v))
		return 0;

	if (memo[s][ind] != -1)
		return memo[s][ind];

	int d1 = 0, d2 = 0, d3 = 0, d4 = 0;

	for (int i = 0; i <= 10; ++i) {
		for (int j = 0; j <= 10; ++j) {
			for (int k = 0; k <= 10; ++k) {
				if(max(abs(i-j), max(abs(i-k), abs(j-k))) > 2)
					continue;
				if ((i + j + k) != v[ind])
					continue;

				if (sur(i, j, k) && s > 0) {
					if (max(i, max(j, k)) >= P)
						d1 = dp(s - 1, ind + 1) + 1;
					else
						d2 = dp(s - 1, ind + 1);
				} else if (!sur(i, j, k)) {
					if (max(i, max(j, k)) >= P)
						d3 = dp(s, ind + 1) + 1;
					else
						d4 = dp(s, ind + 1);
				}
			}
		}
	}
	return memo[s][ind] = max(max(d1, d2), max(d3, d4));
}

int main() {
	freopen("out.txt", "wt", stdout);
	int n;
	scanf("%d", &n);
	int k = 0;
	while (n--) {
		k++;
		v.clear();
		memset(memo, -1, sizeof memo);
		scanf("%d%d%d", &N, &S, &P);
		while (N--) {
			int x;
			scanf("%d", &x);
			v.pb(x);
		}
		cout << "Case #" << k << ": " << dp(S, 0) << endl;
	}
	return 0;
}
