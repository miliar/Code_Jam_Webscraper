#include <vector>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cassert>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#pragma comment(linker, "/STACK:10000000")
#define For(i,l,h) for (int i = (l); i < (h); ++i)
#define ForU(i,l,h) for (int i = (l); i <= (h); ++i)
#define tr(T, v, it) for (T::iterator it = v.begin(); it != v.end(); ++it) 
#define sz(x) ((int)(x.size()))
#define all(c) (c).begin(),(c).end() 
#define pb push_back 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
using namespace std;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef vector<string> vs; 
typedef vector<vs> vvs; 
typedef pair<int,int> pii; 
typedef vector<pii> vpii; 
typedef map<string, int> msi;
typedef long long lint;
const int MAXN = 100;
const double eps = 1e-8;
const double pi = acos(-1.0);

vector<string> S;
int N, M;
vvi G;
vi C, Prev, Next, Use;

void AddEdge(int u, int v) {
	G[u].pb(v);
	G[v].pb(u);
}

void Check(int i1, int j1, int i2, int j2) {
	if (i1 < 0 || j1 < 0 || i2 < 0 || j2 < 0) return;
	if (i1 >= N || j1 >= M || i2 >= N || j2 >= M) return;
	if (S[i1][j1] == 'x' || S[i2][j2] == 'x') return;
	AddEdge(i1 * M + j1, i2 * M + j2);
}

void DFS(int u, int c) {
	C[u] = c;
	for (int i = 0; i < sz(G[u]); ++i) {
		int v = G[u][i];
		if (!C[v]) {
			DFS(v, 3 - c);
		}
		else {
			assert(C[v] == 3 - c);
		}
	}
}

bool Build(int u) {
	Use[u] = true;
	for (int i = 0; i < sz(G[u]); ++i) {
		int v = G[u][i];
		if (Prev[v] == -1 || !Use[Prev[v]] && Build(Prev[v])) {
			Next[u] = v;
			Prev[v] = u;
			return true;
		}
	}
	return false;
}

void Solve(int num) {
	printf("Case #%d: ", num);
	cin >> N >> M;
	G.clear();
	G.assign(N * M, vi());
	S.clear();
	for (int i = 0; i < N; ++i) {
		string s;
		cin >> s;
		S.pb(s);
	}
	int cnt = 0;
	for (int i = 0; i < N; ++i) 
		for (int j = 0; j < M; ++j) {
			if (S[i][j] == 'x') ++cnt;
		}
	for (int i = 0; i < N; ++i) 
		for (int j = 0; j < M; ++j) {
			Check(i, j, i, j - 1);
			Check(i, j, i - 1, j - 1);
			Check(i, j, i, j + 1);
			Check(i, j, i - 1, j + 1);
		}
	C.assign(N * M, 0);
	for (int i = 0; i < N * M; ++i) {
		if (C[i]) continue;
		DFS(i, 1);
	}
	int r = 0;	
	Prev.assign(N * M, -1);
	Next.assign(N * M, -1);
	for (int i = 0; i < N * M; ++i) {
		if (C[i] == 2) continue;
		Use.assign(N * M, 0);
		if (Build(i)) ++r;
	}
	int ans = N * M - r - cnt;
	printf("%d", ans);
	printf("\n");	
}


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);	
	int tst;
	cin >> tst;
	for (int i = 1; i <= tst; ++i) Solve(i);
	return 0;
}

