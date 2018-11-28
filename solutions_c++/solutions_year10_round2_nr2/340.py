#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <queue>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

int x[10000];
int v[10000];
bool imp[10000];
int N, K, B, T;

int process() {
	
	scanf("%d%d%d%d", &N, &K, &B, &T);
	for (int i = 0 ; i < N ; i++) {
		scanf("%d", &x[i]);
	}
	for (int i = 0 ; i < N ; i++) {
		scanf("%d", &v[i]);
	}
	
	int possiveis = 0;
	for (int i = 0 ; i < N ; i++) {
		imp[i] = v[i]*T + x[i] < B;
		if (!imp[i]) possiveis++;
	}
	if (possiveis < K) {
		printf("IMPOSSIBLE\n");
	} else {
		int impossiveis = 0;
		int res = 0;
		for (int i = N-1 ; i >= 0 ; i--) {
			if (!K) break;
			
			if (imp[i]) {
				impossiveis++;
			} else {
				res += impossiveis;
				K--;
			}
		}
		printf("%d\n", res);
	}
}
int main() {
	
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	int T;
	scanf("%d", &T);
	for (int i = 0 ; i < T ; i++) {
		printf("Case #%d: ", i+1);
		process();
	}
	
	return 0;
}
