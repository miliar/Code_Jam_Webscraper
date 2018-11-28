#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

const int N = 128;
const int INF = 1<<20;

int mp[N][N], n;
bool vst[N][N];

int minAdd(int x, int y)
{
	int m = 2*n-1, s1 = m;
	for(int i = 0; i < m; i++) for(int j = 0; j < m; j++) if(vst[i][j]) {
		int ix = 2*x-i, iy = 2*y-j;
		// if(x == 2 && y == 3) printf("%d %d %d %d %d %d %d\n", i, j, ix, iy, mp[i][j], mp[i][iy], mp[ix][j]);
		if(ix >= 0 && ix < m && (vst[ix][j] && mp[ix][j] != mp[i][j])) return INF;
		if(iy >= 0 && iy < m && (vst[i][iy] && mp[i][iy] != mp[i][j])) return INF;
		int dis = abs(ix-x)+abs(iy-y);
		s1 = max(s1, 2*dis+1);
	}
	int sz = (s1+1)/2;
	return sz*sz-n*n;
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 0; t < T; t++) {
		scanf("%d", &n);
		memset(vst, false, sizeof(vst));
		for(int i = 0; i < 2*n-1; i++) {
			int m = (i <= n-1) ? (i+1) : (2*n-1-i);
			int b = n-1-min(i, 2*n-2-i);
			// printf("%d %d %d\n", i, m, b);
			for(int j = 0; j < m; j++, b += 2) {
				scanf("%d", &mp[i][b]);
				vst[i][b] = true;
			}
		}
		int res = INF;
		for(int i = 0; i < 2*n-1; i++) for(int j = 0; j < 2*n-1; j++) {
			int add = minAdd(i, j);
			// printf(".......... %d %d %d\n", i, j, add);
			res = min(res, add);
		}
		printf("Case #%d: %d\n", t+1, res);
	}
	return 0;
}

