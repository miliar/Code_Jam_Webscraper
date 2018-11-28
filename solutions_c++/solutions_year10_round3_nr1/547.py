#include <cstdio>
#include <vector>
#include <utility>
using namespace std;
typedef pair<int, int> pii;
#define X first
#define Y second

int t, it, a, b, n, i, j, c;
vector<pair<int, int> > maj;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &t);
	for(it = 1; it <= t; ++it) {
		c = 0;
		scanf("%d", &n);
		maj.resize(n);
		while(--n >= 0) {
			scanf("%d%d", &a, &b);
			maj[n].X = a;
			maj[n].Y = b;
		}
		for(i = 1; i < maj.size(); ++i) {
			for(j = 0; j < i; ++j) {
				if((maj[i].X - maj[j].X) * (maj[i].Y - maj[j].Y) < 0) {
					++c;
				}
			}
		}
		printf("Case #%d: %d\n", it, c);
	}
	return 0; }