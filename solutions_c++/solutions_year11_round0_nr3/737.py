#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;

const int INF = 0x3f3f3f3f;
int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int i, j, ret, ans, iCas, cas, n, x, sum;
	scanf("%d", &cas);
	for (iCas = 1; iCas <= cas; ++iCas) {
		scanf("%d", &n);
		ret = 0; sum = 0;
		ans = INF;
		for (i = 0; i < n; ++i) {
			scanf("%d", &x);
			sum += x;
			ans = min(ans, x);
			ret ^= x;
		}
		if (ret == 0) {
		   printf("Case #%d: %d\n", iCas, sum - ans);   		
		}
		else
			printf("Case #%d: NO\n", iCas); 
	}
	
		
}