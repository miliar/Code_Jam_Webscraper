#include <stdio.h>

int main() {
	int t;
	scanf("%d", &t);
	for (int z = 1; z <= t; z++) {
		long long ans = 0;
		int f[200] = {0};
		int u[200], c = 0, base = 0;
		for (int i = 0; i < 200; i++) u[i] = -1;

		char s[100];
		scanf("%s", s);
		for (int i = 0; s[i] != 0; i++) {
			if (f[s[i]] == 0) base++;
			f[s[i]] = 1;
		}
		if (base < 2) base = 2;
		u[s[0]] = 1;
		
		for (int i = 0; s[i] != 0; i++) {
			if (u[s[i]] == -1) {
				u[s[i]] = c++;
				if (c == 1) c = 2;
			}
			ans = (ans*base) + u[s[i]];
		}

		printf("Case #%d: %I64d\n", z, ans);
	}
	return 0;
}
