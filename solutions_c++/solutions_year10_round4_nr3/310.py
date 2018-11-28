#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <list>
#include <set>
#include <map>
using namespace std;

#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define CLEAR(a,v) memset((a), (v), sizeof(a))

const double eps = 1e-9;
const int INF = 1000000000;
const long long LLINF = (long long)INF * INF;
const double PI = 2 * acos(.0);

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;

const int MAXN = 128;
int mp[2][MAXN][MAXN];

int main() {
	freopen("c-small.in","r",stdin);
	freopen("c-small.out","w",stdout);
	int T, ca = 0, R, from, to;
	scanf("%d",&T);
	while (T--) {
		scanf("%d",&R);
		CLEAR(mp, 0);
		from = 0; to = 1;
		int tx,ty,i,j;
		int minx, maxx, miny, maxy;
		minx = miny = INF;
		maxx = maxy = -INF;
		for (i = 0 ; i < R ; i++) {
			int x1, y1, x2, y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			minx <?= x1;
			maxx >?= x2;
			miny <?= y1;
			maxy >?= y2;
			for (tx = x1 ; tx <= x2 ; ++tx)
				for (ty = y1 ; ty <= y2 ; ++ty)
					mp[from][tx][ty] = 1;
		}
		int cnt = 0;
		while (1) {
			CLEAR(mp[to], 0);
			int flg = 0;
			for (i = minx ; i <= maxx ; i++) {
				for (j = miny ; j <= maxy ; j++) {
					//printf("%d",mp[from][i][j]);
					if (mp[from][i][j]) flg = 1;

					if (mp[from][i-1][j] == 0 && mp[from][i][j-1] == 0)
						mp[to][i][j] = 0;
					else if (mp[from][i-1][j] == 1 && mp[from][i][j-1] == 1)
						mp[to][i][j] = 1;
					else mp[to][i][j] = mp[from][i][j];
				}
				//printf("\n");
			}
			if (!flg) break;
			from = 1 - from;
			to = 1 - to;
			++cnt;

		}
		printf("Case #%d: %d\n",++ca,cnt);
	}
	return 0;
}
/*
1
3
5 1 5 1
2 2 4 2
2 3 2 4
*/
