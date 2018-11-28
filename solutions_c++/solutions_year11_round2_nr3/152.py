#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
#include <functional>
#include <map>
#include <set>
#include <cstring>
#include <string>
#include <cctype>
#include <cassert>

using namespace std;

#define pb push_back
#define mp make_pair
#define rep(i,n) for(int i = 0; i < (n); i++)
#define repr(i,b,e) for(int i = (b); i <= (e); i++)
#define INF (1001001001)
#define EPS (1e-15)

#define pr(x) do{cout << (#x) << " = " << (x) << endl;}while(0)
#define pri(x,i) do{cout << (#x) << "[" << i << "] = " << (x[i]) << endl;}while(0)
#define pra(x,n) rep(__i,n) pri(x,__i);
#define prar(x,b,e) repr(__i,b,e) pri(x,__i);

typedef long long llint;
typedef pair<int, int> pint;
typedef vector<int> vint;

int in() {
	int a;
	scanf("%d ", &a);
	return a;
}

int N, M;

bool edges[2010][2010];
int ans = INF;

int color[2010];

void solve(int b, int e, int chouten) {
	chouten++;
	if(b == e) {
		ans = min(ans, chouten);
		return;
	}
	int prev = e;
	int hoge = chouten;
	for(int i = N - 1; i >= 0; i--) {
		if(edges[b][i]) {
			solve(i, prev, hoge);
			prev = i;
			hoge = 1;
		}
	}
}

int colcount[2010];
bool okans;

bool abc(int b, int e) {
	int older[12];
	rep(i, ans + 1) older[i] = colcount[i];
	
	colcount[color[b]]++;
	
	bool ret = true;
	
	if(b == e) {
		bool ng = false;
		repr(i, 1, ans) {
			if(colcount[i] == 0) {
				ng = true;
				break;
			}
		}
		if(ng) {
			ret = false;
		}
		else {
			ret = true;
		}
		
		goto HOGE;
	}
	else {
		int prev = e;
		
		for(int i = N - 1; i >= 0; i--) {
			if(edges[b][i]) {
				if(! abc(i, prev)) {
					ret = false;
					goto HOGE;
				}
				prev = i;
				rep(i, ans + 1) colcount[i] = 0;
				colcount[color[b]]++;
			}
		}
	}
	HOGE:;
	rep(i, ans + 1) colcount[i] = older[i];
	return ret;
}

void coloring(int depth) {
	if(depth == N) {
		if(abc(0, N - 1)) {
			okans = true;
		}
		return;
	}
	
	if(okans) return;
	
	repr(i, 1, ans) {
		color[depth] = i;
		coloring(depth + 1);
		if(okans) return;
	}
}

int main() {
	int T = in();
	rep(tst, T) {
		printf("Case #%d: ", tst + 1);
		
		N = in();
		M = in();
		
		rep(i, N + 3) rep(k, N + 3) edges[i][k] = false;
		
		vint begins, ends;
		rep(i, M) {
			int a = in();
			begins.pb(a - 1);
		}
		rep(i, M) {
			int b = in();
			ends.pb(b - 1);
		}
		int size = begins.size();
		rep(i, size) {
			int b = begins[i];
			int e = ends[i];
			edges[min(b, e)][max(b, e)] = true;
		}
		
		rep(i, N) {
			edges[i][(i + 1) % N] = true;
		}
		
		ans = INF;
		solve(0, N - 1, 0);
		
		printf("%d\n", ans);
		
		// color
		rep(i, N + 3) color[i] = colcount[i] = 0;
		okans = false;
		coloring(0);
		
		rep(i, N) {
			printf("%d", color[i]);
			if(i != N - 1) printf(" ");
			else puts("");
		}
	}
	return 0;
}
