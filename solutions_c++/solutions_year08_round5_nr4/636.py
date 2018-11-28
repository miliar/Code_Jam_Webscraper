#include <cstdio>
#include <vector>
#include <set>
#include <utility>
using namespace std;
#define MAXN 101
#define p 10007

set<pair<int, int> > restr;
int tab[MAXN][MAXN];
int h, w, r;

int jump(int x, int y) {
	if (tab[y][x] != -1) return tab[y][x];
	tab[y][x] = 0;
	if (restr.find(make_pair(x, y))!=restr.end()) return 0;	
	if (y-1>=1 && x-2>=1)
		tab[y][x] = (tab[y][x] + jump(x-2, y-1))%p;
	if (x-1>=1 && y-2>=1)
		tab[y][x] = (tab[y][x] + jump(x-1, y-2))%p;
	return tab[y][x];
}

int main() {
	int N;
	scanf("%d", &N);
	for (int n=1; n<=N; n++) {
		memset(tab, -1, sizeof(tab));
		restr.clear();

		int res;
		scanf("%d%d%d", &h, &w, &r);
		while (r--) {
			int x, y;
			scanf("%d%d", &x, &y);
			restr.insert(make_pair(y, x));				
		}
		tab[1][1] = 1;		
		printf("Case #%d: %d\n", n, jump(w, h));
	}
	return 0;
}