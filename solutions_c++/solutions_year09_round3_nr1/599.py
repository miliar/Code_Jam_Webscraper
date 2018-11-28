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

long long  solve() {
	string s;
	cin >> s;
	string t = s.c_str();
	sort(all(t));
	t.erase(unique(all(t)), t.end());
	int base = (int)t.size();

	map<char, int> m;
	bool used[100];
	memset(used, 0, sizeof(used));

	if (base == 1) {
		long long ans = 1LL << (s.size());
		ans--;
		return ans;
	} else {
		m[s[0]] = 1;
		used[1] = true;

		long long cur = 1;
		long long ans = 0;

		vector<int> rez;
		forn(i, s.size()) {
			if (!m.count(s[i])) {
				int idx = -1;
				forn(j, 100) {
					if (!used[j]) {
						idx = j;
						break;
					}
				}
				m[s[i]] = idx;
				used[idx] = true;
			}
			rez.pb(m[s[i]]);
		}

		ford(i, rez.size()) {
			ans += rez[i] * cur;
			cur *= base;
		}
		return ans;
	}

	return 0;
}


int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	int n;
	scanf("%d", &n);
	forn(i, n) {
		printf("Case #%d: %I64d\n", i + 1, solve());
	}

	
    return 0;
}
