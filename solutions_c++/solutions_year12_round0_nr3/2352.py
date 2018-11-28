#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <stack>
#include <queue>
#include <deque>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <cassert>
#include <string>
#include <cstring>

using namespace std;

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()
#define forn(i, n) for(int i = 0;i < n;i++)

typedef long long ll;
typedef unsigned long long llu;

const int inf = 2e9;
const double eps = 1e-7;
const double pi = 3.1415926535;

vector < vector <int> > v;
set <int> used;

void shift(char* s) {
	int n = strlen(s);
	char c = s[0];
	forn(i, n - 1) {
		s[i] = s[i + 1];
	}
	s[n - 1] = c;
}

int main() {
	v.resize(2000001);
	int a, b, tests, cur;
	char s[10];
	for(int i = 1;i <= 2000000;i++) {
		used.clear();
		used.insert(i);
		sprintf(s, "%d", i);
		shift(s);
		while(true) {
			sscanf(s, "%d", &cur);
			if(used.find(cur) != used.end()) break;
			if(1 <= cur && cur <= 2000000) {
				v[i].pb(cur);
			}
			shift(s);
			used.insert(cur);
		}
	}
	cin >> tests;
	forn(t, tests) {
		cin >> a >> b;
		ll res = 0;
		for(int i = a;i <= b;i++) {
			for(int j = 0;j < sz(v[i]);j++) {
				if(a <= v[i][j] && v[i][j] <= b && v[i][j] > i) res++;
			}
		}
		cout << "Case #" << t + 1 << ": " << res << '\n';
	}
	return 0;
}
