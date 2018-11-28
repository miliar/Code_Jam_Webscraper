#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cassert>
#include <algorithm>

using namespace std;

#define debug 0
#define cerr if(debug) cerr

#define For(i, a, b) for(int i = a; i < b; i++)
#define Rep(it, a) for(__typeof(a.begin()) it = a.begin(); it != a.end(); it++)
#define pb push_back
#define mp make_pair
#define sz(a) ((int)a.size())
#define all(a) a.begin(), a.end()
#define cp(a) cerr << "(" << #a << "," << a << ") ";
#define cen cerr << endl;

typedef long long lint;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

const int inf = 0x7fffffff;

const int Size = 1000 * 1000 + 1;
char buffer[Size];

map<char, char> m;
void precalc() {
	freopen("in.txt", "r", stdin);
	map<char, char> rm;
	int n = 3;
	vector<string> v;
	For(i, 0, n) {
		gets(buffer);
		v.pb(buffer);
	}
	rm['z'] = 'q';
	rm['a'] = 'y';
	rm['o'] = 'e';
	m['q'] = 'z';
	m['y'] = 'a';
	m['e'] = 'o';
	
	For(i, 0, n) {
		gets(buffer);
		string b = buffer;
		string &a = v[i];
		assert(sz(a) == sz(b));
		For(j, 0, sz(a)) {
			char ca = a[j];
			char cb = b[j];
			if(m.count(ca) == 0) {
				m[ca] = cb;
				assert(rm.count(cb) == 0);
				rm[cb] = ca;
			}
			else {
				assert(m[ca] == cb);
			}
		}
	}
	vector<char> unassigned;
	For(i, 'a', 'z' + 1) {
		if(m.count(i) == 0) {
			unassigned.pb(i);
		}
	}
	assert(sz(unassigned) <= 1);

	For(i, 'a', 'z' + 1) {
		if(rm.count(i) == 0) {
			m[unassigned.front()] = i;
		}
	}
}

int solution(int nTest) {
	printf("Case #%d: ", nTest + 1);
	gets(buffer);
	string s = buffer;
	cp(sz(m));cen;
	For(i, 0, sz(s)) {
		if(m.count(s[i])) {
			s[i] = m[s[i]];
		}
	}
	puts(s.c_str());

	return 1;
}

int main() {
	precalc();
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);


	int i = 0, n = 99999;
	scanf("%d", &n);
	gets(buffer);

	while(i < n && solution(i)) {
		i++;
	}

	return 0;
}
