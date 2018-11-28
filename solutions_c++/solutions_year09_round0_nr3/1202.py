// cheburashka, bear-mouse, team template

#include <cstdlib>
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <map>
#include <algorithm>
#include <cstdio>
#include <stack>
#include <cmath>
#include <queue>
#include <set>
#include <cstring>
using namespace std;

#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define deb(x) cout << #x << ": " << x << endl;
#define debv(x) for(int i = 0; i < (x).size(); i++) cout << x[i] << ' '; cout << endl;
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

typedef long long ll;
typedef vector < string > vs;
typedef vector <int> vi;

ifstream inp("C.in");
ofstream out("C.out");

string s, g = "welcome to code jam";
int N, M;

int lcs() {
	int d[20][502];
	memset(d, 0, sizeof(d));
	if (s[0] == g[0]) {
		d[0][0] = 1;
	}
	for (int i = 1; i < N; i++) {
		d[i][0] = d[i - 1][0];
		if (g[i] == s[0]) {
			d[i][0] = 1;
		}
	}
	for (int j = 1; j < M; j++) {
		d[0][j] = d[0][j - 1];
		if (g[0] == s[j]) {
			d[0][j] = 1;
		}
	}
	for (int i = 1; i < N; i++) {
		for (int j = 1; j < M; j++) {
			if (g[i] == s[j]) {
				d[i][j] = d[i - 1][j - 1] + 1;
			} else {
				d[i][j] = max(d[i - 1][j], d[i][j - 1]);
			}
		}
	}
	return d[N - 1][M - 1] == N;
}

int dp[20][502];

int rec(int i, int j) {
	if (i < 0) {
		return 1;
	}
	if (j < 0) {
		return 0;
	}
	int &ret = dp[i][j];
	if (ret != -1) {
		return ret;
	}
	ret = 0;
	for (int k = j; k >= 0; k--) {
		if (s[k] == g[i]) {
			ret = (ret + rec(i - 1, k - 1)) % 10000;
		}
	}
	return ret;
}

int solve() {
	/*if (!lcs()) {
		return 0;
	}*/
	memset(dp, -1, sizeof(dp));
	return rec(N - 1, M - 1);
}

int main()
{	
	int T;
	N = g.size();
	getline(inp, s);
	T = atoi(s.c_str());
	for (int i = 0; i < T; i++) {
		getline(inp, s);
		M = s.size();
		
		int ans = solve();

		char buf[7];
		memset(buf, '0', sizeof(buf));
		sprintf(buf, "%d", ans);
		string res = buf;
		while (res.size() < 4) {
			res = "0" + res;
		}
		out << "Case #" << i + 1 << ": " << res << endl;
	}
	inp.close();
	out.close();
	return 0;
}
