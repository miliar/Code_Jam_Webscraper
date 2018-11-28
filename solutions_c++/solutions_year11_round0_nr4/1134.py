#include <stdio.h>
#include <cstring>
#include <algorithm>
using namespace std;

int f[200], a, t, n;

int main()
{
	memset(f, 0x3f, sizeof f);
	f[1] = 0;

	scanf("%d", &t);
	for(int q=1; q<=t; ++q) {
		scanf("%d", &n);
		int ans = 0;
		for(int i=1; i<=n; ++i) {
			scanf("%d", &a);
			if(a != i) ans++;
		}
		printf("Case #%d: %d.000000\n", q, ans);
	}

	return 0;
}

