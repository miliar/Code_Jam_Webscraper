#include <stdio.h>

double sum;

int main(){
	int t, CASE, data, i, n;
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	scanf("%d", &CASE);
	for(t = 1; t <= CASE; t ++){
		scanf("%d", &n);
		sum = 0;
		for(i = 1; i <= n; i ++){
			scanf("%d", &data);
			if(data != i) sum = sum + 1;
		}
		printf("Case #%d: %.6lf\n", t, sum);
	}
	return 0;
}