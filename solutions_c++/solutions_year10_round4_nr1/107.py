#include <cstdio>
#include <queue>

using namespace std;

int N;
int data[51][51];
int big[201][201];
int did[201][201];

int ok(int r, int c, int v)
{
	return !(0 <= r && r < N) || !(0 <= c && c < N) || data[r][c] == v;
}

int go2(int s, int d)
{
	int i, j;
	for (i = 0;i < N;i++)
	{
		for (j = 0;j < N;j++)
		{
			int sum = i + j;
			int diff = i - j;

			int nsum = 2 * s - sum;
			int ndiff = 2 * d - diff;

			int nsi = (nsum + diff) / 2;
			int nsj = (nsum - diff) / 2;

			if (!ok(nsi, nsj, data[i][j]))
				return false;

			int ndi = (sum + ndiff) / 2;
			int ndj = (sum - ndiff) / 2;

			if (!ok(ndi, ndj, data[i][j]))
				return false;
		}
	}
	return true;
}

int go()
{
	int s, d;
	int ret = 0x7FFFFFFF;

	for (s = 0;s <= 2 * (N - 1);s++)
	{
		for (d = -(N - 1);d <= (N - 1);d++)
		{
			if (go2(s, d))
			{
				// do something
				int cs = s - (N - 1);
				if (cs < 0) cs *= -1;
				int cd = d;
				if (cd < 0) cd *= -1;
				if (ret > cs + cd)
					ret = cs + cd;
			}
		}
	}
	return ret;
}

int main()
{
	int tc;
	scanf("%d", &tc);

	int ti;
	for (ti = 1;ti <= tc;ti++)
	{
		printf("Case #%d: ", ti);
		scanf("%d", &N);

		int i, j;
		int sum = 0;
		for (i = 0;i < N;i++, sum++)
		{
			for (j = 0;j <= i;j++)
			{
				int v;
				scanf("%d", &v);
				data[sum - j][j] = v;
			}
		}

		int off;
		for (i = N - 2, off = 1;i >= 0;i--, sum++, off++)
		{
			for (j = 0;j <= i;j++)
			{
				int v;
				scanf("%d", &v);
				data[sum - off - j][off + j] = v;
			}
		}

		int m = go() + N;
		printf("%d\n", m * m - N * N);
		fprintf(stderr, "Case #%d: %d\n", ti, m * m - N * N);
	}
	return 0;
}
