# include <cstdio>

int main () {
	int t = 0, n, k, T, ans;
	scanf("%d", &T); 
	while (T--) {
		printf ("Case #%d: ", ++t);
		scanf("%d%d", &n, &k);
		ans = 0;
		while (k & 1) {
			ans++;
			k = k >> 1;
		}
		if (ans >= n) printf ("ON\n");
		else printf ("OFF\n");
	}
	return 0;
}
