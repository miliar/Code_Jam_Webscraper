#include <cstdio>
#include <cassert>
#include <algorithm>

using namespace std;

typedef long long Int64;

const int maxn = 100000;

Int64 freq[maxn], lcm[maxn], gcd[maxn];
Int64 L, H;
int n;

Int64 GCD(Int64 a, Int64 b) {
	return !b ? a : GCD(b, a % b);
}

bool Check(Int64 lower, Int64 upper) {
	if (lower > upper || L > H) return false;
	if (H < lower || upper < L) return false;
	if (upper % lower != 0) return false;
	//printf("%I64d %I64d\n", lower, upper);
	//printf("%I64d\n", lower < L ? L : lower);
	Int64 answer = lower;
	for (; answer < L; answer += lower);
	for (; answer <= upper / 2/* / answer*/ && upper % answer != 0; answer += lower);
	if (upper % answer == 0 && answer <= H) {
		printf("%I64d\n", answer);
		return true;
	}
	if (upper <= H) {
		printf("%I64d\n", upper);
		return true;
	}
	return false;
}

void solve() {
	scanf("%d %I64d %I64d", &n, &L, &H);
	for (int i = 0; i < n; i++) {
		scanf("%I64d", &freq[i]);
		assert(freq[i] >= 1);
	}
	sort(freq, freq + n);
	lcm[0] = freq[0];
	for (int i = 1; i < n; i++) {
		if (lcm[i - 1] == -1) {
			lcm[i] = -1;
			continue;
		}
		Int64 gcd = GCD(lcm[i - 1], freq[i]);
		Int64 a = lcm[i - 1] / gcd;
		if (a > H / freq[i]) lcm[i] = -1;
		else lcm[i] = a * freq[i];
	}
	gcd[n - 1] = freq[n - 1];
	for (int i = n - 2; i >= 0; i--)
		gcd[i] = GCD(gcd[i + 1], freq[i]);
	//printf("LCM:");
	//for (int i = 0; i < n; i++)
	//	printf(" %I64d", lcm[i]);
	//printf("\n");
	//printf("GCD:");
	//for (int i = 0; i < n; i++)
	//	printf(" %I64d", gcd[i]);
	//printf("\n");
	if (Check(1, gcd[0])) return;
	for (int i = 0; i < n - 1; i++) {
		if (lcm[i] == -1) break;
		if (Check(lcm[i], gcd[i + 1])) return;
	}
	if (lcm[n - 1] != -1) {
		Int64 res = lcm[n - 1];
		for (; res < L; res += lcm[n - 1]);
		if (res <= H) printf("%I64d\n", res);
		else printf("NO\n");
	} else printf("NO\n");
}

void solve_2() {
	scanf("%d %I64d %I64d", &n, &L, &H);
	for (int i = 0; i < n; i++) {
		scanf("%I64d", &freq[i]);
		assert(freq[i] >= 1);
	}
	Int64 answer;
	for (answer = L; answer <= H; answer++) {
		int i;
		for (i = 0; i < n; i++)
			if (freq[i] % answer != 0 && answer % freq[i] != 0) break;
		if (i >= n) {
			printf("%I64d\n", answer);
			break;
		}
	}
	if (answer > H) printf("NO\n");
}

int main() {
	int t, i;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		//solve();
		solve_2();
	}
	return 0;
}