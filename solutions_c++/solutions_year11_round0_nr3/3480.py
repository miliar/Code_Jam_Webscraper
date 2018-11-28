#include <stdio.h>
#include <memory.h>
#include <algorithm>
#define MN 101
using namespace std;
int n;
pair<int,char> d[MN];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t, T, r, i, j, k, p, q, f, s, m, M;
	char str[4];

	scanf("%d",&T);
	for (t = 1; t <= T; t++) {
		printf("Case #%d: ",t);
		scanf("%d",&n);
		s = 0; m = -1; k = 0;
		for (i = 0; i < n; i++) {
			scanf("%d",&j);
			k ^= j; s += j;
			if (m == -1 || m > j) m = j;
		}
		if (k == 0) {
			printf("%d\n",s-m);
		}
		else printf("NO\n");
	}
	return 0;
}