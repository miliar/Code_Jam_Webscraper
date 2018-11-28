#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <sstream>

#include <cassert>
#include <cmath>
#include <ctime>

#include <map>
#include <set>
#include <bitset>
#include <queue>

using namespace std;

typedef long long int64;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; --i)
#define fs first
#define sc second
#define pb push_back
#define mp make_pair
#define all(a) a.begin(), a.end()

const int INF = INT_MAX >> 1;
const double PI = 3.1415926535897932384626433832795;
const double EPS = 1E-8;

string solve(string s) {
	bool found = false;
	for(int i = (int)s.length() - 1; i > 0; --i)
		if (s[i - 1] < s[i]) {
			found = true;
			char mn = s[i];
			vector<char> a;
			for(int j = i - 1; j < (int)s.length(); ++j) {
				a.pb(s[j]);
				if (s[j] > s[i - 1]) mn = min(mn, s[j]);
			}
			sort(all(a));
			s[i - 1] = mn;
			a.erase(lower_bound(all(a), mn));
			
			forn(j, a.size())
				s[i + j] = a[j];

			break;
		}
	if (found) return s;
	return solve("0" + s);
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tk;
	scanf("%d", &tk);

	for(int tc = 1; tc <= tk; ++tc) {
		string s;
		cin >> s;
		printf("Case #%d: %s\n", tc, solve(s).c_str());
	}

	return 0;
}
 