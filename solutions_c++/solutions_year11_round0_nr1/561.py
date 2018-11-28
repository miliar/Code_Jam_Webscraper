#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;
const int MAXN = 1007;

int main() {
	//freopen("in", "r", stdin);
	//freopen("out", "w", stdout);
	int t, n, var = 0;
	scanf("%d", &t);
	while (t -- ) {
		scanf("%d", &n);
		char ch;
		int pos;
		int T[2] = {0}, P[2] = {1, 1};
		int cur;
		for (int i = 0 ; i < n ; i ++ ) {
			scanf(" %c%d", &ch, &pos);
			cur = ch=='O' ? 0 : 1;
			if (T[cur] >= T[1-cur]) {
				T[cur] += abs(pos - P[cur]) + 1;
			} else {
				int left = T[1-cur] - T[cur];
				int need = abs(pos - P[cur]);
				if (need <= left) T[cur] = T[1-cur] + 1;
				else {
					T[cur] = T[cur] + need + 1;
				}
			}
			P[cur] = pos;
		}
		printf("Case #%d: %d\n", ++var, max(T[0], T[1]));
	}
	return 0;
}