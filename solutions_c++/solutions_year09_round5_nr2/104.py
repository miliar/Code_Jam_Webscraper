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

string p;
int s[26];

int cal() {
	int rec = 0, d = 1;
	for(int i = 0; i < p.size(); i++) {
		if(p[i] == '+') {
			rec += d;
			d = 1;
		}
		else d *= s[p[i] - 'a'];
	}
	rec += d;
	return rec;
}

int n, K;
string w[110];
int ans;
int K1;

void dfs(int cnt) {
	if(cnt == K1) {
		ans += cal();
		ans %= 10009;
		return;
	}
	for(int i = 0; i < n; i++) {
		for(int k = 0; k < w[i].size(); k++) {
			s[w[i][k] - 'a']++;
		}
		dfs(cnt+1);
		for(int k = 0; k < w[i].size(); k++) {
			s[w[i][k] - 'a']--;
		}
	}
}

int cases = 1;
void solve() {
	cin >> p >> K;
	cin >> n;
	for(int i = 0; i < n; i++) {
		cin >> w[i];
	}

	printf("Case #%d:", cases++);
	for(int i = 0; i < K; i++) {
		ans = 0;
		memset(s, 0, sizeof(s));
		K1 = i + 1;
		dfs(0);
		printf(" %d", ans);
	}
	printf("\n");
}

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int T;
	cin >> T;
	while(T--)solve();

	return 0;
}

/*Powered By Lynn-Beta1*/