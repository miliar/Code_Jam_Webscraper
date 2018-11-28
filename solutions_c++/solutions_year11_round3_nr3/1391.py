#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

int n, L, H;
long long num[1000], gcd[1000], lcm[1000];

long long GCD(long long a,long long b) {
	if(a > b) {
		long long tmp = a;
		a = b;
		b = tmp;
	}

	while(a != 0) {
		long long tmp = a;
		a = b%a;
		b = tmp;
	}
	return b;
}

void input() {
	scanf("%d%lld%lld", &n, &L, &H);
	for(int i = 0;i < n;i ++) scanf("%lld", &num[i]);
}

int find(long long a, long long b) {
	if(a > b||b%a != 0) return 0;
	long long c = b/a;
	long long mm = -1;
	for(int i = 1;i <= c;i ++) {
		if(i * a > H) return 0;
		if(c%i == 0) {
			if(i * a >= L) {
				printf("%lld\n", i*a);
				return 1;
			}
			else if(c/i * a >= L && c/i * a <= H) mm = c/i * a;
		}
		if(i*i > c) {
			i = c;
			continue;
		}
	}
	if(mm != -1) {
		printf("%lld\n", mm); 
		return 1;
	}
	return 0;
}

void solve() {
	sort(num, num+n);

	lcm[0] = num[0];
	for(int i = 1;i < n;i ++) lcm[i] = H+1;
	for(int i = 1;i < n;i ++) {
		lcm[i] = lcm[i-1]/GCD(lcm[i-1], num[i]);
		lcm[i] *= num[i];
		if(lcm[i] > H||lcm[i] <= 0) {
			lcm[i] = H+1;
			break;
		}
	}
	gcd[n-1] = num[n-1];
	for(int i = n-2;i >= 0;i --) gcd[i] = GCD(num[i], gcd[i+1]);

	//for(int i = 0;i < n;i ++) printf("%lld %lld %lld\n", num[i], lcm[i], gcd[i]);

	if(find(1, gcd[0])) return ;

	for(int i = 0;i < n-1;i ++) {
		if(find(lcm[i], gcd[i+1])) return ;
		int xx = 0;
		xx++;
	}

	if(lcm[n-1] <= H) {
		if(lcm[n-1] >= L) {
			printf("%d\n",lcm[n-1]);
			return ;
		}
		long long a = lcm[n-1];
		long long b = H;

		long long c = b/a;
		for(int i = 1;i <= c;i ++) {
			if(i * a >= L) {
				printf("%lld\n", i*a);
				return ;
			}
		}
	}
	else printf("NO\n");
}

int main() {
	freopen("C-small-attempt4.in", "r", stdin);
	freopen("output", "w", stdout);

	//freopen("text.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int cas = 1;cas <= T;cas ++) {
		input();
		printf("Case #%d: ", cas);
		solve();
	}
	return 0;
}
