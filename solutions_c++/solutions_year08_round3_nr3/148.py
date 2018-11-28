#include <stdio.h>
#define mod = 1000000007
int main()
{
	int nt, n, m, x, y, z;
	int genArr[500000], arr[500000], save[500000], ans;
	
	scanf("%d", &nt);
	for (int it = 1; it <= nt; it++) {
		scanf("%d %d %d %d %d", &n, &m, &x, &y, &z);
		for (int i = 0; i < m; i++) {
			scanf("%d", &genArr[i]);
		}
		for (int i = 0; i < n; i++) {
			arr[i] = genArr[i % m];
			genArr[i % m] = (int)((x * (long long) genArr[i % m] + (long long)y * (i + 1)) % z);
		}
		ans = 0;
		for (int i = 0; i < n; i++) {
			save[i] = 1;
			for (int j = 0; j < i; j++) {
				if (arr[i] > arr[j]) {
					save[i] = (save[i] + save[j]) % 1000000007;
				}
			}
			ans = (ans + save[i]) % 1000000007;
		}
		printf("Case #%d: %d\n", it, ans);
	}
	return 0;
}
