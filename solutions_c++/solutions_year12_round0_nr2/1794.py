#include <cstdio>
#define MAXN (1 << 7)
using namespace std;

int n, sup, k;
int total[MAXN];

inline int solve() {
	int sol = 0;
	for (int i=0; i < n; ++i) {
		if ((total[i] + 2) / 3 >= k)
			sol ++;
		else {
			if (sup > 0)
				if (total[i]-k >= 0 && ((total[i]-k) / 2 >= k-2)) {
					sup --;
					sol ++;
				}
		}
	}

	return sol;
}

inline void read() {
	scanf("%d%d%d", &n, &sup, &k);
	for (int i=0; i < n; ++i)
		scanf("%d", &total[i]);
}

int main() {
	int brt, testNo = 0;

	scanf("%d", &brt);
	while (brt --) {
		read();
		printf("Case #%d: %d\n", ++testNo, solve());
	}
	return 0;
}
