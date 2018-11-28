
	#include <cstdlib>
	#include <cstdio>
	#include <algorithm>
	#include <ctime>

	using namespace std;

	int n, w, l;
	int r[1005], ind[1005];
	int x[1005], y[1005];

	void swap(int &a, int &b)
	{
		a += b;
		b = a - b;
		a -= b;
	}

	void work()
	{
		scanf("%d%d%d", &n, &w, &l);
		for (int i = 0; i < n; i ++)
		{
			scanf("%d", &r[i]);
			ind[i] = i;
		}
		for (int i = 0; i < n; i ++)
			for (int j = i + 1; j < n; j ++)
				if (r[ind[i]] < r[ind[j]])
					swap(ind[i], ind[j]);
		x[ind[0]] = 0;
		y[ind[0]] = 0;
		int cury = 0;
		int newy = r[ind[0]];
		for (int i = 1; i < n; i ++)
		{
			//printf("%d\n", cury);
			if (x[ind[i - 1]] + r[ind[i]] + r[ind[i - 1]] <= w)
			{
				x[ind[i]] = x[ind[i - 1]] + r[ind[i]] + r[ind[i - 1]];
				y[ind[i]] = cury;
			}
			else
			{
				x[ind[i]] = 0;
				cury = newy + r[ind[i]];
				newy = cury + r[ind[i]];
				y[ind[i]] = cury;
			}
		}
		for (int i = 0; i < n; i ++)
			printf(" %d %d", x[i], y[i]);
		printf("\n");
	}

	int main()
	{
		srand(time(0));
		freopen("b.in", "r", stdin);
		freopen("b.out", "w", stdout);
		int t;
		scanf("%d", &t);
		for (int i = 1; i <= t; i ++)
		{
			printf("Case #%d:", i);
			work();
		}
		return 0;
	}
