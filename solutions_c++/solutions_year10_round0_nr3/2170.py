#include <cstdio>
#include <algorithm>
using namespace std;
const int nMax = 1004;
int w[nMax];
int t[nMax], r, k, n, ans[nMax], next[nMax];
void compute(int l) {
	t[0] = w[l];
	for(int i = 1; i < n; i++) {
		t[i] = t[i-1] + w[(l+i) % n];
	}
}
int main() {
	int c; scanf("%d", &c);
	for(int ii = 1; ii <= c; ii++) {
		scanf("%d %d %d", &r, &k , &n);

		for(int i = 0; i < n; i++) scanf("%d",w+i);
		int ile = 0, d = 0;
		while (r-->0) {
			if (ans[d] == 0) {
				compute(d); 
				int* id = upper_bound(t, t+n, k);
				next[d] = (id-t) % n;
				ans[d] = *(--id);
			}
			ile += ans[d];
			d = (d+next[d]) %n;
		//	printf("d-> %d, ile-> %d\n", d, ile);
		}
		printf("Case #%d: %d\n", ii, ile);
		for(int i = 0; i < n ; i++) ans[i] = 0;
	}
}
