#include <iostream>

using namespace std;

typedef long long int64;

int	now, task;

int	N, M, sx, sy, a, b, c, d;
int	hash[1000000 + 100];

inline bool checkN(int i)
{
	return i >= 0 && i < N;
}

inline bool checkM(int i)
{
	return i >= 0 && i < M;
}

inline bool check(int i, int j)
{
	return checkN(i) && checkM(j);
}

int	canGo(int sx, int sy, int a, int b)
{
	int ret = N + M;
	int toMin = 0;
	if (!checkN(sx))
	{
		if (a == 0) return 0;
		if (a > 0)
			if (sx > 0)
				toMin = N + M + 1;
			else
				toMin = max(toMin, (-sx - 1) / a + 1);
		else
			if (sx < 0)
				toMin = N + M + 1;
			else
				toMin = max(toMin, (sx - (N - 1) - 1) / (-a) + 1);
	}

	if (!checkM(sy))
	{
		if (b == 0) return 0;
		if (b > 0)
			if (sy > 0)
				toMin = N + M + 1;
			else
				toMin = max(toMin, (-sy - 1) / b + 1);
		else
			if (sy < 0)
				toMin = N + M + 1;
			else
				toMin = max(toMin, (sy - (M - 1) - 1) / (-b) + 1);
	}

	if (a == 0 && b == 0) ret = 0;
	if (a)
	{
		if (a > 0)
			ret = min(ret, (N - 1 - sx) / a);
		else
			ret = min(ret, sx / (-a));
	} 
	if (b)
	{
		if (b > 0)
			ret = min(ret, (M - 1 - sy) / b);
		else
			ret = min(ret, sy / (-b));
	}
	if (ret < toMin) return 0;
	return ret - toMin + 1;
}

int g[1000][1000];

int	DFS(int i, int j)
{
	if (!check(i, j)) return 0;
	if (g[i][j]) return 0;
	g[i][j] = 1;
//	cout << i << ' ' << j << endl;
	return 1 + DFS(i + a, j + b) + DFS(i + c, j + d);
}

int	main()
{
	scanf("%d", &task);

	memset(hash, 0, sizeof(hash));

	for (int now = 1; now <= task; ++now)
	{
		cin >> N >> M;
		cin >> a >> b >> c >> d;
		cin >> sx >> sy;

		memset(g, 0, sizeof(g));
		printf("Case #%d: ", now); cout << DFS(sx, sy) << endl;
		continue;
		int64 ret = 0;


		if (a == 0 && b == 0)
		{
			ret = canGo(sx, sy, c, d);
		}
		else 
		if (c == 0 && d == 0)
		{
			ret = canGo(sx, sy, a, b);
		}
		else
		if (a * d == c * b)
		{
			if (a == 0)
			{
				swap(a, b);
				swap(c, d);
				swap(N, M);
				swap(sx, sy);
			}

			while (check(sx, sy))
			{
				for (int i = sx, j = sy; check(i, j) && hash[i] < now; i += c, j += d)
				{
					++ret;
					hash[i] = now;
				}
				sx += a;
				sy += b;
			}
		} else
		{
			ret = 0;
			while (canGo(sx, sy, c, d))
			{
				printf("%d %d , %d %d : %d\n", sx, sy, c, d, canGo(sx, sy, c, d));
				ret += canGo(sx, sy, c, d);
				sx += a;
				sy += b;
			}
		}
	
		printf("Case #%d: ", now); cout << ret << endl;
	}
	return 0;
}
