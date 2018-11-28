#include <stdio.h>

int main()
{
	int cnt, T, t, N, S, p, v, l, r;

	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		scanf("%d%d%d", &N, &S, &p);
		l = p * 3 - 4; r = l + 2;
		if (l < 2) l = 2;

		cnt = 0;
		while (N--) {
			scanf("%d", &v);
			if (v >= l && v < r && S) {
				S--;
				cnt++;
			}
			else if (v >= r) cnt++;
		}
		printf("Case #%d: %d\n", t, cnt);
	}
	return 0;
}
