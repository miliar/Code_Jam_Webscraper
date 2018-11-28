#include <cstdio>
#include <cstring>
#include <cassert>
#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

#define Eo(x) { std::cerr << #x << " = " << x << std::endl; }

typedef long long int64;

#define inf 0x3f3f3f3f


#define maxs (1 << 7)
#define maxn (maxs*maxs)

char fld[maxs][maxs];
int n, m;
int ans[maxs][1 << 11];


inline void relax(int& a, int b) {
	if(a < b) a = b;
}
inline int bit_cnt(int x) {
	int ans = 0;
	for(; x; x >>= 1) ans += (x&1);
	return ans;
}

bool poss(int mask, int l) {
	for(int j = 0; j < m; j++)
		if(mask & (1 << j)) {
			if(fld[l][j] == 'x') return false;
			if(j > 0 && fld[l][j-1] == '.' && (mask & (1 << (j-1)))) return false;
			if(j < m-1 && fld[l][j+1] == '.' && (mask & (1 << (j+1)))) return false;
		}
	return true;
}

bool allow(int mask1, int mask2) {
	for(int j = 0; j < m; j++)
		if(mask1 & (1 << j)) {
			if(j > 0 && (mask2 & (1 << (j-1)))) return false;
			if(j < m-1 && (mask2 & (1 << (j+1)))) return false;
		}
	return true;
}

int main() {
	int t, tc;
	scanf("%d", &tc);
	for(t = 1; t <= tc; t++) {
		int i, j, di, dj, k, kp;
		scanf("%d%d", &n, &m); n++;
		for(j = 0; j < m; j++) fld[0][j] = 'x';
		for(i = 1; i < n; i++)
			scanf(" %s", fld[i]);
		memset(ans, 0, sizeof(ans));
		for(i = 0; i < n; i++) {
			for(k = 0; k < (1 << m); k++) if(poss(k, i))
				for(kp = 0; kp < (1 << m); kp++) if(allow(k, kp))
					relax(ans[i+1][k], ans[i][kp] + bit_cnt(k));
		}
		int bans = 0;
		for(k = 0; k < (1 << m); k++)
			relax(bans, ans[n][k]);
		printf("Case #%d: %d\n", t, bans);
	}
	return 0;
}
