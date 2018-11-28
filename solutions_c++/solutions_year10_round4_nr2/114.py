#include <iostream>
#include <string>
#include <vector>

using namespace std;


const long long INF = 1000000000ll * 1000000000ll;

int n, ans;
vector<int> m;
int price[12][1<<11];
long long d[12][1<<11][12];

long long get_d (int level, int cnt, int l, int r) {
	if (level == -1)
		return cnt <= m[l] ? 0 : INF;

	int match = l >> (level+1);

	long long & my = d[level][match][cnt];
	if (my != -1)  return my;

	int m = (l + r) >> 1;
	my = get_d (level-1, cnt+1, l, m) + get_d (level-1, cnt+1, m+1, r);
	my = min (my, get_d (level-1, cnt, l, m) + get_d (level-1, cnt, m+1, r) + price[level][match]);

	my = min (my, INF);

	return my;
}

int main() {
	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);

	int ts;
	cin >> ts;
	for (int tt=1; tt<=ts; ++tt) {

		cin >> n;
		m.resize (1<<n);
		for (int i=0; i<(1<<n); ++i)
			scanf ("%d", &m[i]);
		for (int i=0; i<n; ++i)
			for (int j=0; j<(1<<(n-i-1)); ++j)
				scanf ("%d", &price[i][j]);

		memset (d, -1, sizeof d);
		long long ans = get_d (n-1, 0, 0, (1<<n)-1);

		printf ("Case #%d: %I64d\n", tt, ans);
	}


}

