#include <stdio.h>
#define N 10
const int NONE = -10000;
typedef struct
{	int max, tmax;
	int total;
}People;
People p[N];
int main()
{	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int n, s, P;
		scanf("%d %d %d", &n, &s, &P);
		for (int i = 0; i < n; ++i)
			scanf("%d", &p[i].total);
		for (int i = 0; i < n; ++i) {
			if (p[i].total >= 2 && p[i].total <= 28) {
				if (p[i].total %3 == 0) {
					p[i].max = p[i].total /3;
					p[i].tmax = (p[i].total /3) +1;
				} else if (p[i].total %3 == 1) {
					p[i].max = (p[i].total /3) +1;
					p[i].tmax = ((p[i].total -4)/3) +2;
				} else if (p[i].total %3 == 2) {
					p[i].max = (p[i].total +1) /3;
					p[i].tmax = ((p[i].total -2)/3) +2;
				}
			} else {
				if (p[i].total %3 == 0) {
					p[i].max = p[i].total /3;
					p[i].tmax = NONE;
				} else if (p[i].total == 1){
					p[i].max = 1;
					p[i].tmax = NONE;
				} else {
					p[i].max = 10;
					p[i].tmax = NONE;
				}
			}
		}
		printf("Case #%d: ", t);
		int ans = 0;
		if (s == 0) {
			for (int i = 0; i < n; ++i)
				if (p[i].max >= P)
					++ans;
		} else if (s == 1) {
			for (int i = 0; i < n; ++i) {
				int tmp = 0;
				for (int j = 0; j < n; ++j)
					if (i == j) {
						if (p[j].tmax == NONE)
							break;
						if (p[j].tmax >= P)
							++tmp;
					} else {
						if (p[j].max >= P)
							++tmp;
					}
				if (tmp >= ans)	ans = tmp;
			}
		} else if (s == 2) {
			for (int i = 0; i < n; ++i) {
				int tmp = 0;
				for (int j = 0; j < n; ++j)
					if (i != j) {
						if (p[j].tmax == NONE)
							break;
						if (p[j].tmax >= P)
							++tmp;
					} else {
						if (p[j].max >= P)
							++tmp;
					}
				if (tmp >= ans)	ans = tmp;
			}
		} else {
			for (int i = 0; i < n; ++i)
				if (p[i].tmax >= P)
					++ans;
		}
		printf("%d\n", ans);
	}
	return 0;
}
