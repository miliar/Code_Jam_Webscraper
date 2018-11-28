#include <string.h>
#include <stdio.h>
using namespace std;

int order[2000];
int marca[2000];
int n;
int temp[2000];
int count() {
	memset(marca, 0, sizeof(marca));
	for (int i = 0; i < n; i++) if (marca[i] == 0) {
		int count = 1;
		int j = i;
		while (order[j] != i) {
			marca[j] = 1;
			j = order[j];
			count++;
		}
		marca[j] = 1;
		temp[count]++;
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for (int _ = 0; _ < T; _++) {
		memset(temp, 0, sizeof(temp));
		printf("Case #%d: ", _+1);
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", &order[i]);
			order[i]--;
		}
		count();
		double ans = 0;
		for (int i = 2; i <= n; i++)
			ans += temp[i]*i;
		printf("%.6lf\n", ans);
	}
	return 0;
}
