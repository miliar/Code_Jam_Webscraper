#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <cassert>
using namespace std;

#define ALL(v) (v).begin(), (v).end()
#define SZ(v) (int)((v).size())
#define FOR(i, a, b) for(__typeof(a) i = (a); i < (b); i++)
#define CLEAR(a, b) memset((a), (b), sizeof(a))

const int MOD = 1000;

int c[32][32];

int C(int, int);
int pow(int, int);

int main()
{
	CLEAR(c, -1);
	int T;
	scanf("%d", &T);
	FOR(t, 0, T) {
		int n; scanf("%d", &n);
		int res = 999;
		FOR(i, 0, n+1) if(i%2 == 0) {
			res += 2*C(i, n)*pow(5, i/2)*pow(3, n-i);
			res %= MOD;
		}
		printf("Case #%d: %03d\n", t+1, res);
	}
	return 0;
}

int C(int n, int m)
{
	if(n < 0 || n > m) return 0;
	if(n == 0 && n == m) return 1;
	if(c[n][m] != -1) return c[n][m];
	else return c[n][m] = (C(n, m-1)+C(n-1, m-1))%MOD;
}
int pow(int a, int b)
{
	a %= MOD;
	if(b == 0) return 1;
	if(b == 1) return a;
	int m = pow(a, b/2), res = (m*m)%MOD;
	if(b%2 == 1) res = (res*a)%MOD;
	return res;
}

