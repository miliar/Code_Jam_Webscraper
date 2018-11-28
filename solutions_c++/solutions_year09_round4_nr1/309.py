#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

const int MAXN = 49;
int maxC[MAXN];
int n;
int limit;
char mat[MAXN][MAXN];


int main() {
	freopen("D:\\A-small-attempt0.in", "r", stdin);
	freopen("D:\\A-small-attempt0.out", "w", stdout);
	int i, j, T, cas = 0;
	scanf("%d", &T);
	while (T--) {
		scanf("%d", &n);
		memset(maxC, -1, sizeof(maxC));
		for (i = 0; i < n; ++i) {
			scanf("%s", mat[i]);
			for (j = 0; j < n; ++j) {
				if (mat[i][j] == '1')
					maxC[i] = j;
			}
		}
		int ans = 100000, cnt;
		int seq[MAXN];
		for (i = 0; i < n; ++i) seq[i] = i;
		do {
			for (i = 0; i < n; ++i)
				if (maxC[seq[i]] > i) break;
			if (i < n) continue;
			cnt = 0;
			for (i = 0; i < n; ++i)
				for (j = 0; j < i; ++j)
					if (seq[j] > seq[i]) ++cnt;
			if (cnt < ans) ans = cnt;
		} while (next_permutation(seq, seq + n));
		printf("Case #%d: %d\n", ++cas, ans);
	}
	return 0;
}

		
/*
3
8
11111111
11111110
11111100
11111000
11110000
11100000
11000000
10000000
*/