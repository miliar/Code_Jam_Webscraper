#include <cstdio>
#include <algorithm>

// final version

int compare (const void* a, const void* b) {
	return *(int*)b - *(int*)a;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T, N, S, p;
	int a[200], i, m, n;
	scanf("%d", &T);
	for (int case_i = 1; case_i <= T; ++case_i) {
		scanf("%d%d%d", &N, &S, &p);
		for (i = 0; i < N; ++i)
			scanf("%d", &a[i]);
		qsort(a, N, sizeof(int), compare);
		for (i = 0, n = 0; i < N; ++i) {
			m = a[i] / 3;
			if (a[i] % 3 == 1) { // (m, m, m+1)
				if (m + 1 < p || m + 1 > 10)
					break;
			} else
				if (a[i] % 3) {
					if (m + 2 == p && m + 2 <= 10) 
						if (S > 0)
							--S; // (m, m, m+2)
						else
							break;
					else if (m + 1 < p || m + 1 > 10) // (m, m+1, m+1)
						break;
				} else
					if (m + 1 == p && m + 1 <= 10)
						if (S > 0 && m - 1 >= 0)
							--S; // (m+1, m, m-1)
						else
							break;
					else if (m < p) // (m, m, m)
						break;
			++n;
		}
		printf("Case #%d: %d\n", case_i, n);
	}
}