#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <numeric>
#include <utility>

#include <deque>
#include <stack>
#include <bitset>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <queue>
#include <list>

#include <sstream>
#include <iostream>
#include <iomanip>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) a.size() - 1
#define all(a) a.begin(), a.end()
#define I (int)
#define I64 (long long)
#define LD (long double)
#define VI vector<int>
#define pti pair<int, int>
#define ptd pair<long double, long double>
#define sqr(x) ((x) * (x))

const long double EPS = 1E-9;
const int INF = (int)1E9;
const long long INF64 = (long long)1E18;
const long double PI = 2 * acos(.0);

typedef long double ld;
typedef long long ll;

int n;
char str[50][50];

bool test(const vector<int>& v) {
	forn(i, n) {
		int idx = v[i];
		for (int j = i + 1;j < n;j++)
			if (str[idx][j] == '1')return false;
	}

	return true;
}


void solve(int t) {
	map<vector<int>, int> s;
	
	scanf("%d", &n);
	vector<int> cur;
	forn(i, n) {
		scanf("%s", str[i]);
		cur.pb(i);
	}

	s[cur] = 0;
	queue<vector<int> > q;
	int ans = INF;
	q.push(cur);

	while (!q.empty()) {
		vector<int> tmp = q.front();
		q.pop();

		int val = s[tmp];

		if (test(tmp)) {
			ans = min(ans, val);
		}

		forn(i, n - 1) {
			swap(tmp[i], tmp[i + 1]);

			if (!s.count(tmp)) {
				s[tmp] = val + 1;
				q.push(tmp);
			}

			swap(tmp[i], tmp[i + 1]);
		}
	}

	printf("Case #%d: %d\n", t, ans);
}


int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	int t;
	scanf("%d", &t);
	forn(i, t)
		solve(i + 1);
	
    return 0;
}
