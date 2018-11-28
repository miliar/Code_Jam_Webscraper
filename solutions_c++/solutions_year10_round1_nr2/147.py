#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <set>
#include <ctime>
#include <map>
#include <queue>
#include <stack>
#include <string>

using namespace std;

#define Filename "b"
#define sqr(a) (a)*(a)
#define abs(a) ((a) < 0 ? -(a) : (a))
#define nextline for (int CcC = getchar();CcC != '\n' && CcC != EOF;CcC = getchar());

typedef long long lng;
typedef long double ldb;

const int INF = (1 << 30);
const double EPS = 1e-9;

int D, I, M, N, a[105], dp[105][270];

bool was[105][270];

void Load()
{
	cin >> D >> I >> M >> N;
	for (int i = 0;i < N;i++)
		cin >> a[i];
}

int go (int pos, int v)
{
	if (pos == N) return 0;
	if (was[pos][v]) return INF;
	if (dp[pos][v] != -1) return dp[pos][v];
	int &res = dp[pos][v];
	res = go (pos+1, v) + D;
	for (int i = 0;i < 256;i++)
		if (abs (v - i) <= M)
			res = min(res, go (pos+1, i) + abs(a[pos] - i));
	for (int i = 0;i < 256;i++)
		if (abs (v - i) <= M)
		{
			res = min(res, go (pos, i) + I);
			//if (pos == 1 && v == 14)
			//	cerr << res << " " << i <<  " " << go (pos, i) << " " << I << endl;
		}
	was[pos][v] = 0;
	//cerr << pos << " " << v << " " << res << endl;
	return res;
}

int main()
{
	freopen(Filename".in", "r", stdin);
	freopen(Filename".out", "w", stdout);
	int T;
	cin >> T;
	for (int step = 0;step < T;step++)
	{
		Load();
		memset(dp, -1, sizeof(dp));
		memset(was, 0, sizeof(was));
		printf("Case #%d: ", step+1);
		int ans = INF, cur = 0;
		for (int j = 0;j < N;j++)
		{
			for (int i = 0;i < 256;i++)
			{
				ans = min(ans, go (j+1, i) + abs(a[j] - i) + cur);
				//cerr << ans << " ";
			}
			cur += D;
		}
		//cerr << endl;
		for (int i = 0;i < 256;i++)
			ans = min(ans, go (0, i) + I);
		printf("%d\n", ans);
	}
	return 0;
}
