#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int maxn = 10000 + 10;

int n, D;
int d[maxn], l[maxn], sw[maxn];

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int T;
	scanf("%d", &T);
	for (int cs = 1; cs <= T; ++cs) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%d%d", &d[i], &l[i]);
			l[i] = min(d[i], l[i]);
		}
		scanf("%d", &D);
		
		int mm, cur;
		for (int i = n - 1; i >= 0; --i) {
			mm = min(l[i] + 55, D - d[i]);
			for (int j = i + 1; j < n; ++j) {
				cur = d[j] - d[i];
				if (cur > l[i] || cur < sw[j] || sw[j] == -1) continue;
				mm = min(mm, cur);
				break;
			}
			if (mm > l[i]) sw[i] = -1; else sw[i] = mm;
		}
		
		printf("Case #%d: ", cs);
		if (sw[0] != -1) puts("YES"); else puts("NO");
	}
	
	return 0;
}
