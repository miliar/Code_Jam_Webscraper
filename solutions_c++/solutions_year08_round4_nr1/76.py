#include <cstdio>
#include <cstring>
#include <cassert>
#include <iostream>
#include <string>
#include <algorithm>

#define maxm (1 << 16)
#define inf 0x3f3f3f3f

int type[maxm], ch[maxm], val[maxm][2];

inline int calc(int t, int a, int b) {
	if(t == 1) return a && b;
	else return a || b;
}
inline void relax(int& a, int b) {
	if(a > b) a = b;
}

int main() {
	int t, tc, i, j, k, m, v;
	scanf("%d", &tc);
	for(t = 1; t <= tc; t++) {
		scanf("%d%d", &m, &v);
		for(i = 1; i <= (m-1)/2; i++) {
			scanf("%d%d", type+i, ch+i);
			val[i][0] = val[i][1] = inf;
		}
		for(; i <= m; i++) {
			scanf("%d", &j);
			type[i] = -1;
			ch[i] = 0;
			val[i][0] = val[i][1] = inf;
			val[i][j] = 0;
		}
		for(i = (m-1)/2; i >= 1; i--) {
			int l = i*2, r = i*2+1;
			assert(r <= m);
			for(int a = 0; a < 2; a++)
				for(int b = 0; b < 2; b++)
					if(val[l][a]<inf && val[r][b]<inf) {
						relax(val[i][calc(type[i], a, b)], val[l][a] + val[r][b]);
						if(ch[i]) relax(val[i][calc(1-type[i], a, b)], val[l][a] + val[r][b] + 1);
					}
		}
		printf("Case #%d: ", t);
		if(val[1][v] < inf) printf("%d\n", val[1][v]);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
