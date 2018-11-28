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

const int INF = (1 << 29);
const double EPS = 1e-9;

int P, M[10005], st[1 << 10][1 << 10];

lng dp[1 << 10][1 << 10][12];

void Load()
{
	scanf("%d", &P);

	for (int i = 0;i < (1 << P);i++)
		scanf("%d", &M[i]);

	for (int i = 0;i < P;i++)
	{
		int l = 0, r = (1 << (i+1)) -1;
		for (int j = 0;j < (1 << (P - i - 1));j++, l = r+1, r += (1 << (i+1)))
			scanf("%d", &st[l][r]);
	}
}

lng go (int l, int r, int pr)
{
	if (l == r) 
	{
		if (M[l] < pr) return INF;
		return 0;
	}

	lng &res = dp[l][r][pr];

	if (res != -1) return res;

	res = INF;

	int mid = (l+r) / 2;

	lng t1 = go (l, mid, pr) + go (mid+1, r, pr) + st[l][r];
	lng t2 = go (l, mid, pr+1) + go (mid+1, r, pr+1);

	res = min(t1, t2);

	return res;
}

int main()
{
	freopen(Filename".in", "r", stdin);
	freopen(Filename".out", "w", stdout);
	int t;
	cin >> t;
	for (int sh = 0;sh < t;sh++)
	{
		Load();
		memset(dp, -1, sizeof(dp));
		printf("Case #%d: %d\n", sh+1, (int)go (0, (1 << P) - 1, 0));
	}
	return 0;
}
