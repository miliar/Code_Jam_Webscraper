#include <stdio.h>
#include <cstring>
using namespace std;
char s[1100], sn[1100];
int k, seq[10], can[10], len, ans;
void work(int dep) {
	if (dep < k)
		for (int p = 0, i = can[0]; i > 0; p = i, i = can[i]) {
			can[p] = can[i]; seq[dep] = i;
			work(dep + 1);
			can[p] = i;
		}
	else {
		int i, j, x;
		for (i = 0, x = 0; i < len / k; ++i, x += k)
			for (j = 0; j < k; ++j)
				sn[x + j] = s[x + seq[j] - 1];
		x = 1; 
		for (i = 1; i < len; ++i)
			if (sn[i] != sn[i - 1])
				++x;
		if (x < ans)
			ans = x;
	}
}
int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int cas, tes, i;
	for (scanf("%d", &cas), tes = 1; tes <= cas; ++tes) {
		scanf("%d%s", &k, s);
		for (i = 0; i < k; ++i)
			can[i] = i + 1;
		can[k] = 0; len = strlen(s); ans = len + 1;
		work(0);
		printf("Case #%d: %d\n", tes, ans);
	}
}