#include <iostream>
#include <cstdio>
#include <cstring>
#include <set>

using namespace std;

set<int> himpIn[1005];
set<int> himpOut[1005];
set<int> borosIn[1005];
set<int> borosOut[1005];
int ways[1005];
bool mark[1005];

int main()
{
	freopen("inputa.txt", "r", stdin);
	freopen("outputa.txt", "w", stdout);
	int tc, nc;
	int i, j, n, x;
	int outDeg;
	int loops;
	bool res;
	set<int>::iterator it;
	scanf("%d", &tc);
	for (nc = 1; nc <= tc; nc++) {
		scanf("%d", &n);
		for (i = 0; i < n; i++) {
			himpIn[i].clear();
			himpOut[i].clear();
		}
		for (i = 0; i < n; i++) {
			scanf("%d", &outDeg);
			for (j = 0; j < outDeg; j++) {
				scanf("%d", &x);
				x--;
				himpOut[i].insert(x);
				himpIn[x].insert(i);
			}
		}
		for (i = 0; i < n; i++) {
			borosIn[i] = himpIn[i];
			borosOut[i] = himpOut[i];
		}
		res = false;
		for (j = 0; j < n; j++) {
			for (i = 0; i < n; i++) {
				himpIn[i] = borosIn[i];
				himpOut[i] = borosOut[i];
			}
			loops = n;
			memset(ways, 0, sizeof(ways));
			memset(mark, false, sizeof(mark));
			ways[j] = 1;
			while (loops > 0) {
				for (i = 0; i < n; i++) {
					if (mark[i]) continue;
					if (himpOut[i].size() == 0) {
						for (it = himpIn[i].begin(); it != himpIn[i].end(); it++) {
							x = *it;
							ways[x] += ways[i];
							himpOut[x].erase(i);
						}
						himpIn[i].clear();
						mark[i] = true;
						loops--;
					}			
				}
			}
			for (i = 0; i < n; i++)
				res = res || (ways[i] > 1);
		}
		if (res) printf("Case #%d: %s\n", nc, "Yes");
		else printf("Case #%d: %s\n", nc, "No");
	}
}
