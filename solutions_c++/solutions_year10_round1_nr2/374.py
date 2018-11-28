#include <cstdio>
#include <cstdlib>
#include <algorithm>
#define MAXN 105
#define MAX 256
#define INF 900900900

using namespace std;

int D, I, M, N;
int v[MAXN];
int pd[MAXN][MAX];

//0 - delete
//1 - insert
//2 - muda valor

int f (int p, int va) {
	if (p == N)
		return 0;
	if (pd[p][va] != -1)
		return pd[p][va];
	int &r = pd[p][va];
	r = f (p+1, va) + D;
	if (M != 0)
		r = min (r, f (p+1, v[p]) + (max(abs(va-v[p])+1, 0)/M) * I);
	for (int i = 0; i < MAX; i++)
		if (abs (va-i) <= M)
			r = min (r, f(p+1, i) + abs(v[p]-i));
	if (M != 0)
		for (int i = 0; i < MAX; i++) {
			int tmp = max (abs(va-i)-1, 1)/M + 1;
			for (int j = 0; j < MAX; j++)
				if (abs (j-i) <= M)
					r = min (r, f(p+1, j) + tmp * I + abs (v[p]-j));
		}
	return r;
}

int main () {
	int T;
	scanf ("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf ("%d%d%d%d", &D, &I, &M, &N);
		for (int i = 0; i < N; i++) {
			scanf ("%d", &v[i]);
			for (int j = 0; j < MAX; j++)
				pd[i][j] = -1;
		}
		int b = INF;
		for (int i = 0; i < MAX; i++)
			b = min (b, f (0, i));
		printf ("Case #%d: %d\n", t, b);
	}
	return 0;
}
