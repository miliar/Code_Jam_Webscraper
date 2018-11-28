#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cassert>
#include <string>
#include <cstdio>
#include <cmath>
#include <stack>
#define sz(x) ((int)(x.size()))
#define all(c) (c).begin(),(c).end() 
#define pb push_back 
#define mp make_pair
#define foreach(T, x, it) for (T::iterator it = x.begin(); it != x.end(); ++it)
using namespace std;
typedef long long lint;
typedef pair<int, int> pii;
typedef vector<int> vi;

int H, W;
vector<vi> A, Use;
vector<string> Ans;

const int di[] = {-1, 0, 0, 1};
const int dj[] = {0, -1, 1, 0 };

vector<pii> G[200][200];

void AddEdge(int u1, int u2, int v1, int v2) {
	G[u1][u2].pb(mp(v1, v2));
	G[v1][v2].pb(mp(u1, u2));
}

void DFS(int i, int j, char cur) {
	Use[i][j] = true;
	Ans[i][j] = cur;
	
	for (int k = 0; k < sz(G[i][j]); ++k) {
		int ni = G[i][j][k].first;
		int nj = G[i][j][k].second;
		if (Use[ni][nj]) continue;
		DFS(ni, nj, cur);
	}
}

void Make() {
	for (int i = 0; i < H; ++i) {
		for (int j = 0; j < W; ++j) {

			int ii = -1, jj = -1;
			for (int k = 0; k < 4; ++k) {
				int ni = i + di[k];
				int nj = j + dj[k];
				if (ni < 0 || ni >= H || nj < 0 || nj >= W) continue;
				//if (Use[ni][nj]) continue;
				if (A[ni][nj] >= A[i][j]) continue;
				if (ii == -1 || A[ni][nj] < A[ii][jj]) {
					ii = ni;
					jj = nj;
				}
			}

			if (ii != -1) {
				AddEdge(i, j, ii, jj);
			}
		}
	}
		
	

}

void Solve(int num) {
	printf("Case #%d:\n", num);
	cin >> H >> W;
	A.assign(H, vi(W, 0));
	for (int i = 0; i < H; ++i) {
		for (int j = 0; j < W; ++j) {
			cin >> A[i][j];
			G[i][j].clear();
		}
	}


	Use.assign(H, vi(W, 0));
	Ans.assign(H, string(W, '.'));
	char cur = 'a';
	Make();
	for (int i = 0; i < H; ++i) {
		for (int j = 0; j < W; ++j) {
			if (Use[i][j]) continue;
			
			DFS(i, j, cur);
			cur++;
		}
	}
	for (int i = 0; i < H; ++i) {
		for (int j = 0; j < W; ++j) {
			cout << Ans[i][j];
			if (j != W - 1) cout << " ";
		}
		cout << endl;
	}
}

int main() {	
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int tst;
	cin >> tst;
	for (int i = 1; i <= tst; ++i)
		Solve(i);
	return 0;
}

