#include <cstdio>
#include <cstring>
#include <cassert>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>

#define Eo(x) { std::cerr << #x << " = " << x << std::endl; }
#define modulo 10007LL
#define maxn 110

typedef long long int64;

typedef double real;

int64 ans[maxn][maxn];


int main() {
	int ferlon;
	scanf("%d", &ferlon);
	for (int _ = 0; _ < ferlon; ++_){
		int h, w, r;
		scanf("%d%d%d", &h, &w, &r);
		memset(ans, 0, sizeof(ans));
		int i, j;
		for (i = 0; i < r; i++){
		 	int x, y;
		 	scanf("%d%d", &x, &y);
		 	--x;
		 	--y;
		 	ans[x][y] = -1;
		}
		ans[0][0] = 1;
		for (i = 0; i < h; i++)
			for (j = 0; j < w; j++) if (ans[i][j] > 0){
//				if (ans[i + 1][j + 1] != -1) ans[i + 1][j + 1] = (ans[i + 1][j + 1] + ans[i][j]) % modulo;
				if (ans[i + 1][j + 2] != -1) ans[i + 1][j + 2] = (ans[i + 1][j + 2] + ans[i][j]) % modulo;
				if (ans[i + 2][j + 1] != -1) ans[i + 2][j + 1] = (ans[i + 2][j + 1] + ans[i][j]) % modulo;
			}
		printf("Case #%d: %I64d\n", _ + 1, ans[h - 1][w - 1]);
	}
	return 0;
}
