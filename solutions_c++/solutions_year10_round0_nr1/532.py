#include <stdio.h>
#include <memory.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

#define FOR(i, n)	for (int i = 0; i < (int) (n); i++)
#define RFOR(i, n)	for (int i = (int) (n) - 1; i >= 0; i--)
#define CL(x)		memset(x, 0, sizeof(x))
#define CLX(x, v)	memset(x, v, sizeof(x))
#define ALL(x)		(x).begin(), (x).end()
#define PB			push_back
#define MP			make_pair

typedef long long LL;
typedef unsigned long long UL;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

/////////////////////////////////////////////////////////////

int D(int n, int k)
{
	if (n == 0) return 0;

	k %= (1 << n);
	if (k == 0) return 0;

	int i = 0;
	while ((1 << i) <= k) i++;
	i--;

	return D(i, k - (1 << i)) + (1 << i);
}

void solve(int n, int k)
{
	int m = D(n, k);
	if (m == (1 << n) - 1) printf("ON\n");
	else printf("OFF\n");
}

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int tt;
	scanf("%d", &tt);

	FOR(i, tt)
	{
		int n, k;
		scanf("%d %d", &n, &k);
		printf("Case #%d: ", i+1);
		solve(n, k);
	}

	return 0;
}
