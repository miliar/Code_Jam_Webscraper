#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int maxn = 10000;

int casei, cases, n, D, open, closed;
int vine[maxn][2];
int used[maxn][maxn];
int Q[maxn * maxn][2];

int main() {
	//freopen("in.txt", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("Aout.txt", "w", stdout);
	
	memset(used, 0, sizeof used);
	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) scanf("%d%d", &(vine[i][0]), &(vine[i][1]));
		scanf("%d", &D);
		
		if (n == 1) {
			if ((vine[0][0] << 1) >= D) printf("Case #%d: YES\n", casei);
			else printf("Case #%d: NO\n", casei);
			continue;
		}
		if ((vine[0][0] << 1) >= D) {
			printf("Case #%d: YES\n", casei);
			continue;
		}
		
		int t = vine[0][0] << 1;
		closed = -1;
		open = -1;
		for (int i = 1; i < n; ++i) 
			if (vine[i][0] <= t) {
				++closed;
				Q[closed][0] = 0;
				Q[closed][1] = i;
				used[0][i] = casei;
			}
			else break;
		
		bool ok = false;
		int sec;
		while (open < closed) {
			++open;
			sec = Q[open][1];
			t = vine[sec][0] - vine[Q[open][0]][0];
			if (t > vine[sec][1]) t = vine[sec][1];
			t += vine[sec][0];
			if (t >= D) {
				ok = true;
				break;
			}
			for (int i = sec + 1; i < n; ++i) 
				if (vine[i][0] <= t && used[sec][i] != casei) {
					++closed;
					Q[closed][0] = sec;
					Q[closed][1] = i;
					used[sec][i] = casei;
				}
				else break;
		}
		
		if (ok) printf("Case #%d: YES\n", casei);
		else printf("Case #%d: NO\n", casei);
	}

	return 0;
}
