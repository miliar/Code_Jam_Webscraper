#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;
int best[102][102];
int tocke[102];
int n, c, l;

int main() {
	scanf("%d\n", &c);
	for (int cases = 0; cases < c; cases++) {
		scanf("%d %d", &l, &n);
		for (int i = 1; i < n+1; i++)
			scanf("%d", &tocke[i]);
		tocke[0] = 0; tocke[n+1] = l+1;
		for (int i = 1; i <= n+1; i++) {
			for (int j = i-1; j >= 0; j--) {
				best[i][j] = 1000000000;
				if (j == i-1) {best[i][j] = 0; continue;}
				for (int k = i-1; k > j; k--) {
					if (best[i][j] > tocke[i]-tocke[j]-2+best[i][k]+best[k][j])
						best[i][j] = tocke[i]-tocke[j]-2+best[i][k]+best[k][j];
				}
			}
		}
		printf("Case #%d: %d\n", cases+1, best[n+1][0]);
	}
	return 0;
}