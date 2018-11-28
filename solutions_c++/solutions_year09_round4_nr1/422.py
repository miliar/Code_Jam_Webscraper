#include <stdio.h>
#include <algorithm>
#define MN 40
using namespace std;
int n, r;
int d[MN][MN], M[MN], ch[MN];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t, T;
	int i, j, k;

	scanf("%d",&T);
	for (t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		scanf("%d",&n);
		for (i = 0; i < n; i++) {
			M[i] = -1;
			for (j = 0; j < n; j++) {
				scanf("%1d",&d[i][j]);
				if (d[i][j]) M[i] = j;
			}
		}
		r = 0;
		for (i = 0; i < n; i++) {
			if (M[i] <= i) continue;
			for (j = i+1; j < n; j++) {
				if (M[j] <= i) {
					r += j-i;
					for (k = j; k > i; k--) swap(M[k],M[k-1]);
					break;
				}
			}
		}
		printf("%d\n", r);
	}
	return 0;
}