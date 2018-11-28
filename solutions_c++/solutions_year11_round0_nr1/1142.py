#include <stdio.h>
#include <cstring>
#include <algorithm>
using namespace std;

int main()
{
	char str[10];
	int t, n;
	scanf("%d", &t);
	for(int q=1; q<=t; ++q) {
		printf("Case #%d: ", q);
		scanf("%d", &n);
		int p1 = 1, p2 = 1, ans = 0, c1 = 0, c2 = 0, x, last = -1;
		for(int i=0; i<n; ++i) {
			scanf("%s%d", str, &x);
			
			if(str[0] == 'O') {
				int w = abs(x - p1);
				if(w < c1) w = 0; else w -= c1;
				w++;
				ans += w;
				p1 = x;
				c1 = 0; c2 += w;
			}
			else {
				int w = abs(x - p2);
				if(w < c2) w = 0; else w -= c2;
				w++;
				ans += w;
				p2 = x;
				c2 = 0; c1 += w;
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}

