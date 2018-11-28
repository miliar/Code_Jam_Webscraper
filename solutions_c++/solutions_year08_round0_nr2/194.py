#include <stdio.h>
#include <string.h>

int i, j, k, t, T, m;
int n, nl, nr, x, y;
int pl, pr;

struct st {
	int b;
	int e;
};

st l[105], r[105];

int al[2000], ar[2000];
int kl, kr;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &T);
	for (t = 1; t <= T; t ++) {
		scanf("%d" ,&m);
		scanf("%d %d", &nl, &nr);
		for (i = 0; i < nl; i ++) {
			scanf("%d:%d", &x, &y);
			l[i].b = x * 60 + y;
			scanf("%d:%d", &x, &y);
			l[i].e = x * 60 + y;
		}
		for (i = 0; i < nr; i ++) {
			scanf("%d:%d", &x, &y);
			r[i].b = x * 60 + y;
			scanf("%d:%d", &x, &y);
			r[i].e = x * 60 + y;
		}

		memset(al, 0, sizeof(al));
		memset(ar, 0, sizeof(ar));
		pl = pr = 0;
		kl = kr = 0;
		for (i = 0; i < 2000; i ++) {
			for (j = 0; j < nr; j ++) {
				if (r[j].e == i) {
					al[i+m] ++;
				}
			}
			kl += al[i];
			for (j = 0; j < nl; j ++) {
				if (l[j].b == i) {
					kl --;
					if (kl < 0) {
						kl = 0;
						pl ++;
					}
				}
			}

			for (j = 0; j < nl; j ++) {
				if (l[j].e == i) {
					ar[i+m] ++;
				}
			}
			kr += ar[i];
			for (j = 0; j < nr; j ++) {
				if (r[j].b == i) {
					kr --;
					if (kr < 0) {
						kr = 0;
						pr ++;
					}
				}
			}
		}

		printf("Case #%d: %d %d\n", t, pl, pr);
	}
	return 0;
}



