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

int main() {
	freopen("out.txt", "wt", stdout);
	map<char, char> m;
	vstr v1, v2;
	v1.pb("ejp mysljylc kd kxveddknmc re jsicpdrysi");
	v1.pb("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
	v1.pb("de kr kd eoya kw aej tysr re ujdr lkgc jv");
	v2.pb("our language is impossible to understand");
	v2.pb("there are twenty six factorial possibilities");
	v2.pb("so it is okay if you want to just give up");

	for (int j = 0; j < sz(v1); ++j) {
		for (int k = 0; k < sz(v1[j]); ++k) {
			if (m.find(v1[j][k]) == m.end()) {
				m[v1[j][k]] = v2[j][k];
			}
		}
	}
	m['q'] = 'z', m['z'] = 'q';

	int n;
	cin >> n;
	int k = 0;
	string str;
	getline(cin, str);
	vstr res;
	while (n--) {
		getline(cin, str);
		for (int i = 0; i < sz(str); ++i) {
			str[i] = m[str[i]];
		}
		res.pb(str);
	}

	for (int i = 0; i < sz(res); ++i) {
		k++;
		cout << "Case #" << k << ": " << res[i] << endl;
	}

	return 0;
}
