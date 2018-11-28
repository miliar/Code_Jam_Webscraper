#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>
using namespace std;

typedef long long llong;

const llong INF = 1LL<<60;
const int N = 128;

int mp[N][N], mp2[N][N];

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 0; t < T; t++) {
		memset(mp, 0, sizeof(mp));
		int n; scanf("%d", &n);
		int w = 0, h = 0;
		for(int i = 0; i < n; i++) {
			int x1, y1, x2, y2;
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			for(int a = x1; a <= x2; a++) for(int b = y1; b <= y2; b++) mp[a][b] = 1;
			w = max(w, x2); h = max(h, y2);
		}
		llong res = 0;
		for(; true; res++) {
			int cc = 0;
			for(int i = 0; i <= w; i++) for(int j = 0; j <= h; j++) {
				int cnt = 0;
				if(i != 0 && mp[i-1][j] == 1) cnt++;
				if(j != 0 && mp[i][j-1] == 1) cnt++;
				// printf("%d %d %d\n", i, j, cnt);
				if(mp[i][j] == 0 && cnt == 2) mp2[i][j] = 1;
				else if(mp[i][j] == 1 && cnt == 0) mp2[i][j] = 0;
				else mp2[i][j] = mp[i][j];
				
				if(mp2[i][j] == 1) cc++;
			}
			if(cc == 0) break;
			for(int i = 0; i <= w; i++) for(int j = 0; j <= h; j++) mp[i][j] = mp2[i][j];
		}
		printf("Case #%d: %lld\n", t+1, res+1);
	}
	return 0;
}

