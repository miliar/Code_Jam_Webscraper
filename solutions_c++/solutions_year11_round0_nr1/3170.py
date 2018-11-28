// thiago kronig <thiagokronig@gmail.com>

#include <cstdio>
#include <cmath>

using namespace std;

int main() {
	
	int t, n;
	char r;
	int p;
	
	scanf("%d", &t);
	for (int tt=1; tt<=t; tt++) {
	
		int o = 1;
		int b = 1;
		int y = 0;
		int yb = 0;
		int yo = 0;
		int delta;
		
		scanf("%d", &n);
		for (int i=1; i<=n; i++) {
			scanf(" %c %d", &r, &p);
			if (r == 'B') {
				delta = abs(p - b);
				yb = delta + yb;
				y = yb = y > yb ? y + 1 : yb + 1;
				b = p;
			} else {
				delta = abs(p - o);
				yo = delta + yo;
				y = yo = y > yo ? y + 1 : yo + 1;
				o = p;
			}
		}

		printf("Case #%d: %d\n", tt, y);
	}
	
	return 0;
}