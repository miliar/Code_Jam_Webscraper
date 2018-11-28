#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <numeric>
#include <functional>
#define rep(i,n) for(int i=0;i<(n);++i)
#define foreach(i,v) for(__typeof(v.begin()) i=v.begin();i!=v.end();++i)
#define ass(v) (v)||++*(int*)0;
using namespace std;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<bool> VB;
typedef vector<double> VD;
int state(int s, int p)
{
	int res = 0;
	for (int i = 0; i <= 10 && i <= s; ++i)
		for(int j = i; j <= 10 && i + j * 2 <= s; ++j)
		{
			int k = s - i - j;
			if (k - i > 2) continue;
			else if (k - i == 2)
			{
				if (k >= p) res |= 1; else res |= 4;
			}
			else
			{
				if (k >= p) res |= 2; else res |= 8;
			}
		}
	return res;
}
int main()
{
	int t;
	scanf("%d", &t);
	for (int cs = 1; cs <= t; ++cs)
	{
		int n, s, p;
		scanf("%d%d%d", &n, &s, &p);
		int f[128][128] = {};
		rep(i, s) f[0][i + 1] = INT_MIN;
		rep(i, n)
		{
			int z;
			scanf("%d", &z);
			int r = state(z, p);
			for (int j = 0; j <= s && j <= i + 1; ++j)
			{
				int &ans = f[i + 1][j];
				if ((r & 1) && j > 0)
				{
					ans = max(ans, f[i][j - 1] + 1);
				}
				if (r & 2)
				{
					ans = max(ans, f[i][j] + 1);
				}
				if ((r & 4) && j > 0)
				{
					ans = max(ans, f[i][j - 1]);
				}
				if (r & 8)
				{
					ans = max(ans, f[i][j]);
				}
			}
		}
		printf("Case #%d: %d\n", cs, f[n][s]);
	}
	return 0;
}
