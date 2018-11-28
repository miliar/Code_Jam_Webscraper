#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define DEBUG(x) cout << ">>> " << #x << " = " << (x) << endl;
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,a) for(int i=0;i<(a);++i)

#define INF (1<<29)
typedef long long ll;

int N, t, T, L;
char W[1100];

char trans[256] = {0};

bool edges[256][256];

int incnt[256], outcnt[256];

bool vis[256];

void addEdge(char ch1, char ch2) {
	edges[ch1][ch2] = true;
}

void addEdges(char ch1, char ch2) {
	addEdge(ch1, ch2);
	if (trans[ch1]) addEdge(trans[ch1], ch2);
	if (trans[ch2]) addEdge(ch1, trans[ch2]);
	if (trans[ch1] && trans[ch2]) addEdge(trans[ch1], trans[ch2]);
}

bool anyE() {
	REP(i,256) if (incnt[i] || outcnt[i]) return true;
	return false;
}

void dfs(int s) {
	vis[s] = true;
	REP(n,256) if ((edges[s][n] || edges[n][s]) && !vis[n]) dfs(n);
}

int main() {
	trans['o'] = '0';
	trans['i'] = '1';
	trans['e'] = '3';
	trans['a'] = '4';
	trans['s'] = '5';
	trans['t'] = '7';
	trans['b'] = '8';
	trans['g'] = '9';
	scanf("%d", &T);
	t = 0;
	while (t < T) {
		++t;
		REP(i,256) REP(j,256) edges[i][j] = false;
		scanf("%d", &N);
		scanf("%s", W);
		L = strlen(W);
		REP(i,L-1) addEdges(W[i], W[i+1]);
		REP(i,256) { incnt[i] = 0; outcnt[i] = 0; }
		REP(i,256) REP(j,256) {
			if (edges[i][j]) { ++outcnt[i]; ++incnt[j]; }
		}
		int start = 0;
		int res = 0;
		while (anyE()) {
			while (incnt[start] == 0 && outcnt[start] == 0) ++start;
			REP(i,256) vis[i] = false;
			dfs(start);
			int cur = 0;
			int cnt = 0;
			REP(i,256) if (vis[i]) {
				cnt += incnt[i]+outcnt[i];
				cur += abs(incnt[i]-outcnt[i]);
				incnt[i] = 0; outcnt[i] = 0;
			}
			cur /= 2; cnt /= 2;
			if (cur == 0) cur = 1;
			res += cur+cnt;
		}
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}
