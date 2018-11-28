#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <sstream>
#include <cassert>
#include <functional>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <ctime>
#include <deque>

using namespace std;

void prepare() {
	freopen("input.txt", "r", stdin);
#ifndef _DEBUG
	freopen("output.txt", "w", stdout);
#endif
}

#define fo(a,b,c) for( a = (b); a < (c); ++ a )
#define fr(a,b) fo(a,0,(b))
#define fi(n) fr(i,(n))
#define fj(n) fr(j,(n))
#define fk(n) fr(k,(n))
#define mp make_pair
#define pb push_back
#define all(a) (a).begin( ), (a).end( )
#define _(a, b) memset( (a), (b), sizeof( a ) )
#define __(a) memset( (a), 0, sizeof( a ) )
#define sz(a) (int)(a).size( )

typedef long long lint;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair <int, int> PII;

const int INF = 2000000000;

int n, m;
char mapper[256][256];
char kill[256][256];

void solve() {
	int i, j, k;
	__(mapper);
	__(kill);
	scanf("%d", &n);
	for (i = 0; i < n; ++ i) {
		char buf[4];
		scanf("%s", buf);
		char a = buf[0];
		char b = buf[1];
		mapper[a][b] = mapper[b][a] = buf[2];
	}
	scanf("%d", &n);
	for (i = 0; i < n; ++ i) {
		char buf[4];
		scanf("%s", buf);
		char a = buf[0];
		char b = buf[1];
		kill[a][b] = kill[b][a] = 1;
	}
	scanf("%d", &n);
	char v[105];
	scanf("%s", v);
	string s;
	for (i = 0; i < n; ++ i) {
		s += v[i];
		while (sz(s) >= 2) {
			char c = mapper[s[sz(s) - 1]][s[sz(s) - 2]]; 
			if (c) {
				s.pop_back();
				s.pop_back();
				s.push_back(c);
			} else {
				break;
			}
		}
		for (j = 0; j < sz(s) - 1; ++ j) {
			if (kill[s[j]][s[sz(s) - 1]]) {
				s = "";
			}
		}
	}
	printf("[");
	for (i = 0; i < sz(s); ++ i){
		if (i) {
			printf(", ");
		}
		printf("%c", s[i]);
	}
	printf("]\n");
}

int main() {
	prepare();
	int tn;
	cin >> tn;
	int t = 0;
	while (t++ < tn) {
		printf("Case #%d: ", t);
		solve();
	}

	return 0;
}