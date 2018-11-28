#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
#include <set>
#include <map>

using namespace std;

const int MAXN = 1005;

long long T, R, K, N;
long long P[MAXN * 2];
long long sum[MAXN * 2];
int next[MAXN];
long long cost[MAXN];

int path[MAXN], L;
bool vis[MAXN];

int main() {
	cin >> T;
	for(int t = 1 ; t <= T ; t++) {
		cin >> R >> K >> N;
		long long tot = 0;
		for(int i = 0 ; i < N ; i++) {
			cin >> P[i];
			tot += P[i];
			P[i + N] = P[i];
		}
		if (tot <= K) {
			printf("Case #%d: %lld\n",t,(tot * R));
			continue;
		}
		sum[0] = P[0];
		for(int i = 1 ; i < 2 * N ; i++) {
			sum[i] = sum[i - 1] + P[i];
		}
		next[0] = 0;
		while (sum[next[0]] <= K) {next[0]++;}
		long long C = sum[next[0]];
		cost[0] = C - P[next[0]];
		for(int i = 1 ; i < N ; i++) {
			next[i] = next[i - 1];
			C -= P[i - 1];
			while (C <= K) {
				next[i]++;			
				C += P[next[i]];
			}
			cost[i] = C - P[next[i]];
			next[i] %= N;
		}		
		memset(vis,0,sizeof(vis));
		L = 0;
		int v = 0;
		while (!vis[v]) {
			vis[v] = true;
			path[L++] = v;
			v = next[v];
		}
		
		long long ans = 0;
		int ind = 0;
		while (path[ind] != v && R > 0) {
			R--;
			ans += cost[path[ind]];
			ind++;
		}
		if (R > 0) {
			long long cycle = 0;
			for(int i = ind ; i < L ; i++) {
				cycle += cost[path[i]];
			}
			ans += (R / (L - ind)) * cycle;
			R %= (L - ind);
			for(int i = ind ; i < ind + R ; i++) {
				ans += cost[path[i]];
			}
		}
		printf("Case #%d: %lld\n",t,ans);
	}	
	return 0;
}
