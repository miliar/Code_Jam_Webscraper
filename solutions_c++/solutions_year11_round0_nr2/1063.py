#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>
using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define forv(i, v) forn(i, (v).size())
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()
#define contains(c, v) binary_search(all(c), v)

typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;
typedef long double ld;

bool oppose(string a, string in)
{
	forv(i, a) {
		if (contains(in, a[i])) return true;
	}
	return false;
}

string solve(const string& s, vs comb, vs cMap, vs op)
{
	string res;
	forv(i, s) {
		if (res.empty()) {
			res.pb(s[i]);
			continue;
		}
		if (contains(comb[res[res.size()-1]-'A'], s[i])) {
			res[res.size()-1] = cMap[res[res.size()-1]-'A'][s[i]-'A'];
			continue;
		}
		if (oppose(res, op[s[i]-'A'])) {
			res.clear();
			continue;
		}
		res += s[i];
	}
	string ret = "[";
	forv(i, res) {
		if (i) ret += ", ";
		ret += res[i];
	}
	ret += ']';
	return ret;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	ios_base::sync_with_stdio(false);
	int tn; cin >> tn;
	forn(it, tn) {
		int c; cin >> c;
		vs comb(26);
		vs combMap(26, string(26, ' '));
		forn(i, c) {
			string s; cin >> s;
			comb[s[0]-'A'] += s[1];
			comb[s[1]-'A'] += s[0];
			combMap[s[0]-'A'][s[1]-'A'] = s[2];
			combMap[s[1]-'A'][s[0]-'A'] = s[2];
		}
		int d; cin >> d;
		vs op(26);
		forn(i, d) {
			string s; cin >> s;
			op[s[0]-'A'] += s[1];
			op[s[1]-'A'] += s[0];
		}
		forn(i, 26) {
			sort(all(comb[i]));
			sort(all(op[i]));
		}
		int k; cin >> k;
		string s; cin >> s;
		cout << "Case #" << it+1 << ": " << solve(s, comb, combMap, op) << endl;
	}
	return 0;
}
