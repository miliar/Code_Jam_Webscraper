#include <iostream>
#include <map>

using namespace std;

int dist, slow, fast, lmt, n;
map<int, int> len;

void init()
{
	scanf("%d%d%d%d%d", &dist, &slow, &fast, &lmt, &n);
	len.clear();
	int sum = 0;
	for (int i = 0; i < n; i++) {
		int x, y, z;
		scanf("%d%d%d", &x, &y, &z);
		len[z] += y - x;
		sum += y - x;
	}
	len[0] = dist - sum;
}

void work()
{
	double ans = 0;
	double rest = lmt;
	for (map<int, int>::iterator it = len.begin(); it != len.end(); it++) {
		double need = (double)it->second / ((double)fast + (double)it->first);
		if (need <= rest) {
			rest -= need;
			ans += need;
		} else {
			double dd = (double)it->second - rest * ((double)fast + (double)it->first);
			ans += rest;
			ans += dd / ((double)it->first + (double)slow);
			rest = 0;
		}
	}
	printf("%.10lf\n", ans);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int tt = 1; tt <= test; tt++) {
		printf("Case #%d: ", tt);
		init();
		work();
	}
}