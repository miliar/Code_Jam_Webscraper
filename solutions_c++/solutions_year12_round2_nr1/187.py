#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int MaxN = 205;
const double eps = 1e-10;
int s[MaxN];
int N, sum;

int sgn(double x) {
	return x < -eps ? -1 : x > eps;
}

bool sol(int id, double d) {
	double score = s[id] + sum * d / 100.0;
	double left = 100.0 - d;
	for (int i = 0; i < N; i++) {
		if (i == id) continue;
		if (sgn(s[i] - score) >= 0) continue;
		double rate = (score - s[i]) * 100.0 / sum;
		if (sgn(rate - left) >= 0) return true;
		left -= rate;
	}
	
	return false;
}

int main() {
	int T;
	int cas = 1;
	
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	scanf("%d", &T);
	while (T--) {
		scanf("%d", &N);
		sum = 0;
		for (int i = 0; i < N; i++) {
			scanf("%d", &s[i]);
			sum += s[i];
		}
		printf("Case #%d:", cas++);
		for (int i = 0; i < N; i++) {
			double L = 0, R = 100.0, mid;
			for (int j = 0; j < 200; j++) {
				mid = (L + R) / 2.0;
				if (sol(i, mid)) R = mid;
				else L = mid;
			}
			mid = (L + R) / 2.0;
			printf(" %.8f", mid);
		}
		puts("");
	}
	
	return 0;
}

