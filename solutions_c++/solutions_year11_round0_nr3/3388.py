#include <cstdio>

int t, n, a[1010], mn, x, xr, s;
int main (){
	scanf("%d", &t);
	for (int i = 1; i <= t; i++){
		scanf("%d", &n);
		xr = s = 0; mn = (1 << 30);
		for (int j = 0; j < n; j++){
			scanf("%d", &x);
			xr ^= x; s += x;
			if (mn > x)
				mn = x;
		}
		printf("Case #%d: ", i);
		if (xr != 0)printf("NO\n");
		else printf("%d\n", s - mn);
	}
	return 0;
}

