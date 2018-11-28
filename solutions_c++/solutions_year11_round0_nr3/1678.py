/*
	Author: TangQiao @ Netease Youdao.
	2011.5.7
*/
#include <stdio.h>
#include <string>
#include <vector>
#include <math.h>
using namespace std;

int ans;

void deal() {
	int n, tot, m, a, tmp;
	scanf("%d", &n);
	tot = tmp = 0;
	m = 200000000;
	for (int i = 0; i < n; ++i) {
		scanf("%d", &a);
		tot += a;
		m = m < a ? m : a;
		tmp ^= a;
	}
	if (tmp == 0) {
		ans = tot - m;
	} else {
		ans = -1;
	}
}

int main() {
    int N;
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
    scanf("%d", &N);
    for (int i = 0; i < N; ++i) {
        deal();
        printf("Case #%d: ", i+1);
		if (ans == -1) 
			printf("NO\n");
		else 
			printf("%d\n", ans);
    }
    return 0;
}
