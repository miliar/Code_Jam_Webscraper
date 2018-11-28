#include <cstdio>

int n;
int st[32];

int getsum(int t) {
	int ret = 0;
	for (int i = 0; i < n; ++i) {
		if (t & 1u << i)
			ret += st[i];
	}
	return ret;
}

int getxor(int t) {
	int ret = 0;
	for (int i = 0; i < n; ++i) {
		if (t & 1u << i)
			ret ^= st[i];
	}
	return ret;
}
int getnxor(int t) {
	int ret = 0;
	for (int i = 0; i < n; ++i) {
		if (!(t & 1u << i))
			ret ^= st[i];
	}
	return ret;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int k = 0; k < t; ++k) {
		scanf("%d", &n);
		int sum = 0;
		for (int i = 0; i < n; ++i) {
			scanf("%d", st + i);
			sum += st[i];
		}
		int upb = 1u << n;
		int ret = -1;
		for (int i = 1; i < upb - 1; ++i) {
			int asum = getsum(i);
			int a = getxor(i);
			int b = getnxor(i);
			int bsum = sum - asum;
			if (a == b)
				ret >?= (asum >? bsum);					
		}
		if (ret != -1)
			printf("Case #%d: %d\n", k + 1, ret);
		else
			printf("Case #%d: NO\n", k + 1);
	}
	return 0;
}

