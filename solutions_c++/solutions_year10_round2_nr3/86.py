#include <stdio.h>
#include <math.h>
#include <string.h>
#include <utility>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <iostream>
using namespace std;

#define TRACE(x...)
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x << " = " << x << endl)

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define _foreach(it, b, e) for (typeof(b) it = (b); it < (e); ++it)
#define foreach(x...) _foreach(x)
#define rep(i, n) foreach(i, 0, n)

#define MSET(c, v) memset(c, v, sizeof(c))

const int INF = 0x3f3f3f3f; const int NEGINF = 0xC0C0C0C0;
const int NULO = -1;
double EPS = 1.e-10;

inline int cmp(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}
long long PD[510][510]; // PD[N][j] == number of valid subsets in which N is the j-th element
const long long int MAGIC = 100003LL;
long long int fat[510];

pair<long long, long long> find_bezout(long long x, long long y) {
	if (y == 0LL) return make_pair(1ll, 0ll);
	pair<long long, long long> u = find_bezout(y, x%y);
	return make_pair(u.second, ((u.first - (x/y)*u.second)%MAGIC+MAGIC) % MAGIC);
}

long long inv(long long x) {
	pair<long long, long long> b = find_bezout(x, MAGIC); // a*x + b*MAGIC == 1
	return b.first;
}

long long C(int a, int b) {
	if (a < b) return 0;
	long long temp = (fat[a]*inv(fat[b])) % MAGIC;
	return (temp * inv(fat[a-b]))%MAGIC;
}

int main() {
	TRACE(setbuf(stdout, NULL));
	fat[0] = 1;
	foreach(i, 1LL, 501LL) fat[i] = (i*fat[i-1])%MAGIC;
	MSET(PD, 0);
	PD[1][0] = 1;
	for (long long N = 2; N < 501; N++) {
		WATCH(N);
	  for (long long pos = 1; pos < N; pos++) {
			rep(pos2, pos) {
				PD[N][pos] += (PD[pos][pos2]*C(N-pos-1, pos-pos2-1)) % MAGIC;
			}
		}
	}
	int T;
	scanf("%d", &T);
	rep(_42, T) {
		long long int N;
		scanf("%lld", &N);
		long long ans = 0;
		rep(i, N) ans = (ans + PD[N][i]) % MAGIC;
		printf("Case #%d: %lld\n", _42+1, ans);
	}
	return 0;
}
