#include <cstdio>
#include <algorithm>
using namespace std;

int pos[100], V[100];

int main() {
	int tcase;
	scanf("%d", &tcase);
	for(int ttt=1; ttt<=tcase; ttt++) {
		int B, T, n, k;
		scanf("%d%d%d%d", &n, &k, &B, &T);
		int yes = 0, no = 0;
		for(int i=0; i<n; i++) scanf("%d", &pos[i]);
		for(int i=0; i<n; i++) scanf("%d", &V[i]);
		int cnt = 0;
		for(int i=n-1; i>=0 && yes < k; i--) {
			if(pos[i] + T*V[i] >= B) {
				yes ++;
				cnt += no;
			} else {
				no++;
			}
		}
		printf("Case #%d: ", ttt);
		if(yes < k) {
			puts("IMPOSSIBLE");
		} else {
			printf("%d\n", cnt);
		}
	}
}
