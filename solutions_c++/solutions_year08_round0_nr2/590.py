#include <cstdio>
#include <algorithm>
using namespace std;

#define CLEAR(a, b) memset((a), (b), sizeof(a));
#define FOR(i, a, b) for(__typeof(a) i = (a); i < (b); i++)

const int N = 128;

int ab[N], ae[N], an;
int bb[N], be[N], bn;
int nexta[N], nextb[N];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	FOR(t, 1, T+1) {
		int K; scanf("%d", &K);
		scanf("%d %d", &an, &bn);
		FOR(i, 0, an) {
			int h1, m1, h2, m2; scanf("%d%*c%d %d%*c%d", &h1, &m1, &h2, &m2);
			ab[i] = h1*60+m1;
			ae[i] = h2*60+m2;
			//fprintf(stderr, "%d: %d %d\n", t, ab[i], ae[i]);
		}
		FOR(i, 0, bn) {
			int h1, m1, h2, m2; scanf("%d%*c%d %d%*c%d", &h1, &m1, &h2, &m2);
			bb[i] = h1*60+m1;
			be[i] = h2*60+m2;
			//fprintf(stderr, "%d: %d %d\n", t, bb[i], be[i]);
		}
		CLEAR(nexta, -1); CLEAR(nextb, -1);
		bool vsta[N] = { false }, vstb[N] = { false };
		FOR(i, 0, an) {
			FOR(j, 0, bn)
				if(bb[j] >= ae[i]+K && !vstb[j] && (nexta[i] == -1 || bb[nexta[i]] > bb[j])) nexta[i] = j;
			if(nexta[i] != -1) vstb[nexta[i]] = true;
		}
		FOR(i, 0, bn) {
			FOR(j, 0, an)
				if(ab[j] >= be[i]+K && !vsta[j] && (nextb[i] == -1 || ab[nextb[i]] > ab[j])) nextb[i] = j;
			if(nextb[i] != -1) vsta[nextb[i]] = true;
		}
		int da[N] = { 0 }, db[N] = { 0 };
		FOR(i, 0, an) if(nexta[i] != -1) db[nexta[i]]++;
		FOR(i, 0, bn) if(nextb[i] != -1) da[nextb[i]]++;
		int ax = 0, bx = 0;
		FOR(i, 0, an) if(da[i] == 0) ax++;
		FOR(i, 0, bn) if(db[i] == 0) bx++;
		printf("Case #%d: %d %d\n", t, ax, bx);
		
	}
	return 0;
}
