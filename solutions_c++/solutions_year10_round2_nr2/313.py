#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <memory.h>
#include <string.h>
#include <string>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

#define FOR(i, n) for (int i = 0; i < (int)(n); i++)
#define CL(x) memset(x, 0, sizeof(x));

typedef long long LL;
typedef vector<int> vi;
typedef vector<string> VS;


int x[1000];
int v[1000];

void Solve()
{
	int n, k, B, T;
	scanf("%d %d %d %d", &n, &k, &B, &T);
	FOR(i, n)
		scanf("%d", &x[i]);
	FOR(i, n)
		scanf("%d", &v[i]);
	vector<int> vv;
	FOR(i, n)
		if (B - x[i] <= T * v[i])
		{
			int cnt = 0;
			FOR(j, n)
				if (x[i] < x[j] && B - x[j] > T * v[j])
					cnt++;
			vv.push_back(cnt);
		}
	if (vv.size() < k)
		printf("IMPOSSIBLE\n");
	else
	{
		int res = 0;
		sort(vv.begin(), vv.end());
		FOR(i, k)
			res += vv[i];
		printf("%d\n", res);
	}
}

int main()
{
	freopen("c:\\my\\in.txt", "r", stdin);
	freopen("c:\\my\\out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	FOR(i, t)
	{
		printf("Case #%d: ", i + 1);
		Solve();
	}
	return 0;
}