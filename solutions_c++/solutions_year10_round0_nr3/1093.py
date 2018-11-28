#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	
	int T, R, k, N, g[1001];
	int rsize[1001], rid[1001];

	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d%d%d", &R, &k, &N);
		for (int n = 0; n < N; ++n) scanf("%d", g + n);
		// make rounds
		memset(rid, 0, sizeof(rid));
		int i = 0, nr = 0, repeat;
		while (true) {
			if (rid[i]) {
				repeat = rid[i] - 1;
				break;
			}
			rid[i] = nr + 1;
			int s = 0, start = i;
			while (s + g[i] <= k) {
				s += g[i];
				i = (i + 1) % N;
				if (i == start) break;
			}
			rsize[nr++] = s;
		}
		// make money
		double money = 0.0;
		if (R < repeat) {
			for (int i = 0; i < R; ++i) money += rsize[i];
		} else {
			for (int i = 0; i < repeat; ++i) money += rsize[i];
			R -= repeat;
			double x = 0;
			int csize = nr - repeat;
			for (int i = repeat; i < nr; ++i) x += rsize[i];
			money += x * 1.0 * (R / csize);
			R %= csize;
			for (int i = 0; i < R; ++i) money += rsize[repeat + i];
		}
		// output
		printf("Case #%d: %.0lf\n", t, money); 
	}
	return 0;
}