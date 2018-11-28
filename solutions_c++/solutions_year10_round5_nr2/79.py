#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iostream>
#include <queue>

using namespace std;

const int maxn=100000;
vector<int> adj[maxn];
vector<int> cost[maxn];

const int inf=1000000000;

int main() 
{
	int test_num;
	scanf("%d", &test_num);
	for (int case_num = 1; case_num <= test_num; case_num++) {
		long long L;
		int n;
		cin>>L>>n;
		vector<int> B(n);
		for (int i = 0; i < n; i++)
			cin >> B[i];
		sort(B.begin(),B.end());
		n --;
		int B0 = B[n];
		for (int i = 0; i < B0; i++) {
			adj[i].clear();
			cost[i].clear();
		}
		for (int i = 0; i < B0; i++) {
			for (int j = 0; j < n; j++) {
				int sum = i + B [j];
				adj[i].push_back(sum >= B0 ? sum - B0 : sum);
				cost[i].push_back(1 - (sum >= B0 ? 1 : 0));
			} 
		}
		vector<int> dist(B0, inf);
		vector<bool> inQ(B0, false);
		dist[0] = 0;
		queue<int> Q;
		Q.push(0);
		inQ[0] = true;
		while (!Q.empty()) {
			int p = Q.front();
			inQ[p] = false;
			Q.pop();
			for (int i = 0; i < adj[p].size(); i++) {
				int q = adj[p][i];
				if (dist[q] > dist[p] + cost[p][i]) {
					dist[q] = dist[p] + cost[p][i];
					if (!inQ[q]) {
						inQ[q] = true;
						Q.push(q);
					}
				}
			}
		}
		int target = L % B0;
		if (dist[target] == inf) {
			printf("Case #%d: IMPOSSIBLE\n", case_num);
		} else {
			printf("Case #%d: %lld\n", case_num, L / B0 + dist[target]);
		}
	}
}
