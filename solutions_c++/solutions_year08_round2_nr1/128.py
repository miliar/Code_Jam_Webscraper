#include <stdio.h>

#define MAX 1024

long long data[9];

int main(int argc, char *argv[])
{
	int i, j, k, l;
	long long n, A, B, C, D, x, y, M;
	long long X, Y, ans;
	int t, N;

	scanf("%d", &N);
	for(t = 1; t <= N; t++) {
		scanf("%lld %lld %lld %lld %lld %lld %lld %lld", &n, &A, &B, &C, &D, &x, &y, &M);

		for(i = 0; i < 9; i++)data[i] = 0;

		X = x;
		Y = y;
		data[(X % 3) * 3 + Y % 3]++;
		for(i = 1; i < n; i++) {
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
			data[(X % 3) * 3 + Y % 3]++;
		}

		ans = 0;
		for(i = 0; i < 9; i++)
			for(j = i; j < 9; j++)
				for(k = j; k < 9; k++)
					if((i / 3 + j / 3 + k / 3) % 3 == 0)
						if((i % 3 + j % 3 + k % 3) % 3 == 0) {
							if(i != j && j != k && i != k)
								ans += data[i] * data[j] * data[k];
							else if(i == j && j == k) {
								ans += data[i] * (data[i] - 1) * (data[i] - 2) / 6;
							} else {
								if(i == j) {
									ans += data[i] * (data[i] - 1) * data[k] / 2;
								} else if(j == k) {
									ans += data[j] * (data[j] - 1) * data[i] / 2;
								} else {
									ans += data[i] * (data[i] - 1) * data[j] / 2;
								}
							}
						}

		printf("Case #%d: %lld\n", t, ans);
	}

	return 0;
}
