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

int mat[N][N];
bool mk[N][N];
char ans[N][N];
int n, m;
char c;

int wx[4] = {-1, 0, 0, 1};
int wy[4] = {0, -1, 1, 0};

bool check(int x, int y) {
	for(int k = 0; k < 4; k++) {
		int nx = x + wx[k];
		int ny = y + wy[k];
		if(nx >= 0 && nx < n && ny >= 0 && ny < m && mat[nx][ny] < mat[x][y])return false;
	}
	return true;
}

void next(int x, int y, int &nx, int &ny) {
	int minh = NIL, u = -1;
	for(int k = 0; k < 4; k++) {
		nx = x + wx[k];
		ny = y + wy[k];
		if(nx >= 0 && nx < n && ny >= 0 && ny < m && mat[nx][ny] < minh) {
			minh = mat[nx][ny];
			u = k;
		}
	}
	nx = x + wx[u];
	ny = y + wy[u];
}

char find(int x, int y) {
	int nx = x, ny = y;
	while(true) {
		if(mk[nx][ny]) {
			if(ans[nx][ny] > 0)return ans[nx][ny];
			c++;
			ans[nx][ny] = c - 1;
			return c - 1;
		}
		next(nx, ny, nx, ny);
	}
}

void solve() {
	c = 'a';
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < m; j++) {
			if(check(i, j)) {
				mk[i][j] = true;
			}
		}
	}
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < m; j++) {
			ans[i][j] = find(i, j);
		}
	}

	for(int i = 0; i < n; i++) {
		for(int j = 0; j < m; j++) {
			printf("%c%c", ans[i][j], j == m-1 ? '\n' : ' ');
		}
	}
}

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int T;
	int cases = 1;
	scanf("%d", &T);
	while(T--) {
		memset(mk, false, sizeof(mk));
		memset(ans, 0, sizeof(ans));
		scanf("%d %d", &n, &m);
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
				scanf("%d", &mat[i][j]);
		printf("Case #%d:\n", cases++);
		solve();
	}

	return 0;
}

/*Powered By Lynn-Beta1*/