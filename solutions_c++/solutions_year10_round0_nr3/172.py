#include <stdio.h>
#include <string.h>

long long int ult[1010];
long long int valult[1010];
long long int tam[1010];
int main() {
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		printf("Case #%d: ", t+1);
		long long int R, k, N;
		scanf("%lld %lld %lld", &R, &k, &N);
		memset(ult, -1, sizeof(ult));
		for (int i = 0; i < N; i++) scanf("%lld", &tam[i]);
		long long int soma = 0;
		for (int i = 0; i < N; i++) soma += tam[i];
		if (soma <= k) {
			printf("%lld\n", soma*R);
			continue;
		}
		long long int atu = 0;
		long long int resp = 0;
		long long int i;
		for (i = 0; i < R; i++) {
			long long int ja = 0;
			while (ja <= k) {
				ja += tam[atu];
				atu = (atu+1)%N;
			}
			atu = (atu + N - 1) % N;
			ja -= tam[atu];
			resp += ja;
			if (ult[atu] != -1) {
				i++;
				break;
			}
			ult[atu] = i+1;
			valult[atu] = resp;
		}
		if (R == i) {
			printf("%lld\n", resp);
			continue;
		}
		long long int qts = (R-i)/(i - ult[atu]);
		resp += qts*(resp-valult[atu]);
		for (i += qts*(i-ult[atu]); i < R; i++) {
			long long int ja = 0;
			while (ja <= k) {
				ja += tam[atu];
				atu = (atu+1)%N;
			}
			atu = (atu + N - 1) % N;
			ja -= tam[atu];
			resp += ja;
		}
		printf("%lld\n", resp);
	}
	return 0;
}
