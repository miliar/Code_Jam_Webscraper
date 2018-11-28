#include <stdio.h>


int main() {
	int ecase, ecount;
	int next[1010];
	int emany[1010];
	int get[1010];
	int i, j;
	scanf("%d",&ecase);
	for (ecount = 1; ecount <= ecase; ecount++) {
		int er,en,ek;
		scanf("%d%d%d",&er, &ek, &en);
		for (i = 0; i < en; i++)
			scanf("%d", &emany[i]);
		int t = 0;
		long long int total = 0;
		for (i = 0; i < en; i++) {
			if (i > 0)
				total -= emany[i-1];
			while (t < i + en && total + emany[t % en] <= ek) {
				total += emany[t % en];
				t++;
			}
			next[i] = t % en;
			get[i] = total;
		}
		long long int ans = 0;
		t = 0;
		for (i = 0; i < er; i++) {
			ans += get[t];
			t = next[t];
		}
		printf("Case #%d: %I64d\n", ecount, ans);
	}
	return 0;
}
