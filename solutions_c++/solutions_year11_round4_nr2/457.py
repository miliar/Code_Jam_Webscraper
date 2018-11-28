#if 1
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <stack>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <functional>
#include <algorithm>
#include <cmath>
#include <bitset>
#include <cstdio>
#include <list>
#include <ctime>
using namespace std;

typedef long long LL;
typedef long double LD;
const LD eps = 1e-9;

typedef pair<int, int> pii;
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define iss istringstream
#define oss ostringstream
#define dbg(x) cerr << #x << " = " << x << endl;
#define dbgv(x) { cerr << #x << ": {"; for(int i = 0; i < x.size(); ++i) { if(i) cerr << ", "; cerr << x[i]; } cerr << "}" << endl; }

const int maxn = 512;
int a[maxn][maxn];
LL sxm[maxn][maxn];
LL sym[maxn][maxn];
LL sm[maxn][maxn];

char str[maxn];
void gen()
{
	freopen("input.txt", "w", stdout);
	cout << 1 << endl;
	cout << 500 << " " << 500 << " " << 1000000 << endl;
	for(int i = 0; i < 500; ++i)
	{
		for(int j = 0; j < 500; ++j)
			cout << rand() % 10;
		cout << endl;
	}
	exit(0);
}
int main()
{
	//gen();
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	memset(sxm, 0, sizeof sxm);
	memset(sym, 0, sizeof sym);
	memset(sm, 0, sizeof sm);
	for(int z = 0; z < t; ++z)
	{
		int n, m, d;
		scanf("%d%d%d", &n, &m, &d);
		for(int i = 0; i < n; ++i)
		{
			scanf("%s", str);
			for(int j = 0; j < m; ++j)
				a[i][j] = str[j] - '0' + d;
		}

		memset(sm, 0, sizeof sm);
		memset(sxm, 0, sizeof sxm);
		memset(sym, 0, sizeof sym);

		for(int i = 1; i <= n; ++i)
			for(int j = 1; j <= m; ++j)
			{
				sm[i][j] = a[i - 1][j - 1] + sm[i - 1][j] + sm[i][j - 1] - sm[i - 1][j - 1];
				sxm[i][j] = a[i - 1][j - 1] * (i - 1) + sxm[i - 1][j] + sxm[i][j - 1] - sxm[i - 1][j - 1];
				sym[i][j] = a[i - 1][j - 1] * (j - 1) + sym[i - 1][j] + sym[i][j - 1] - sym[i - 1][j - 1];
				//assert(sm[i][j] >= 0);
				//assert(sxm[i][j] >= 0);
				//assert(sym[i][j] >= 0);
			}

		int ans = -1;
		for(int k = min(n, m); k >= 3; --k)
		{
			for(int x = 0, endx = n - k; x <= endx; ++x)
			for(int y = 0, endy = m - k; y <= endy; ++y)
			{
				LL sumM =  sm[x + k][y + k] - sm[x + k][y] - sm[x][y + k] + sm[x][y];
				LL sumXM = sxm[x + k][y + k] - sxm[x + k][y] - sxm[x][y + k] + sxm[x][y];
				LL sumYM = sym[x + k][y + k] - sym[x + k][y] - sym[x][y + k] + sym[x][y];

				sumM -= a[x][y] + a[x + k - 1][y] + a[x][y + k - 1] + a[x + k - 1][y + k - 1];
				sumXM -= a[x][y] * x + a[x + k - 1][y] * (x + k - 1) + a[x][y + k - 1] * x + a[x + k - 1][y + k - 1] * (x + k - 1);
				sumYM -= a[x][y] * y + a[x + k - 1][y] * y + a[x][y + k - 1] * (y + k - 1) + a[x + k - 1][y + k - 1] * (y + k - 1);

				//assert(sumM >= 0);
				//assert(sumXM >= 0);
				//assert(sumYM >= 0);

				if(k & 1)
				{
					if(sumM * (x + k / 2) == sumXM && sumM * (y + k / 2) == sumYM)
					{
						ans = k;
						goto answer;
					}
				} else
				{
					if(sumM * (2 * x + k - 1) == 2 * sumXM && sumM * (2 * y + k - 1) == 2 * sumYM)
					{
						ans = k;
						goto answer;
					}
				}
			}
		}
answer:
		if(ans == -1)
			cout << "Case #" << z + 1 << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << z + 1 << ": " << ans << endl;

	}
	return 0;
}
#endif

