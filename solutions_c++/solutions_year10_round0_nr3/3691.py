#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>

using namespace std;

typedef __int64 i64;
int R, k, N;
int g[1024];
i64 s[1024];
int r[1000000];
int hash[1024];
int circle;

int go(int startIdx, int endIdx, int remain)
{
	int idx = lower_bound(s + startIdx, s + endIdx + 1, remain + s[startIdx - 1]) - s;

	if(s[idx] - s[startIdx - 1] == remain)
		return idx;
	else
		return idx - 1;
}

i64 Solve()
{
	i64 ret = 0;
	int i, j;
	int idx = 1;
	circle = 0;
	int startCircle = 0;
	for(i = 0; i < R; i++)
	{
		r[i] = idx;
		hash[idx] = i;
		int sum1 = s[N] - s[idx - 1];
		if(k < sum1)
		{
			int nextIdx = go(idx, N, k);
			ret += s[nextIdx] - s[idx - 1];
			idx = nextIdx + 1;
		}
		else
		{
			int remain = k - sum1;
			ret += sum1;
			if(idx > 1)
			{
				int nextIdx = go(1, idx - 1, remain);
				ret += s[nextIdx];
				idx = nextIdx + 1;
			}
		}
		if(hash[idx] != -1)
		{
			circle = i - hash[idx] + 1;
			startCircle = hash[idx];
			r[i + 1] = idx;
			break;
		}

	}
	if(i >= R)
		return ret;
	ret = 0;
	for(i = 1; i <= startCircle; i++)
	{
		if(r[i] > r[i - 1])
			ret += s[ r[i] - 1 ] - s[ r[i - 1] - 1 ];
		else
			ret += s[N] - s[r[i - 1] - 1] + s[ r[i] - 1];
	}
	R -= startCircle;
	int num = R / circle;
	i64 cNum = 0;
	for(i = startCircle + 1; i <= startCircle + circle; i++)
	{
		if(r[i] > r[i - 1])
			cNum += s[ r[i] - 1 ] - s[ r[i - 1] - 1 ];
		else
			cNum += s[N] - s[r[i - 1] - 1] + s[ r[i] - 1];
	}

	ret += num * cNum;
	R -= num * circle;
	for(i = startCircle + 1; i <= startCircle + R; i++)
	{
		if(r[i] > r[i - 1])
			ret += s[ r[i] - 1 ] - s[ r[i - 1] - 1 ];
		else
			ret += s[N] - s[r[i - 1] - 1] + s[ r[i] - 1];
	}

	return ret;
}

int main()
{
freopen("C-small-attempt0.in", "r", stdin);
	freopen("CSmallhaha.txt", "w", stdout);
	int T, i, j;
	scanf("%d", &T);
	for(int tt = 1; tt <= T; tt++)
	{
		scanf("%d%d%d", &R, &k, &N);
		memset(g, 0, sizeof(g));
		memset(s, 0, sizeof(s));
		memset(hash, -1, sizeof(hash));
		memset(r, 0, sizeof(r));

		for(i = 1; i <= N; i++)
		{
			scanf("%d", g + i);
			s[i] = s[i - 1] + g[i];
		}
		printf("Case #%d: %I64d\n", tt, Solve());
	}

	return 0;
}
