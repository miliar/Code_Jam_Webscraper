#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;

int main() {
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	int i, j, n, icas, cas, ans, x;
	scanf("%d", &cas);
	for (icas = 1; icas <= cas; ++icas) {
		scanf("%d", &n);
		ans = 0;
		for (i = 1; i <= n; ++i) {
			scanf("%d", &x);
			if (x != i)
			   ans++;
         }
		 printf("Case #%d: %d.000000\n", icas, ans);	
	}
}