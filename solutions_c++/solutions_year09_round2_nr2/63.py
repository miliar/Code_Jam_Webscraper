#define _CRT_SECURE_NO_DEPRECATE

#pragma comment(linker, "/STACK:255888000")

#include <iostream>
#include <vector>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <queue>
#include <stack>

#define pii pair<int,int>
#define vi vector<int>
#define int64 long long
#define ll long long
#define INF 1000000000
#define ld long double
#define forn(i, n) for(int i = 0; i < (int)n; i++)
#define forv(i, v) for(int i = 0; i < (int)v.size(); i++)
#define ford(i, n) for(int i = (int)(n - 1); i >= 0; i--)
#define fore(i, a, b) for(int i = (int)a; i < (int)b; i++)
#define all(a) a.begin(),a.end()
#define norm(a) sort(a);a.erase(unique(all(a)),a.end())
#define pb push_back
#define mp make_pair
#define fs first
#define sc second

const int64 INF64 = (int64)1e18;
const ld EPS = 1e-8;
const ld PI = 3.1415926535897932384626433832795;

using namespace std;

char  buf[130];

inline void solve() {
	string s;
	scanf("%s", buf);
	s = buf;
	int a[10];
	memset(a, 0, sizeof a);
	forn(i, s.length())
		a[s[i] - '0']++;
	int last = 1;
	forn(i, s.length() - 1)
		last &= s[i] >= s[i + 1];
	if (last) {
		a[0]++;
		fore(i, 1, 10)
			if (a[i]) {
				--a[i];
				printf("%c", (char)(i + '0'));
				break;
			}
		forn(i, a[0])
			printf("0");
		fore(c, 1, 10)
			forn(j, a[c])
				printf("%c", (char)(c + '0'));
		return;
	}
	int u[10];
	forn(i, 10)
		u[i] = a[i];
	string best = string((int)s.length(), '9');
	forn(i, s.length()){
		fore(c, s[i] - '0' + 1, 10) {
			if (u[c]) {
				string cur = string((int)s.length(), '9');
				forn(j, i)
					cur[j] = s[j];
				u[c]--;
				cur[i] = (char)(c + '0');
				int p = i + 1;
				forn(j, 10)
					forn(k, u[j])
						cur[p++] = (char)(j + '0');
				u[c]++;
				if (cur < best)
					best = cur;
			}
		}
		u[s[i] - '0']--;
	}
	printf("%s", best.c_str());
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int tests;
	cin >> tests;
	fore(test, 1, tests + 1) {
		printf("Case #%d: ", test);
		solve();
		puts("");
	}

	return 0;
}