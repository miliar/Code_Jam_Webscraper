#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>

using namespace std;

#define EPS 1e-8

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef vector<double> VD;
typedef pair<int, int> PII;
typedef set<int> SI;
typedef map<int, int> MII;

const int maxn = 64;

char s[maxn];
int sign[maxn];
LL num[maxn];
LL ans = 0;

int isUgly(LL x) {
	if (!x) return 1;
	if (x % 2 == 0) return 1;
	if (x % 3 == 0) return 1;
	if (x % 5 == 0) return 1;
	if (x % 7 == 0) return 1;
	return 0;
}

void getSign(int x) {
	int i = 0;
	memset(sign, 0, sizeof(sign));
	do {
		sign[i++] = x % 3;
		x /= 3;
	} while (x);
}

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int cases, n, d;
	scanf("%d\n", &cases);
	for (int cc = 1; cc <= cases; ++cc) {
		printf("Case #%d: ", cc);
		gets(s);
		n = strlen(s);
		d = 1;
		for (int i = 1; i < n; ++i) d *= 3;
		ans = 0;
		for (int i = 0; i < d; ++i) {
//			printf("i = %d\n", i);
			getSign(i);
			memset(num, 0, sizeof(num));
			int nn = 0, dd = 1; // 1 -1
			for (int k = 0; k < n - 1; ++k) {
//				printf("%d ", sign[k]);
				if (sign[k] == 0)
					num[nn] = num[nn] * 10 + s[k] - '0';
				else
					if (sign[k] == 1) {
						num[nn] = num[nn] * 10 + (s[k] - '0');
						num[nn] *= dd;
						dd = 1;
						++nn;
					}
					else {
							num[nn] = num[nn] * 10 + (s[k] - '0');
							num[nn] *= dd;
							dd = -1;
							++nn;
					}
			}
			num[nn] = num[nn] * 10 + (s[n - 1] - '0');
			num[nn] *= dd;
			++nn;
//			printf("\n");
			LL x = 0;
			for (int j = 0; j < nn; ++j) {
//				printf("num[%d] = %d\n", j, num[j]);
				x += num[j];
			}
//			cout << x << "\n";
			if (isUgly(x)) ++ans;
		}
		cout << ans << "\n";
	}
	return 0;
}

