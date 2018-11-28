#include <vector>
#include <cstdio>
#include <algorithm>
#include <queue>

using namespace std;

int prime[1000001]; // 0 -> prime
vector <vector <int> > graph;
vector <int> check;

void bfs(int num) {
	queue<int> Q;
	Q.push(num);
	check[num] = 1;

	while (!Q.empty()) {
		int v = Q.front(); Q.pop();
		for (int i = 0; i < graph[v].size(); ++i) {
			if (check[graph[v][i]] == 0) {
				check[graph[v][i]] = 1;
				Q.push(graph[v][i]);
			}
		}
	}
}

int main() {
	
	int T;
	int A, B, P;
	scanf("%d", &T);

	for (long long i = 2; i <= 1000000; ++i) {
		if (prime[i] == 0) {
			for (long long j = i * i; j <= 1000000; j += i)
				prime[j] = 1;
		}
	}
	for (int cn = 1; cn <= T; ++cn) {
		scanf("%d %d %d", &A, &B, &P);
		graph.assign(B + 1, vector <int> ());
		check.assign(B + 1, 0);

		for (int i = P; i <= B - A; ++i) {
			if (prime[i]) continue;
			int start = ((A + (i - 1)) / i) * i;
			for (int j = start + i; j <= B; j += i) {
				graph[start].push_back(j);
				graph[j].push_back(start);
			}
		}

		int ret = 0;
		for (int i = A; i <= B; ++i) {
			if (check[i] == 0) {
				ret++;
				bfs(i);
			}
		}
		printf("Case #%d: %d\n", cn, ret);
	}
}
