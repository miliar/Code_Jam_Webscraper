#include <cmath>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <list>
#include <climits>
#include <ctime>
using namespace std;

#define NIL INT_MAX/2
#define inf 1e20
#define eps 1e-10

#define REP(i,n) for(int i=0; i<(n); ++i)
#define FOR(i,a,b) for(int i=a; i<(b); ++i)
#define clr(x) memset(x,0,sizeof(x)) 

const int N = 1000;

int l[1100];
int r[1100];
double p[1100];
string f[1100];
int id;
map<string, int>h;

bool check(string s) {
	for(int i = 0; i < s.size(); i++) {
		if(s[i] >= 'a' && s[i] <= 'z')return true;
	}
	return false;
}

void input(int u, bool fg) {
	char c;
	string inp = "";
	while((c = getchar()) && c != '(' && c != ')')inp += c;
	stringstream in(inp);

	int v = id;
	//cout << inp << endl;
	if(check(inp)) {
		in >> p[id] >> f[id];
		if(u != -1) {
			if(fg)l[u] = id;
			else r[u] = id;
		}
		id++;
	}
	else {
		in >> p[id];
		if(u != -1) {
			if(fg)l[u] = id;
			else r[u] = id;
		}
		id++;
	}
	if(c == '(') {
		input(v, true);
		while((c = getchar()) && c != '(');
		input(v, false);
		while((c = getchar()) && c != ')');
		return;
	}
	else if(c == ')')return;
}

double dfs(int u) {
	double rec = p[u];
	if(!l[u])return rec;
	
	if(h[f[u]])rec *= dfs(l[u]);
	else rec *= dfs(r[u]);
	return rec;
}

void solve() {
	h.clear();
	int cnt = 1;
	memset(l, 0, sizeof(l));
	memset(r, 0, sizeof(r));
	int L;
	cin >> L;
	char c;
	while((c = getchar()) && c != '(');
	id = 1;
	input(-1, true);

	int n, k;
	cin >> n;
	string inp;
	while(n--) {
		h.clear();
		cin >> inp;
		cin >> k;
		while(k--)cin >> inp, h[inp] = 1;
		printf("%.6lf\n", dfs(1));
	}
}

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int cases;
	int cnt = 1;
	cin >> cases;
	while(cases--) {
		printf("Case #%d:\n", cnt++);
		solve();
	}

	return 0;
}

/*Powered By Lynn-Beta1*/