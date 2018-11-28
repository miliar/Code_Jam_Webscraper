// Adrian Kügel
#include <stdio.h>
#include <vector>
#include <set>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <map>
#include <assert.h>
#include <limits.h>
#include <complex>
#include <algorithm>
#include <ctype.h>
#include <string>
using namespace std;

typedef set<int> SI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef complex<double> tComp;

long long gcd(long long a, long long b) {
	return b?gcd(b, a%b): a;
}

int cnt[1001], cnt2[1001];
int p[1001];
int cur[1001];
int l;

void get_cnt(int num) {
	memset(cur, 0, sizeof(int) * l);
	for (int i=0; i<l; ++i) {
		while(num % p[i] == 0) {
			num /= p[i];
			++cur[i];
		}
	}
}

int main() {
	int tc, n;
	for (int i=2; i<=1000; ++i) {
		if (!p[i]) {
			p[l++] = i;
			for (int j=i*i; j<=1000; j+=i)
				p[j] = 1;
		}
	}
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		scanf("%d", &n);
		if (n == 1) {
			puts("0");
			continue;
		}
		memset(cnt, 0, sizeof(int) * l);
		for (int i=1; i<=n; ++i) {
			get_cnt(i);
			bool changed = (i == 1);
			for (int j=0; j<l; ++j) {
				if (cur[j] > cnt[j]) {
					changed = true;
					cnt[j] = cur[j];
				}
			}
		}
		int c1 = 1;
		for (int i=0; i<l; ++i)
			c1 += cnt[i];
		memset(cnt2, 0, sizeof(int) * l);
		int c2 = 0;
		for (int i=n; i>=1; --i) {
			get_cnt(i);
			bool changed = false;
			bool valid = false;
			for (int j=0; j<l; ++j) {
				if (cnt[j] && cur[j] == cnt[j]) valid = true;
				if (cur[j] > cnt2[j]) {
					changed = true;
					cnt2[j] = cur[j];
				}
			}
			if (!valid) continue;
			if (changed) ++c2;
		}
		printf("%d\n", c1-c2);
	}
	return 0;
}
