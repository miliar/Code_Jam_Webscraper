#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int t, r, k, n, g[2000], next[2000], vislev[2000], racekol[2000];
long long dopaid[2000];
bool visited[2000];

int main() {
	freopen("c-large.in", "r", stdin);
	freopen("c-large.out", "w", stdout);	
	scanf("%d", &t);
	int i, j, l, p, q, R;
	long long res, cur;
	for (l = 1; l <= t; ++l) {
		res = 0;
		scanf("%d%d%d", &r, &k, &n);
		for (i = 0; i < n; ++i)
			scanf("%d", &g[i]);
		for (i = 0; i < n; ++i) {
			visited[i] = false;
			j = (i + 1) % n;
			racekol[i] = g[i];
			while (j != i) {
				if (racekol[i] + g[j] > k) break;
				racekol[i] += g[j];
				j = (j + 1) % n;
			}
			next[i] = j;
		}
		cur = 0; i = 0;
		R = 0;
		for (p = 1; p <= r; ++p) {
			cur += racekol[i];
			if (visited[i]) {
				R = r;
				R -= vislev[i];
				res = dopaid[i];
				int len = p - vislev[i];
				int kol = R / len;
				res += (cur - dopaid[i]) * (long long)kol;
				R -= kol * len;
				cur = res;
				i = next[i];
				break;		
			}
			vislev[i] = p;
			dopaid[i] = cur;
			visited[i] = true;
			i = next[i];										
		}
		while (R--) {
			cur += racekol[i];
			i = next[i];
		}
		printf("Case #%d: ", l);
		cout << cur << endl;
	}
	return 0;
}
