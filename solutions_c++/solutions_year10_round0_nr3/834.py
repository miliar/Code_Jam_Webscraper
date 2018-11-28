#include <stdio.h>
#include <string.h>

typedef long long ll;

const int MAXN = 1024;

ll lastNum[MAXN];
int moveNo[MAXN];
int R, k, N;
ll g[MAXN], summe = 0;

ll solve()
{
	ll ans = 0;
	int m = 0;
	memset(lastNum, 0xff, sizeof(lastNum));
	memset(moveNo, 0xff, sizeof(moveNo));
	if (summe <= k) return (ll)R * summe;
	int f = 0;
	while (lastNum[f] == -1) {
		lastNum[f] = ans;
		moveNo[f] = m;
		int i = 0;
		ll s = 0;
		while (s <= k) {
			s += g[(f + i) % N];
			i++;
		}
		i--;
		s -= g[(f + i) % N];
		ans += s;
		m++;
		f = (f + i) % N;
		if (m == R) break;
	}
	if (m < R) {
//		printf("Cycle detected, f = %d, [%lld, %lld], [%d, %d]\n", f, ans, lastNum[f], m, moveNo[f]);
		ll diff = ans - lastNum[f];
		int md = m - moveNo[f];
		int toDo = (R - m) / md;
		ans += diff * (ll) toDo;
		m += md * toDo;
	}
	while (m < R) {
		int i = 0;
		ll s = 0;
		while (s <= k) {
			s += g[(f + i) % N];
			i++;
		}
		i--;
		s -= g[(f + i) % N];
		ans += s;
		m++;		
		f = (f + i) % N;
	}
	return ans;
}

int main(void)
{
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		summe = 0;
		scanf("%d%d%d", &R, &k, &N);
		for (int i = 0; i < N; i++) {
			int xx;
			scanf("%d", &xx);
			g[i] = xx;
			summe += g[i];
		}
		printf("Case #%d: %lld\n", tc, solve());
	}
	return 0;
}
