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

int process() {
	int N;
	scanf("%d", &N);
	
	int c;
	int all_xor = 0;
	int sum = 0;
	int menor = 99999999;
	for (int i = 0; i < N; ++i) {
		scanf("%d", &c);
		sum += c;
		all_xor ^= c;
		menor = min(menor, c);
	}
	
	if (all_xor) printf("NO\n");
	else printf("%d\n", sum - menor);
}

int main() {
	
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	
	int T;
	scanf("%d", &T);
	for (int i = 0 ; i < T ; i++) {
		printf("Case #%d: ", i+1);
		process();
	}
	
	return 0;
}
