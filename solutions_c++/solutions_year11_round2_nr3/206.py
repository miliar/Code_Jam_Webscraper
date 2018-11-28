#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;


const int MAXN = 8+1;
int n, m;
int U[MAXN], V[MAXN];

vector<int> g[MAXN];

int color[MAXN];
int goodColor[MAXN];

int pivot;

bool cmp(int i, int j) {
	if(i > pivot) i -= 2*n;
	if(j > pivot) j -= 2*n;
	return i < j;
}

int h(int u, int v, int start) {
	if(v == start) return 0;

	int mask = (1<<color[u]) | (1<< color[v]);
	for(int i = 0; i < g[v].size(); i++) {
		if(g[v][i] == u) {
			i = (i+1+g[v].size())%g[v].size();
			return mask | h(v, g[v][i], start);
		}
	}


}

bool f(int x, int numColors) {
	if(x == n) {

		int myMask = 0;
		for(int i = 0; i < n; i++) myMask |= (1<<color[i]);
		
		int mask = 0;
		for(int i = 0; i < numColors; i++) mask |= 1<<i;
		if(mask != myMask) return false;

		for(int i = 0; i < n; i++) {
			for(int j = 0; j < g[i].size(); j++) {
				int v = g[i][j];

				if(i == (v-1)%n) continue;
				if(h(i, v, i) != mask) return false;
			}
		}

		for(int i = 0; i < n; i++) goodColor[i] = color[i];
		return true;

	}

	for(int i = numColors-1; i >= 0; i--) {
		color[x] = i;
		if(f(x+1, numColors)) return true;
	}

	return false;

}
void solve(int caseNumber) {
	scanf("%d %d", &n, &m);

	for(int i = 0; i < n; i++) g[i].clear();

	for(int i = 0; i < n; i++) {
		g[i].push_back((i+1)%n);
		g[(i+1)%n].push_back(i);
	}	
	for(int i = 0; i < m; i++) {
		scanf("%d", &U[i]);
		U[i]--;
	}
	for(int i = 0; i < m; i++) {
		scanf("%d", &V[i]);
		V[i]--;
	}

	for(int i = 0; i < m; i++) {
		g[U[i]].push_back(V[i]);
		g[V[i]].push_back(U[i]);
	}

	for(int i = 0; i < n; i++) {
		pivot = i;
		sort(g[i].begin(), g[i].end(), &cmp);
	}

	int res = 0;
	for(int i = 1;; i++) 	{
		if(!f(0, i)) break;
		res = i;
	}

	printf("Case #%d: %d\n", caseNumber, res);
	for(int i = 0; i < n; i++) printf("%d ", goodColor[i]+1);
	printf("\n");



}


int main() {
	//freopen("in.txt", "r", stdin);
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) solve(i);
}