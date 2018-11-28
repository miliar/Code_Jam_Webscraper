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
#include <sstream>

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

double p[105];

string fl[107];

int son1[108], son2[108];

set<string> f[106];

int L, A;

char buf[10000];

int n, N;

string s, t;

int l;

int build(int v) { 
	n++;
	v = n - 1;
	l++;
	string num = "";
	while(s[l] == '.' || '0' <= s[l] && s[l] <= '9'){
		num += s[l];
		++l;
	}
	stringstream ss;
	ss << num;
	ss >> p[v];
	if (s[l] == ')'){
		// leaf
		l++;
		return v;
	}
	fl[v] = "";
	while(s[l] != '(')
		fl[v] += s[l++];
	
	// s[l] == '('
	son1[v] = build(0);
	son2[v] = build(0);
	l++;
	return v;
}

double get(int a){
	int v = 0;
	double res = 1.;
	while(son1[v] >= 0){
		res *= p[v];
		if (f[a].find(fl[v]) != f[a].end()){
			v = son1[v];
		}else{
			v = son2[v];
		}
	}
	res *= p[v];
	return res;
}

inline void solve() {
	scanf("%d\n", &L);
	
	memset(son1, -1 ,sizeof son1);

	forn(i, L){
		getline(cin, t);
		s += t;
	}
	scanf("%d\n", &A);
	t = "";
	forn(i, s.length())
		if (s[i] != ' ')
			t += s[i];
	s = t;
	forn(i, A){
		int h;
		f[i].clear();
		scanf("%s", buf);
		scanf(" %d", &h);
		forn(j, h){
			scanf("%s", buf);
			t = buf;
			f[i].insert(t);
		}
	}
	//
	n = 0;
	N = (int)s.length();
	build(0);

	forn(i, A)
		printf("%.16lf\n", get(i));
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
		printf("Case #%d:\n", test);
		solve();
		//puts("");
	}

	return 0;
}