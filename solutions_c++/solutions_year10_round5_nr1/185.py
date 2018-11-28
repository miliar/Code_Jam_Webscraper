#include <cstdio>
#include <vector>
#include <cassert>
#define MAX_P 1100000
using namespace std;

int tests, d, k, res[MAX_P];
long long a[10];
bool isp[MAX_P];
vector<long long> p;

long long exgcd(long long a, long long b, long long &x, long long &y) {
	if (b == 0) {
		x = 1;
		y = 0;
		return a;
	} else {
		long long d = exgcd(b, a % b, x, y);
		long long nx = y;
		long long ny = x - (a / b) * y;
		x = nx;
		y = ny;
		return d;
	}
}

long long inv(long long a, long long m) {
	long long x, y;
	long long d = exgcd(a, m, x, y);
	//printf("%lld %lld\n", a, m);
	assert(d == 1);
	long long ans = (x % m + m) % m;
	assert((a * ans) % m == 1);
	return ans;
}

int main() {
	fill(isp, isp + MAX_P, true);
	isp[0] = isp[1] = false;
	for (int i = 2; i < MAX_P; i++)
		if (isp[i])
			for (int j = i + i; j < MAX_P; j += i)
				isp[j] = false;
	for (int i = 0; i < MAX_P; i++)
		if (isp[i])
			p.push_back((long long)i);
	//printf("%d\n", p.size());
	scanf("%d", &tests);
	for (int tc = 1; tc <= tests; tc++) {
		scanf("%d %d", &d, &k);
		for (int i = 0; i < k; i++)
			scanf("%lld", &a[i]);
		printf("Case #%d: ", tc);
		if (k == 1) {
			printf("I don't know.\n");
			continue;
		}
		long long p10 = 1;
		while (d--) p10 *= 10;
		long long ile = 0, rozw;
		for (int indP = 0; p[indP] < p10; indP++) {
			long long P = p[indP];
			bool bad = false;
			for (int i = 0; i < k; i++)
				if (a[i] < 0 || a[i] >= P) {
					bad = true;
					break;
				}
			if (bad)
				continue;
			//printf("%lld\n", P);
			if (k == 2) {
				long long A = 0, B = a[1];
				long long S = (A * a[1] + B) % P;
				if (res[S] != tc) {
					res[S] = tc;
					rozw = S;
					ile++;
				}
				A = 1, B = a[1] - a[0];
				S = (A * a[1] + B) % P;
				if (res[S] != tc) {
					res[S] = tc;
					rozw = S;
					ile++;
				}
			} else {
					long long A = -1, B = -1;
					bool ok = true;
					for (int i = 0; i < k - 2; i++) {
						long long L1 = ((a[i + 1] - a[i + 2]) % P + P) % P;
						long long L2 = ((a[i] - a[i + 1]) % P + P) % P;
						if (L2 == 0) {
							for (int j = i; j < k; j++)
								if (a[j] != a[i])
									ok = false;
							break;
						}
						long long L3 = (L1 * inv(L2, P)) % P;
						if (A == -1 || A == L3) {
							A = L3;
							long long NB = ((a[1] - A * a[0]) % P + P) % P;
							if (B == -1 || B == NB) B = NB;
							else ok = false;
						} else {
							ok = false;
							break;
						}
					}
					if (ok) {
						if (A != -1) {
							long long S = (A * a[k - 1] + B) % P;
							if (res[S] != tc) {
								res[S] = tc;
								rozw = S;
								ile++;
							}
						} else {
							if (res[a[0]] != tc) {
								res[a[0]] = tc;
								rozw = a[0];
								ile++;
							}
						}
					}
			}
			if (ile > 1) {
				break;
			}
		}
		assert(ile >= 1);
		if (ile == 1) {
			printf("%lld\n", rozw);
		} else {
			printf("I don't know.\n");
		}
	}
	return 0;
}