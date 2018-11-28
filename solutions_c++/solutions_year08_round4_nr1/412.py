#include <stdio.h>
int ins[10010][2], lea[10010], cha[10010][2], m, v;
inline int calc(int t, int l, int r) {
	if (t == 0)
		return l | r;
	else
		return l & r;
}
void work(int nod) {
	if (nod <= (m - 1) / 2) {
		work(nod << 1);
		work(nod << 1 | 1);
		cha[nod][0] = m + 1; cha[nod][1] = m + 1;
		int l, r, x;
		for (l = 0; l < 2; ++l)
			for (r = 0; r < 2; ++r) {
				x = calc(ins[nod][0], l, r);
				if (cha[nod << 1][l] + cha[nod << 1 | 1][r] < cha[nod][x])
					cha[nod][x] = cha[nod << 1][l] + cha[nod << 1 | 1][r];
				if (ins[nod][1] == 1) {
					x = calc(ins[nod][0] ^ 1, l, r);
					if (cha[nod << 1][l] + cha[nod << 1 | 1][r] + 1 < cha[nod][x])
						cha[nod][x] = cha[nod << 1][l] + cha[nod << 1 | 1][r] + 1;
				}
			}
	}
	else {
		cha[nod][lea[nod]] = 0;
		cha[nod][lea[nod] ^ 1] = m + 1;
	}
}
int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int cas, tes, i;
	for (scanf("%d", &cas), tes = 1; tes <= cas; ++tes) {
		scanf("%d%d", &m, &v);
		for (i = 1; i <= (m - 1) / 2; ++i)
			scanf("%d%d", &ins[i][0], &ins[i][1]);
		for (i = (m - 1) / 2 + 1; i <= m; ++i)
			scanf("%d", &lea[i]);
		work(1);
		printf("Case #%d: ", tes);
		if (cha[1][v] > m)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", cha[1][v]);
	}
	return 0;
}