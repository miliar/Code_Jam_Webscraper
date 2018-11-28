#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

int D, n;

int const maxpp = 1000007, maxp = 200000;
bool tt[maxpp];
int l, prime[maxp];
void Eratosthenes(){
	tt[1] = true;
	int temp = int(sqrt(double(maxpp)));
	for (int i = 2; i < temp; i++)
		if (!tt[i]){
			for (int j = i * 2; j < maxpp; j+=i)
				tt[j] = true;
		}
		l = 0;
		for (int i = 2; i <= maxpp; i++)
			if (!tt[i]) prime[l++] = i;
}

int a[32];

int power_mod(int a, int b, int n){
	int x=a % n, y=1;
	while (b > 0){
		if (b & 1) y = ((long long)y * x) % n; 
		x = (long long)x * x % n; b>>=1;
	}
	return y;
}

int check(int t) {
	if (a[0] >= t || a[1] >= t) return -1;
	int A = (long long)(a[2]-a[1]) * power_mod(a[1] - a[0], t-2, t) % t;
	if (A < 0) A += t;
	int B = ((a[1] - (long long)A * a[0]) % t + t) % t;
	for (int i = 2; i < n; ++i)
		if (a[i] != ((long long)a[i-1]*A+B) % t) return -1;
	return ((long long)a[n-1]*A+B) % t;
}

void solve() {
	scanf("%d%d", &D, &n);
	for (int i = 0; i < n; ++i) {
		scanf("%d", a+i);
	}
	int t = 1;
	while (D--) t*=10;
	int ans = -1;
	if (n > 2)
	for (int i = 2; i <= t; ++i) {
		if (!tt[i]) {
			int next = check(i);
			if (next != -1) {
				if (next == -2) {
					printf("I don't know.\n");
					return;
				}
				if (ans == -1 || ans == next) {
					ans = next;
				} else {
					printf("I don't know.\n");
					return;
				}
			}
		}
	}
	if (n == 2 && a[0] == a[1]) {
		ans = a[0];
	}
	if (ans == -1)
		printf("I don't know.\n");
	else
		printf("%d\n", ans);
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	Eratosthenes();
	int T, tc = 0;
	scanf("%d", &T);
	while ( T -- ) {
		printf("Case #%d: ", ++tc);
		solve();
		fprintf(stderr, "%d\n", tc);
	}
	return 0;
}
