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
	int tb = 0, to = 0, pb = 1, po = 1, t = 0;
	
	char c[5];
	int next;
	
	int dist;
	for (int i = 0; i < N; ++i) {
		scanf("%s %d", c, &next);
		if (c[0] == 'B') {
			dist = abs(next - pb) + 1;
			pb = next;
			t = tb = max(tb+dist, t+1);
		} else {
			dist = abs(next - po) + 1;
			po = next;
			t = to = max(to+dist, t+1);
		}
	}
	return t;
}

int main() {
	
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int T;
	scanf("%d", &T);
	for (int i = 0 ; i < T ; i++) {
		printf("Case #%d: %d\n", i+1, process());
	}
	
	return 0;
}
