#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

const int MAXM = 1100000;

int prime[MAXM];

void prepare() {
	for (int i=2;i<=MAXM;i++) prime[i] = 1;
	for (int i=2;i<=MAXM;i++)
		if (prime[i]) {
			for (int j=i+i;j<=MAXM;j+=i)
				prime[j] = 0;
		}
	//for (int i=2;i<=100;i++) if (prime[i]) printf("%d ", i); printf("\n");
}

long long n;

int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	prepare();
	int T;
	cin>>T;
	for (int ti=1;ti<=T;ti++) {
		cin>>n;
		int ans = 0;
		for (int i=2;(long long)i*i<=n;i++) {
			if (prime[i]) {
				long long t = i; int k = 1;
				while (t * i <= n) {
					t *= i;
					k ++;
				}
				ans += k - 1;
			}
		}
		if (n == 1) ans = 0; else ans ++;
		printf("Case #%d: %d\n", ti, ans);
	}
	return 0;
}
