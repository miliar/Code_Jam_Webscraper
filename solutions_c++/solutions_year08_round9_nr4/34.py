#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <sstream>
#include <iostream>
#include <queue>
#include <set>
#include <map>

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define LD long double
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define DFOR(a,b) for(int a=b-1;a>=0;a--)
#define CLR(a,b) memset(a,b,sizeof(a))

using namespace std;

#define PII pair<int, int>

int d[33][33];

queue<PII> q;

int n, m;
char a[33][33];
int previ[33][33], prevj[33][33];
bool used[33][33];

int di[] = {0,0,-1,1};
int dj[] = {-1,1,0,0};

void push(int i, int j, int pi, int pj, int dist) {
	if (d[i][j] == -1) {
		d[i][j] = dist;
		q.push(MP(i,j));
		previ[i][j] = pi;
		prevj[i][j] = pj;
	}
}

void bfs() {
	while (!q.empty()) {
		int i = q.front().first;
		int j = q.front().second;
		q.pop();
		FOR(dir, 4) {
			int ii = i + di[dir];
			int jj = j + dj[dir];
			if (ii < 0 || jj < 0 || ii >= n || jj >= m) continue;
			if (a[ii][jj] == '#' || a[ii][jj] == 'T') push(ii, jj, i, j, d[i][j]+1);
		}
	}
}

void solvecase() {
	scanf("%d%d", &n, &m);
	FOR(i, n) scanf("%s", a[i]);
	
	CLR(d, -1);
	CLR(used, 0);
	push(0,0,-1,-1,0);
	bfs();
	
	int ti = -1, tj = -1;
	int res = 0;

	FOR(i, n) FOR(j, m) {
		if ((i != 0 || j != 0) && a[i][j] == 'T') {
			ti = i;
			tj = j;
		}
	}

	if (ti == -1) {
		FOR(i, n) FOR(j, m) if (a[i][j] != '.') res += d[i][j];
	} else {
		int I = ti, J = tj;
		while (I != 0 || J != 0) {
			used[I][J] = true;
			res += d[I][J];
			int ti = I;
			int tj = J;
			I = previ[ti][tj];
			J = prevj[ti][tj];
		}
		CLR(d, -1);
		push(0,0,-1,-1,0);
		push(ti,tj,-1,-1,0);
		bfs();
		FOR(i, n) FOR(j, m) if (a[i][j] != '.' && !used[i][j]) res += d[i][j];
	}
	printf("%d", res);
}


void solve() {
	int n;
	scanf("%d\n", &n);
	FOR(i, n) {
		printf("Case #%d: ", i+1);
		solvecase();
		printf("\n");
	}
}

int main() {
	freopen("x", "rt", stdin);
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}