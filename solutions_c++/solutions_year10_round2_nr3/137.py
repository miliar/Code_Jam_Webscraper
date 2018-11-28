#include <cstdio>
#include <algorithm>
using namespace std;

typedef long long ull;

#define MOD 100003


ull mem[505][505];
ull memchoose[505][505];

ull choose(ull k, ull n) {
	if (memchoose[k][n] == -1) {
		if (k == 0 || n == 0 || k == n) {
			memchoose[k][n] = 1;
		} else {
			memchoose[k][n] = (choose(k-1, n-1) + choose(k, n-1)) % MOD;
		}
	}
	return memchoose[k][n];
}

ull count(ull n, ull rank) {
	//printf("%lld %lld\n", n, rank);
	if (mem[n][rank] == -1) {
		if (rank > n-1) {
			mem[n][rank] = 0;
		} else if (rank == 1) {
			mem[n][rank] = 1;
		} else {
			mem[n][rank] = 0;

			for (ull a = max(1LL, 2*rank-n); a < rank; ++a) {
				//printf("a:%d max.x:%lld\n", a, n-(rank-a));
				ull cnt = (count(rank, a) * choose(rank-a-1, n-rank-1)) % MOD;
				//printf("x:%lld cnt:%lld\n", rank, cnt);
				mem[n][rank] += cnt;
				mem[n][rank] %= MOD;
			}

			/*for (int x = 2; x < n; ++x) {
				for (int a = x+rank-n; a < x; ++a) {
				}
			}*/
		}
	}
	//printf("%lld %lld => %lld\n", n, rank, mem[n][rank]);
	return mem[n][rank];
}


int main() {
	for (int i = 0; i < 505; ++i) {
		for (int j = 0; j < 505; ++j) {
			mem[i][j] = -1;
			memchoose[i][j] = -1;
		}
	}

	int t;
	ull n;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; ++tt) {
		scanf("%lld", &n);
		ull res = 0;
		for (ull rank = 1; rank < n; ++rank) {
			res += count(n, rank);
			res %= MOD;
		}
		printf("Case #%d: %lld\n", tt, res);
	}
}
