#include <iostream>
using namespace std;

const int MaxN = 1000010;

int TCase, A1, A2, B1, B2, Pos[MaxN];
long long Ans;

bool Check(int a, int b) {
	if (b > a) swap(a, b);
	for (bool w = 1; ; w ^= 1) {
		if (b == 0 || a / b > 1) return w;
		swap(a, b), b %= a;
	}
}

long long Ask(int x) {
	int l = Pos[x], r = Pos[x] + x - 1;
	if (B2 < l) return B2 - B1 + 1;
	if (B1 < l) {
		if (B2 <= r) return l - B1;
		return l - B1 + B2 - r;
	}
	if (B1 <= r) return max(0, B2 - r);
	return B2 - B1 + 1;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	Pos[1] = 1;
	for (int i = 2; i < MaxN; ++i) {
		Pos[i] = Pos[i - 1];
		while (Check(Pos[i], i)) ++Pos[i];
	}
	scanf("%d", &TCase);
	for (int Case = 1; Case <= TCase; ++Case) {
		scanf("%d%d%d%d", &A1, &A2, &B1, &B2);
		Ans = 0;
		for (int i = A1; i <= A2; ++i)
			Ans += (long long)Ask(i);
		printf("Case #%d: %lld\n", Case, Ans);
	}
	return 0;
}
