#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <algorithm>

#define inf 0x3f3f3f3f

#define maxs (1 << 7)
#define maxq (1 << 10)

int ans[maxs][maxq];

std::string eng[maxs];
std::string que[maxq];

char buf[1 << 16];

bool eq[maxs][maxq];

inline void relax(int& a, int b) {
	if(a > b) a = b;
}

int main() {
	int t, tc, i, j, k, s, q;
	for((t = 1), scanf("%d", &tc); t <= tc; t++) {
		scanf("%d", &s); gets(buf);
		for(i = 0; i < s; i++) {
			gets(buf);
			eng[i] = buf;
		}
		scanf("%d", &q); gets(buf);
		for(i = 0; i < q; i++) {
			gets(buf);
			que[i] = buf;
		}
		for(i = 0; i < s; i++)
			for(j = 0; j < q; j++)
				eq[i][j] = (eng[i] == que[j]);
		memset(ans, 0x3f, sizeof(ans));
		for(i = 0; i < s; i++) ans[i][0] = 0;
		for(j = 0; j < q; j++)
			for(i = 0; i < s; i++)
				for(k = 0; k < s; k++)
					if(!eq[k][j])
						relax(ans[k][j+1], ans[i][j] + (i != k));
		int bans = inf;
		for(i = 0; i < s; i++)
			relax(bans, ans[i][q]);
		printf("Case #%d: %d\n", t, bans);
	}
	return 0;
}
