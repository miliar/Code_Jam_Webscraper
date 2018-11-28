#include <math.h>
#include <stdio.h>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <algorithm>
#include <ctype.h>
#include <hash_set>

using namespace std;
using namespace stdext;

#define FOR(i, a, b) for (int _n(b), i(a); i < _n; i++)
#define REP(i, n) FOR(i, 0, n)
#define ALL(a) a.begin(), a.end()
#define SORT(a) sort(ALL(a))
#define pb push_back
#define INF 1000000

typedef pair< int, int > pii;

int t;

void init() {
	freopen("input_3.txt", "rt", stdin);
	scanf("%d\n", &t);
}

void find() {
	string line;
	getline(cin, line);
	vector< vector< int > > d(600);
	REP(i, 600) d[i] = vector< int >(20,0);
	string s = "welcome to code jam";
	FOR(i, 1, line.length()+1) d[i][0] = 1;

	FOR(j, 1, s.length()+1) {
		FOR(i, 1, line.length()+1) {
			if (line[i-1] == s[j-1]) d[i][j] = (d[i][j-1] + d[i-1][j]) % 10000;
			else d[i][j] = d[i-1][j];
		}
	}

	int res = d[line.length()][s.length()];
	int t = res;
	int z = (t==0)?3:4;
	while (t != 0) {
		t = t / 10; 
		z--;
	}
	REP(i, z) cout << '0';
	cout << d[line.length()][s.length()] << endl;
}

void solve() {
	freopen("out_3.txt", "wt", stdout);
	REP(i, t) {
		printf("Case #%d: ", i+1);
		find();
	}
}

int main() {
	init();
	solve();
}