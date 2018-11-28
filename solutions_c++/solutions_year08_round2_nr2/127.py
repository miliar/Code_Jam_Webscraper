#include <stdio.h>

#define MAX 1024

int set[MAX], prime[MAX], count;

int gcd(int x, int y) {
	int c = x % y;
	for(; c != 0; c = x % y) {
		x = y;
		y = c;
	}
	return y;
}

int root(int x) {
	if(set[x] == x)return x;
	set[x] = root(set[x]);
	return set[x];
}

void merge(int x, int y) {
	int sx = root(x);
	int sy = root(y);
	set[sx] = sy;
}

int maxprime(int x) {
	int i, ans = 0;
	for(i = 0; prime[i] <= x; i++)
		if(x % prime[i] == 0)
			ans = prime[i];
	return ans;
}

int main(int argc, char *argv[])
{
	int i, j, tmp, ans;
	int a, b, p;
	int t, N;

	count = 0;
	prime[count++] = 2;
	for(i = 3; i < MAX; i += 2) {
		for(j = 0; prime[j] * prime[j] <= i; j++)
			if(i % prime[j] == 0)break;
		if(prime[j] * prime[j] > i)
			prime[count++] = i;
	}

	scanf("%d", &N);
	for(t = 1; t <= N; t++) {
		scanf("%d %d %d", &a, &b, &p);

		for(i = a; i <= b; i++)set[i] = i;

		for(i = a; i <= b; i++)
			for(j = i + 1; j <= b; j++) {
				tmp = gcd(i, j);
				tmp = maxprime(tmp);
				if(tmp >= p) {
					merge(i, j);
				}
			}

		ans = 0;
		for(i = a; i <= b; i++)
			if(set[i] == i)ans++;

		printf("Case #%d: %d\n", t, ans);
	}

	return 0;
}
