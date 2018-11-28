#include <cstdio>
#include <memory>

int casei, cases, n;
long long NA, NB, NC, ND, px0, py0, m, nowx, nowy, ans;
long long total[3][3];

inline void init() {
	scanf("%d%I64d%I64d%I64d%I64d%I64d%I64d%I64d", &n, &NA, &NB, &NC, &ND, &px0, &py0, &m);
}

inline void process() {
	memset(total, 0, sizeof total);
	nowx = px0; nowy = py0;
	for (int i = 0; i < n; ++i) {
		++total[nowx % 3][nowy % 3];
		nowx = (NA * nowx + NB) % m;
		nowy = (NC * nowy + ND) % m;
	}

	ans = 0;
	for (int i1 = 0; i1 < 3; ++i1)
	for (int j1 = 0; j1 < 3; ++j1)
		for (int i2 = 0; i2 < 3; ++i2)
		for (int j2 = 0; j2 < 3; ++j2)
			for (int i3 = 0; i3 < 3; ++i3) if ((i1 + i2 + i3) % 3 == 0)
			for (int j3 = 0; j3 < 3; ++j3) if ((j1 + j2 + j3) % 3 == 0)
				if ((i1 != i2 || i2 != i3 || i3 != i1) || (j1 != j2 || j2 != j3 || j3 != j1))
					ans += total[i1][j1] * total[i2][j2] * total[i3][j3];
	ans /= 6;

	for (int i1 = 0; i1 < 3; ++i1)
	for (int j1 = 0; j1 < 3; ++j1)
		ans += total[i1][j1] * (total[i1][j1] - 1) * (total[i1][j1] - 2) / 6;

	for (int i1 = 0; i1 < 3; ++i1)
	for (int j1 = 0; j1 < 3; ++j1)
		for (int i3 = 0; i3 < 3; ++i3) if ((i1 + i1 + i3) % 3 == 0)
		for (int j3 = 0; j3 < 3; ++j3) if ((j1 + j1 + j3) % 3 == 0)
			if (i1 != i3 || j1 != j3)
				ans -= total[i1][j1] * (total[i1][j1] - 1) * total[i3][j3] / 2;
}

inline void print() {
	printf("Case #%d: %I64d\n", casei, ans);
}

int main() {
//	freopen("in.txt", "r", stdin);
//	freopen("", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		init();
		process();
		print();
	}
}
