#include <cstdio>
#include <cstring>
using namespace std;

#define min(a, b) (a > b ? b : a)
#define max(a, b) (a > b ? a : b)
int x[60010], y[60010], f[60010];
int T, n, len;

int main(){
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	for (int ca = 1; ca <= T; ++ca){
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%d%d", &x[i], &y[i]);
		scanf("%d", &len);
		f[0] = x[0] + min(x[0], y[0]);
		for (int i = 1; i < n; ++i)
			for (int j = 0; j < i; ++j)
				if (f[j] >= x[i])
					f[i] = max(f[i], x[i] + min(y[i], x[i] - x[j]));
		bool flag = false;
		for (int i = 0; i < n; ++i)
			if (f[i] >= len){
				flag = true;
				break;
			}
		printf("Case #%d: %s\n", ca, (flag ? "YES" : "NO"));
		memset(f, 0, sizeof(f));
	}
	return 0;
}

