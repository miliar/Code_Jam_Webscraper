#include <math.h>
#include <stdio.h>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <algorithm>
#include <ctype.h>
#include <hash_set>

using namespace std;
using namespace stdext;

#define FOR(i, a, b) for (int _n(b), i(a); i < _n; i++)
#define REP(i, n) FOR(i, 0, n)
#define ALL(a) a.begin(), a.end()
#define SORT(a) sort(ALL(a))
#define pb push_back
#define INF 1000000

typedef pair< int, int > pii;

int t;

void init() {
	freopen("input_2.txt", "rt", stdin);
	scanf("%d\n", &t);
}

void find() {
	int n,m;
	cin >> n >> m;
	vector< vector< int > > a(n+2);
	vector< vector< int > > b(n+2);
	vector< vector< char > > db(n+2);
	REP(i, n+2) {
		a[i] = vector< int >(m+2, 0);
		b[i] = vector< int >(m+2, 0);
		db[i] = vector< char >(m+2, 0);
		a[i][0] = INF;
		a[i][m+1] = INF;
		b[i][0] = INF;
		b[i][m+1] = INF;
	}
	REP(j, m+2) {
		a[0][j] = INF;
		a[n+1][j] = INF;
		b[0][j] = INF;
		b[n+1][j] = INF;
	}
	FOR(i,1,n+1) FOR(j,1,m+1) cin >> a[i][j];

	int di[] = {-1,0,0,1};
	int dj[] = {0,-1,1,0};
	FOR(i,1,n+1) {
		FOR(j,1,m+1) {
			int d[4];
			REP(k,4) d[k] = a[i+di[k]][j+dj[k]];
			int min = 0;
			FOR(k,1,4) if (d[k] < d[min]) min = k;
			if (d[min] < a[i][j]) b[i][j] = min;
			else b[i][j] = -1;
		}
	}
	char id = 'a';
	FOR(i,1,n+1) {
		FOR(j,1,m+1) {
			if (db[i][j] != 0) continue;

			int ii = i;
			int jj = j;
			while (b[ii][jj] != -1) {
				int t = ii + di[b[ii][jj]];
				jj += dj[b[ii][jj]];
				ii = t;
			}
			queue< pii > q;
			q.push(pii(ii,jj));
			while (!q.empty()) {
				pii top = q.front();
				q.pop();
				db[top.first][top.second] = id;
				REP(k,4) {
					ii = top.first+di[k];
					jj = top.second+dj[k];
					if (b[ii][jj] == (3-k)) {
						q.push(pii(ii,jj));
					}
				}
			}
			id++;
		}
	}
	FOR(i,1,n+1) {
		FOR(j,1,m+1) {
			cout << db[i][j] << (j==m ? "\n" : " ");
		}
	}
}

void solve() {
	freopen("out_2.txt", "wt", stdout);
	REP(i, t) {
		printf("Case #%d:\n", i+1);
		find();
	}
}

int main() {
	init();
	solve();
}