#include <iostream>

using namespace std;

typedef long long ll;

int total[1005];
int byk[1005];
int now[1005];
int idx[1005];
bool pake[1005];
int q[1005];

int main()
{
	freopen("c.in", "rt", stdin);
	freopen("c.out", "wt", stdout);
	int tc, nc, i, j, r, k, n, st, ak, loop;
	ll res, part;
	scanf("%d", &tc);
	for (nc = 1; nc <= tc; nc++) {
		scanf("%d%d%d", &r, &k, &n);
		for (i = 0; i < n; i++)
			scanf("%d", &byk[i]);
		memset(pake, false, sizeof(pake));
		for (i = 0; i < n; i++) {
			total[i] = 0;
			now[i] = i;
			for (j = 0; j < n; j++) {
				int px = (i+j)%n;
				if (total[i]+byk[px] <= k)
					total[i] += byk[px];
				else {
					now[i] = px;
					break;
				}
			}
		}
		for (ak = -1, st = 0; !pake[st]; st = now[st]) {
			pake[st] = true;
			q[++ak] = total[st];
			idx[st] = ak;
		}
		st = idx[st];
		res = 0LL;
		for (i = 0; (i < st && r > 0); i++, r--)
			res += ll(q[i]);
		if (r > 0) {
			part = 0LL;
			loop = ak-st+1;
			for (i = st; i <= ak; i++)
				part += ll(q[i]);
			res += part*(r/loop);
			r %= loop;
			for (i = st; (i <= ak && r > 0); i++, r--)
				res += ll(q[i]);
		}
		printf("Case #%d: %I64d\n", nc, res);
	}
}
