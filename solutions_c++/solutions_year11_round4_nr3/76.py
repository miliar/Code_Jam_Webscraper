#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cmath>

using namespace std;

const int MAXN = 1005;

int T;
long long N;

bool p[MAXN * MAXN];
int ct[MAXN * MAXN];

int main() {
	for(int i = 2 ; i * i <= 1000000 ; i++) {
		if (!p[i]) {
			for(int j = i * i ; j <= 1000000 ; j+=i) {
				p[j] = true;
			}
		}
	}
	ct[1] = 0;
	for(int i = 2 ; i <= 1000000 ; i++) {
		ct[i] = ct[i - 1] + (p[i] ? 0 : 1);
	}

	scanf("%d",&T);
	for(int t = 1 ; t <= T ; t++) {
		scanf("%lld",&N);
		long long x = (long long)sqrt((double)(N + 5));
		while (x * x > N) {x--;}
		int ans = 1;
		for(int i = 2 ; i <= x ; i++) {
			if (!p[i]) {
				long long N2 = N;
				while (N2 >= i) {
					N2 /= i;
					ans++;
				}
				ans--;
			}
		}
		if (N == 1) {ans = 0;}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
