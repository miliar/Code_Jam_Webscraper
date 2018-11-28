#include <cstdio>



using namespace std;
int T, i, n, k;
inline bool rez (int n, int k) {
	//int x, y;
	//x = (1 << n) - 1; y = k / x;
	//printf ("%d %d\n", x, y);
	if ((k & ( (1<<n) - 1))== ((1<<n)-1)) return 0;
	return 1;
}
int main () {
	freopen ("snap.in", "r", stdin);
	freopen ("snap.out", "w", stdout);
	scanf ("%d\n", &T);
	for (i = 1; i <= T; i++) {
		scanf ("%d %d\n", &n, &k);
		if (!rez (n, k)) printf ("Case #%d: ON\n", i);
		else printf ("Case #%d: OFF\n", i);
	}
	return 0;
}
