#include <cstdio>
#include <cstring>
#define MAXN (1 << 24)
using namespace std;

typedef long long ll;

int a, b, ten[10];
int last[MAXN];

inline ll solve() {
	ll ret = 0;
	int am = 0, x = a;
	while (x) {
		x /= 10;
		am ++;
	}
	am --;
	for (int i=a; i <= b; ++i) {
		int cur = i;
		for (int j=0; j < am; ++j) {
			cur = (cur / 10) + ten[am] * (cur % 10);
			if (cur > i && cur <= b && last[cur] != i) {
				ret ++;
			}
			last[cur] = i;
		}
	}

	return ret;
}

inline void pre() {
	ten[0] = 1;
	for (int i=1; i < 8; ++i)
		ten[i] = ten[i-1] * 10;
}

inline void clear() {
	memset(last, 0, sizeof(last));
}

inline void read() {
	scanf("%d%d", &a, &b);
}

int main() {
	int brt, testNo = 0;
	scanf("%d", &brt);

	pre();
	while (brt --) {
		read();
		printf("Case #%d: %lld\n", ++testNo, solve());
		clear();
	}

	return 0;
}
