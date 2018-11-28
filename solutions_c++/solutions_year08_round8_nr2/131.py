#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <cmath>
#include <map>

using namespace std;

#define REP(a, b) for(int a=0; a<(b); a++)
#define FOR(a, b, c) for(int a=(b); a<=(c); a++)
#define FORD(a, b, c) for(int a=(b); a>=(c); a--)
#define FOREACH(it, c) for(typeof(c.begin()) it = c.begin(); it != c.end(); it++)
#define ABS(a) ((a)<0 ? -(a) : (a))
#define MP make_pair
#define F first
#define S second

map<string, int> colors;

map<int, map<int, int> > all;
// pos -> (maski, wyniki)

#define INF 100000

int cnt[1<<10];

int get(int mask, int pos, int newPos) {
	//printf("%d %d %d\n", mask, pos, newPos);
	int ret = INF;
	FOREACH (iter, all) if (iter->first >= pos && iter->first < newPos) {
		FOREACH (iter2, iter->second) if ((mask|iter2->F)==mask) ret <?= iter2->second + 1;
	}
	if (all.find(newPos)==all.end())
		all[newPos] = map<int, int>();
	if (all[newPos].find(mask)==all[newPos].end())
		all[newPos][mask] = INF;
	all[newPos][mask] = (all[newPos][mask]<?ret);
	return all[newPos][mask];
}

pair<pair<int, int>, int> w[300];

char buf[100];

int main() {
	REP(i, 1<<10) {
		cnt[i] = 0;
		int tmp = i;
		while (tmp!=0) {
			cnt[i] += (tmp&1);
			tmp /= 2;
		}
	}
    int zz;
    scanf("%d", &zz);
    FOR(zzz, 1, zz) {
        colors.clear();
		all.clear();
		int n;
		scanf("%d\n", &n);
		int colorsn = 0;
		REP(i, n) {
			int a, b;
			scanf("%s %d %d\n", buf, &a, &b);
			string col = string(buf);
			if (colors.find(col)==colors.end()) colors[col] = colorsn++;
			w[i] = MP(MP(a, b), colors[col]);
		}
		sort(w, w+n);
		all[0][0] = 0;
		REP(i, n) REP(m, 1<<10) if (cnt[m]<=3 && (m&(1<<w[i].S))==(1<<w[i].S))
			get(m, w[i].F.F-1, w[i].F.S);
		int ret = INF;
		FOREACH(iter, all[10000]) ret <?= iter->S;
		if (ret==INF)
			printf("Case #%d: IMPOSSIBLE\n", zzz);
		else
			printf("Case #%d: %d\n", zzz, ret);
    }
	
    return 0;
}
