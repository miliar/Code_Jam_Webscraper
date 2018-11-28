#include<stdio.h>
#include<string.h>

const int mod = 10000;

char str[1000];
char T[] = "welcome to code jam";
int f[505][30];

int dp(char *s) {
	int len = strlen(s);
	int lenT = strlen(T);
	memset(f, 0, sizeof(f));
	for (int i = 0; i < len; i++) {
		if (s[i] == T[0]) {
			f[i][0] = 1;
		}
	}
	for (int i = 1; i < len; i++) {
		for (int j = 1; j < lenT; j++) {
			if (s[i] == T[j]) {
				for (int k = 0; k < i; k++) {
					f[i][j] = (f[i][j] + f[k][j - 1]) % mod;
				}
			}
		}
	}
	int ans = 0;
	for (int i = 0; i < len; i++) {
		ans = (ans + f[i][lenT - 1]) % mod;
	}
	return ans;
}

int main() {
	int n;
	scanf("%d", &n);
	gets(str);
	for (int t = 1; t <= n; t++) {
		gets(str);
		int ans = dp(str);
		printf("Case #%d: %04d\n", t, ans);
	}
	return 0;
}
