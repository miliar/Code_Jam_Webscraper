#include <cstdio>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
using namespace std;

int N, K;
long long data[200][50];
int adj[200][200], match1[200], used2[200], dist[200][2], seen[200];

int dfs(int x) {
	if (seen[x]) return 0;
	seen[x] = 1;
	for (int i = 0; i < N; i++) {
		if (!adj[i][x]) continue;
		if (match1[i] == -1 || dfs(match1[i])) {
			used2[x] = 1;
			match1[i] = x;
			return 1;
		}
	}
	return 0;
}

int main() {
	int nTests;
	scanf("%d",&nTests);
	for (int test=1;test<=nTests;test++) {
		if (1) fprintf(stderr,"Case %d/%d\n",test,nTests);
		
		scanf("%d%d",&N,&K);
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < K; j++) {scanf("%lld",&data[i][j]);}
		}
		for (int i = 0; i < N; i++) {
			used2[i] = 0;
			match1[i] = -1;
			for (int j = 0; j < N; j++) {
				adj[i][j] = 1;
				for (int k = 0; k < K; k++) {
					adj[i][j] = adj[i][j] && (data[i][k] < data[j][k]);
				}
			}
		}
		int success=1,ans=N;
		while (success) {
			success=0;
			for (int i = 0; i < N; i++) {
				seen[i] = 0;
			}
			for (int i = 0; i < N; i++) {
				if (!used2[i] && dfs(i)) {
					ans--;success=1; break;
				}
			}
		}
		
		printf("Case #%d: %d\n",test,ans);
	}
}
