#include <cstdio>
#include <algorithm>
using namespace std;

#define For(i,n) for (int i = 0; i < n; ++i)
#define FOr(i,a,b) for (int i = a; i < b; ++i)

int T, n, d[40], ans;
char s[256];

int main() {
	scanf("%d", &T);
	For(r,T) {
		printf("Case #%d: ", r + 1);
		scanf("%d", &n);
		For(i,n) {
			scanf("%s", s);
			d[i] = 0; For(j,n) if (s[j] == '1') d[i] = j;
		}
		ans = 0;
		For(i,n) {
			FOr(j,i,n) if (d[j] <= i) {
				ans += j - i;
				for (int k = j; i < k; --k) d[k] = d[k - 1];
				break;
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}
