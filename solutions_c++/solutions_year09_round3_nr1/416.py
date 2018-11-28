#include <cstdio>
#include <cstring>
char s[70];
long long chg[70];
bool vis[256];
int main ()
{
	char rest[10];
	int t, ca, i, j, len, k;
	long long m;
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &t);
	gets(rest);
	for (ca = 1; ca <= t; ++ ca) {
		gets(s);
		printf("Case #%d: ", ca);
		len = strlen(s);
		m = 0;
		memset(vis, 0, sizeof(vis));
		for (i = 0; i < len; ++ i)
			if (!vis[s[i]]) {
				m ++;
				vis[s[i]] = true;
			}
		if (m == 1)
			m ++;
		for (i = 0; i < len; ++ i)
			chg[i] = -1;
		chg[0] = 1;
		for (i = 1; i < len; ++ i)
			if (s[i] != s[i - 1])
				break;
			else
				chg[i] = 1;
		
		if (i < len)
			chg[i] = 0;
		
		k = 2;
		for (++ i; i < len; ++ i)
			if (chg[i] == -1) {
				for (j = 0; j < i; ++ j)
					if (s[i] == s[j])
						break;
				if (j < i)
					chg[i] = chg[j];
				else {
					chg[i] = k;
					k ++;
				}
			}
		
		long long ans = 0, l = 1;
		for (i = len - 1; i >= 0; -- i) {
			ans += chg[i] * l;
			l *= m;
		}
		printf("%I64d\n", ans);
	}
}
