#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cctype>
#include <cstdlib>

using namespace std;

int T,N;
int waarden[1000];
int verdeel[1000];
int xr[2];

int check(int num) {
	int sum = 0;
	xr[0] = 0;
	xr[1] = 0;
	for (int i = 0; i < N; i++) {
		verdeel[i] = 0;
		if ((num & (1 << i)) != 0)
			verdeel[i] = 1;
		sum += verdeel[i] * waarden[i];
		xr[verdeel[i]] ^= waarden[i];
	}
	if (xr[0] == xr[1])
		return sum;
	return -1;
}

int main() {
	scanf("%d",&T);
	for (int i = 0; i < T; i++) {
		scanf("%d", &N);
		int macht = 1;
		for (int j = 0; j < N; j++) {
			int tmp;
			scanf("%d", &tmp);
			waarden[j] = tmp;
			macht *= 2;
		}
		int m = -1;
		for (int j = 1; j < macht - 1; j++) {
			int tmp = check(j);
			if (tmp != -1 && tmp > m)
				m = tmp;
		}
		printf("Case #%d: ", i + 1);
		if (m < 0)
			printf("NO\n");
		else
			printf("%d\n", m);
	}
	return 0;
}
