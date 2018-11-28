#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
	int n, t;
	int s, m, p, q;

	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	
	scanf("%d", &t);
	for (int k = 1; k <= t; k++){
		scanf("%d", &n);
		m = 999999999; p = 0;s = 0;
		for (int i = 0; i < n; i++){
			scanf("%d", &q);
			p ^= q;
			s += q;
			m = min(m, q);
		}
		if (p) printf("Case #%d: NO\n", k);
		else printf("Case #%d: %d\n", k, s - m);
	}

	return 0;
}