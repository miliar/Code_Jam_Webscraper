#include <stdio.h>

#define MAX 1024

int n, s[MAX], sum;

void action() {
	sum = 0;
	scanf("%d", &n);
	for(int i = 0; i < n; i++) {
		scanf("%d", &s[i]);
		sum += s[i];
	}

	for(int i = 0; i < n; i++) {
		double lb, ub, mid;
		lb = 0;
		ub = 100;
		while(true) {
			mid = (lb + ub) / 2;
			double si = (mid / 100 * sum) + s[i];
			double y = 100 - mid;
			for(int j = 0; j < n; j++) {
				if(i == j)continue;
				if(si < s[j])continue;
				y -= (si - s[j]) * 100 / sum;
			}
			if(y < 0) {
				if(ub == mid)break;
				ub = mid;
			} else if(y > 0) {
				if(lb == mid)break;
				lb = mid;
			} else break;
		}
		printf(" %.6lf", mid);
	}
}

int main() {
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) {
		printf("Case #%d:", i);
		action();
		printf("\n");
	}
return 0;
}
