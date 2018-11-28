#define  _CRT_SECURE_NO_WARNINGS

#include <vector>
#include <string>
#include <set>
#include <sstream>
#include <map>

#define sz(x) (int)((x).size())
#define all(x) (x).begin(), (x).end()
#define contains(x, y) ((x).find(y) != (x).end())

using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef long long int int64;

#define TASK "C-small-attempt0"
const int MAXN = 500;
const int modulo = 100003;

int cache[MAXN + 1][MAXN + 1];

int ccache[MAXN + 1][MAXN + 1];

int C(int n, int m)
{
	if (m > n) return 0;
	if (n == m) return 1;
	if (ccache[n][m] != -1) return ccache[n][m];
	int res = (C(n - 1, m) + C(n - 1, m - 1)) % modulo;
	return ccache[n][m] = res;
}

int Solve(int n, int len)
{
	if (len < 3) return 1;
	if (len < 1) exit(14);
	if (cache[n][len] != -1)
		return cache[n][len];
	int res = 0;
	for (int pos = 1; pos < len; pos++)
	{
		int left = Solve(len, pos);
		int right = C(n - len - 1, len - pos - 1);
		res += ((int64)left * right) % modulo;
	}
	return cache[n][len] = res % modulo;
}

int main()
{
	freopen(TASK ".in", "r", stdin);
	freopen(TASK ".out", "w", stdout);
	memset(cache, -1, sizeof(cache));
	memset(ccache, -1, sizeof(ccache));
	int testCount;
	scanf("%d", &testCount);
	for (int c = 1; c <= testCount; c++)
	{
		int n;
		scanf("%d", &n);
		int res = 0;
		for (int i = 1; i < n; i++)
			res += Solve(n, i);
		res %= modulo;
		printf("Case #%d: %d\n", c, res);
	}
	return 0;
}