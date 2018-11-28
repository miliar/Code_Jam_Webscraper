#include <iostream>
#include <cstdio>
#include <string.h>
#include <string>
using namespace std;

const int maxn = 20000 + 10;
int f[maxn], d[maxn], L[maxn], Dis;
int n;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("k2.out", "w", stdout);
	int TextN, TT = 0, tmp, x;
	scanf("%d", &TextN);
	while (TextN--) {
		scanf("%d", &n);
		for (int i = 1; i <= n; i++)
			scanf("%d%d", &d[i], &L[i]);
		scanf("%d", &Dis);
		if (d[1] < L[1]) L[1] = d[1];

		bool bj = false;
		memset(f, -1, sizeof(f));
		f[1] = 0;
		for (int i = 1; i <= n; i++) 
		if (f[i] >= 0) {
			tmp = d[i] - f[i] + d[i];
			if (tmp >= Dis) {
				bj = true;
				break;
			}
			for (int j = i+1; j <= n; j++) 
			if (tmp >= d[j]){
				x = max(d[i], d[j] - L[j]);
				if (f[j] == -1 || x < f[j]) f[j] = x;
			} else break;
		}
		if (bj) printf("Case #%d: YES\n", ++TT);
		else printf("Case #%d: NO\n", ++TT);
	}
	return 0;
}