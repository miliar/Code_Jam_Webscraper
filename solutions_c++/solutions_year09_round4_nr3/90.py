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

const int N = 110;

int p[110][110];
bool mat[110][110];
int T, n, K, cas = 1;

bool check(int i, int j) {
	for(int k = 0; k < K; k++) {
		if(p[i][k] >= p[j][k])return false;
	}
	return true;
}

int pre[110];
bool mk[110];

bool find(int u) {
	for(int i = 0; i < n; i++) {
		if(mat[u][i] && !mk[i]) {
			mk[i] = true;
			if(pre[i] == -1 || find(pre[i])) {
				pre[i] = u;
				return true;
			}
		}
	}
	return false;
}

int gans() {
	memset(pre, -1, sizeof(pre));
	int rec = 0;
	for(int i = 0; i < n; i++) {
		memset(mk, false, sizeof(mk));
		if(find(i))rec++;
	}
	return n - rec;
}

void solve() {
	cin >> n >> K;
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < K; j++)
			cin >> p[i][j];
	}

	memset(mat, 0, sizeof(mat));
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < n; j++) {
			if(check(i, j))mat[i][j] = true;
		}
	}
	printf("Case #%d: %d\n", cas++, gans());
}

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	cin >> T;
	while(T--)solve();

	return 0;
}

/*Powered By Lynn-Beta1*/