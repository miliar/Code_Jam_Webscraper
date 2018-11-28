#include <stdio.h>
#include <string.h>
#include <algorithm>

typedef __int64 ll;
using namespace std;
const int MAXN = 1009;

int a[MAXN];
char s[MAXN];
bool vst[MAXN];
bool numUsed[MAXN];

int main() {
	freopen("F:\\A-large.in", "r", stdin);
	freopen("F:\\A-large.out", "w", stdout);
	int T;
	int cas = 0;
	int i, j, k, len;
	scanf("%d", &T);
	while (T--) {
		scanf("%s", s);
		memset(vst, 0, sizeof(vst));
		memset(numUsed, 0, sizeof(numUsed));
		len = strlen(s);
		for (i = 0; i < len; ++i) {
			if (!vst[s[i]]) {
				vst[s[i]] = true;
				if (i == 0) {
					a[i] = 1;
					numUsed[1] = true;
				} else {
					for (j = 0; numUsed[j]; ++j);
					a[i] = j;
					numUsed[j] = true;
				}
				for (j = i + 1; j < len; ++j) {
				//	vst[j] = true;
					if (s[j] == s[i]) a[j] = a[i];
				}
			}
		}
		int R;
		for (R = 0; numUsed[R]; ++R);
		if (R <= 1) R = 2;
		
		ll ans = 0;
		for (i = 0; i < len; ++i)
			ans = ans * R + a[i];
		printf("Case #%d: %I64d\n", ++cas, ans);
	}
	return 0;
}

