#include <stdio.h>
#include <map>
#include <string>
#include <memory.h>
using namespace std;
#define MX 7000013
#define INF 100000
map<string, int> mp;
int f[1100][110];
int best[1100];
char buf[1000000];

int main() {
	int rep;

	scanf("%d%*c", &rep);
	for (int ri = 0; ri < rep; ri ++) {
		mp.clear();

		int s, q;
		scanf("%d%*c", &s);
		for (int i = 0; i < s; i++) {
			mp[gets(buf)] = i;
		}
		scanf("%d%*c", &q);
		memset(f[0], 0, sizeof(f[0]));
		best[0] = 0;
		for (int i = 1; i <= q; i++) {
			best[i] = INF;
			int d;
			gets(buf);
			if (mp.find(buf) == mp.end()) d = -1;
			else d = mp[buf];
			for (int j = 0; j < s; j++) {
				if (j != d) f[i][j] = min(f[i - 1][j], best[i - 1] + 1);
				else f[i][j] = INF;

				if (f[i][j] < best[i]) best[i] = f[i][j];
			}
		}
		printf("Case #%d: %d\n", ri + 1, best[q]);
	}
}