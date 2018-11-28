#include <iostream>
#include <cmath>
#include <deque>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <bitset>

using namespace std;

typedef long long int64;

const int	modes = 10007;

int		rest[modes], rev[modes], f[100], cnt[1 << 14];
int		H, W, R, x[100], y[100], idx[100];

bool	compare(int i, int j)
{
	return (x[i] < x[j] || x[i] == x[j] && y[i] < y[j]);
}

int	two(int i)
{
	return 1 << i;
}

bool	isPrepared = 0;

void	prepare()
{
	if (isPrepared) return;
	isPrepared = 1;

	for (int i = 1; i < modes; ++i) for (int j = 1; j < modes; ++j) if (i * j % modes == 1) rev[i] = j;
	rest[0] = 1;
	for (int i = 1; i < modes; ++i) rest[i] = (int64) rest[i - 1] * i % modes;
}

int	get(int p)
{
	int ret = 0;
	while (p)
	{
		p /= modes;
		ret += p;
	}
	return ret;
}

int	getP(int k, int p)
{
	if (!p) return 1;
	int ret = getP(k, p / 2);
	ret = (int64) ret * ret % modes;
	if (p & 1) ret = (int64) ret * k % modes;
	return ret;
}

int	compute(int i, int j)
{
	prepare();
	if (i < 0 || j < 0) return 0;
	if ((i + j) % 3 > 0 || 2 * i < j || 2 * j < i) return 0;
	int p = (i + j) / 3, q = (2 * i - j) / 3;
	
	int t = get(p) - get(q) - get(p - q);
	if (t) return 0;

	int ret = (int64) getP(rest[modes - 1], p / modes) * rest[p % modes] % modes;
	int di1 = (int64) getP(rest[modes - 1], q / modes) * rest[q % modes] % modes;
	q = p - q;
	int di2 = (int64) getP(rest[modes - 1], q / modes) * rest[q % modes] % modes;
	ret = (int64) ret * rev[di1] % modes;
	ret = (int64) ret * rev[di2] % modes;
	return ret;
}

int	main()
{
	int nCase;
	scanf("%d", &nCase);

	cnt[0] = 0;
	for (int i = 1; i < two(12); ++i) cnt[i] = cnt[i / 2] + (i & 1);
	for (int nowCase = 1; nowCase <= nCase; ++nowCase)
	{
		scanf("%d%d%d", &H, &W, &R);
		for (int i = 0; i < R; ++i) scanf("%d%d", &x[i], &y[i]), --x[i], --y[i];
		x[R] = H - 1; y[R] = W - 1; 
		R += 1;

		for (int i = 0; i < R; ++i) idx[i] = i;
		sort(idx, idx + R, compare);

		int64 answer = 0;
		for (int s = 2 * two(R - 1) - 1; s >= two(R - 1); --s)
		{
			int u = 0, v = 0;
			int64 c = 1;
			for (int j = 0; c >= 0 && j <= R - 1; ++j) if (two(j) & s)
			{
				int dx = x[idx[j]] - u, dy = y[idx[j]] - v;
				c = c * compute(dx, dy) % modes;
				u = x[idx[j]]; v = y[idx[j]];
			}

			if (cnt[s] & 1)
			{
				answer = (answer + c) % modes;
			}
			else
			{
				answer = (answer + modes - c) % modes;
			}
		}

		printf("Case #%d: %d\n", nowCase, (int)(answer + modes) % modes);
	}
	return 0;
}
