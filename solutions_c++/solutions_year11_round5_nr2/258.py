#include <stdio.h>

int cs, ct;
int n, ans;
int a[10], p[10];

void search(int l)
{
	int i, j, k;
	if (l == n) {
		j = 1;
		k = 100;
		for (i = 0; i < n; i++)
		if (a[p[i]] + 1 == a[p[i + 1]]) j++;
		else {
			if (j < k) k = j;
			j = 1;
		}
		if (k > ans) ans = k;
		return;
	}
	for (i = l; i < n; i++) {
		j = p[l]; p[l] = p[i]; p[i] = j;
		search(l + 1);
		j = p[l]; p[l] = p[i]; p[i] = j;
	}
}

int main()
{
	int i;
	scanf("%d", &ct);
	for (cs = 1; cs <= ct; cs++) {
		scanf("%d", &n);
		for (i = 0; i < n; i++) {
			scanf("%d", &a[i]);
			p[i] = i;
		}
		a[n] = 0;
		ans = 0;
		if (n) search(0);
		printf("Case #%d: %d\n", cs, ans);
	}	
	return 0;
}
