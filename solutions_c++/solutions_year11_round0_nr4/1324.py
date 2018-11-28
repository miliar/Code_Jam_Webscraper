


/*
	Prob: (Google code jam 2011 - Qualification Round - D)
	Author: peanut
	Time: 07/05/11 20:30
	Description: >_<
*/

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

const int MaxN = 1111;

int T, N, c, s;
int next[MaxN];
bool v[MaxN];

int main() {
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	
	scanf("%d", &T);
	for (int cs = 1; cs <= T; ++ cs) {
		scanf("%d", &N);
		for (int k = 1; k <= N; ++ k)
			scanf("%d", &next[k]);
		memset(v, 1, sizeof(v));
		s = 0;
		for (int k = 1; k <= N; ++ k) 
			if (v[k]) {
				c = 1;
				for (int cur = next[k]; cur != k; cur = next[cur]) {
					++ c;
					v[cur] = false;
				}
				if (c > 1) s = c + s;
			}
		printf("Case #%d: %d.000000\n", cs, s);
	}
	
	return 0;
}
