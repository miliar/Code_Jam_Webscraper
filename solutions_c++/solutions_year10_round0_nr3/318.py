#include <cstdio>
#include <cstring>

using namespace std;

#define MAXN 1000
#define PACK 1000

long test, tests;
long R, K, N;
long g[MAXN];

long w1[MAXN], wk[MAXN];
__int64 c1[MAXN], ck[MAXN];

void init(long start) {
    long left = K;

    long next = start;
    for (long i = 0; g[next] <= left && i < N; i++) {
        left -= g[next];
        next++;
		if (next == N)
			next = 0;
    }
    w1[start] = next;
    c1[start] = K - left;
}

void move1(long &state, __int64 &sum) {
    sum = sum + c1[state];
	state = w1[state];
}
void moveK(long &state, __int64 &sum) {
    sum = sum + ck[state];
	state = wk[state];
}

void solve() {
    scanf("%ld%ld%ld", &R, &K, &N);
    for (int i = 0; i < N; i++)
        scanf("%ld", &g[i]);

    for (int start = 0; start < N; start++)
        init(start);

	for (int i = 0; i < N; i++) {
		wk[i] = w1[i];
		ck[i] = c1[i];
		for (int step = 2; step <= PACK; step++)
			move1(wk[i], ck[i]);
	}

    long state = 0;
    __int64 cost = 0;
    while (R >= PACK) {
        moveK(state, cost);
        R -= PACK;
    }
    while (R > 0) {
        move1(state, cost);
        R -= 1;
    }
	printf("Case #%ld: %I64d\n", test, cost);
}

int main() {
    freopen("C-large.in", "rt", stdin);
    freopen("data.out", "wt", stdout);

    scanf("%d", &tests);
    for (test = 1; test <= tests; test++)
        solve();

    return 0;
}
