#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <ctype.h>
#include <complex>
using namespace std;
#define REP(i,n) for (int i=0,_n=int(n);i<_n;++i)
#define REPD(i,n) for (int i=int(n)-1;i>=0;--i)
#define FOR(i,a,b) for (int _b=int(b),i=int(a);i<=_b;++i)
#define FORD(i,a,b) for(int i=int(a),_b=int(b);i>=_b;--i)
#define FILL(x,v) memset(x,v,sizeof x);
#define mp make_pair
#define x first
#define y second
#define sz(s) int((s).size())
#define pb push_back
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef long long ll;
typedef long double ldb;
template<class T> T sqr(T x) {return x * x;}
template<class T> T abs(T x) {return (x < 0) ? -x : x;}
const double EPS = 1e-9;
const int INF = 1010 * 1000 * 1000;

vector<int> s;
int step;
vector< vector<int> > a;
bool found;

void dfs(int v) {
	if (s[v] == step) {
		found = true;
		return;
	}
	s[v] = step;
	REP(i, sz(a[v])) {
		dfs(a[v][i]);
		if (found)
			break;
	}
}

int main () {
	freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);	
	//freopen("Input.txt", "r", stdin);freopen("Output.txt", "w", stdout);
	
	int test;
	cin >> test;
	REP(tc, test) {
		int n;
		cin >> n;
		a.assign(n, vector<int>(0));
		
		REP(i, n) {
			int m;
			cin >> m;
			REP(j, m) {
				int c;
				cin >> c;
				a[i].pb(c - 1);
			}
		}
		
		s.assign(n, 0);
		step = 0;
		found = false;
		
		REP(i, n) {
			step++;
			dfs(i);
		}
		
		printf("Case #%d: ", tc + 1);
		
		if (found)
			printf("Yes");
		else
			printf("No");
		
		printf("\n");
	}
	
	
	return 0;
}

















