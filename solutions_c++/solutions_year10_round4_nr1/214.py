#include <stdio.h>

int n;
int data[51][51];

int main ()
{
	freopen ("A-large.in", "r", stdin);
	freopen ("A-large.out", "w", stdout);

	int t;
	int ct;

	scanf ("%d", &t);
	for (ct = 0; ct < t; ct ++)
	{
		scanf ("%d", &n);
		for (int i = 0; i < n + n - 1; i ++)
			for (int j = 0; j < n; j ++)
				if (i - j >= 0 && i - j < n)
					scanf ("%d", &(data[j][i - j]));
		
		int best = 1000000000;
		for (int i = -n; i < n + n + 1; i ++)
			for (int j = -n; j < n + n + 1; j ++)
			{
				int cur;

				// use as center
				{
					int x1,x2,y1,y2;

					x1 = 0; x2 = n - 1;
					y1 = 0; y2 = n - 1;
					if (i + i - 0 > x2) x2 = i + i - 0;
					if (i + i - (n - 1) < x1) x1 = i + i - (n - 1);
					if (j + j - 0 > y2) y2 = j + j - 0;
					if (j + j - (n - 1) < y1) y1 = j + j - (n - 1);

					cur = (x2 - x1 + 1) > (y2 - y1 + 1)? (x2 - x1 + 1) : (y2 - y1 + 1);
				}

				if (cur < best)
				{
					bool it_works = true;

					for (int x = 0; it_works && x < n; x ++)
						for (int y = 0; it_works && y < n; y ++)
						{
							int x2 = i + i - x;
							int y2 = j + j - y;
							int x3 = y - j + i;
							int y3 = x - i + j;
							int x4 = j - y + i;
							int y4 = i - x + j;

							if (x2 >= 0 && x2 < n && y2 >= 0 && y2 < n && data[x2][y2] != data[x][y])
								it_works = false;
							if (x3 >= 0 && x3 < n && y3 >= 0 && y3 < n && data[x3][y3] != data[x][y])
								it_works = false;
							if (x4 >= 0 && x4 < n && y4 >= 0 && y4 < n && data[x4][y4] != data[x][y])
								it_works = false;
						}

					if (it_works)
					{
						best = cur;
					}
				}
			}

		for (int i = -n; i < n + n + 1; i ++)
			for (int j = -n; j < n + n + 1; j ++)
			{
				int cur;

				{
					int x1,x2,y1,y2;

					x1 = 0; x2 = n - 1;
					y1 = 0; y2 = n - 1;
					if (i + i + 1 - 0 > x2) x2 = i + i + 1 - 0;
					if (i + i + 1 - (n - 1) < x1) x1 = i + i + 1 - (n - 1);
					if (j + j + 1 - 0 > y2) y2 = j + j + 1 - 0;
					if (j + j + 1 - (n - 1) < y1) y1 = j + j + 1 - (n - 1);

					cur = (x2 - x1 + 1) > (y2 - y1 + 1)? (x2 - x1 + 1) : (y2 - y1 + 1);
				}

				if (cur < best)
				{
					bool it_works = true;

					for (int x = 0; it_works && x < n; x ++)
						for (int y = 0; it_works && y < n; y ++)
						{
							int x2 = i + i + 1 - x;
							int y2 = j + j + 1 - y;
							int x3 = y - j + i;
							int y3 = x - i + j;
							int x4 = j - y + i + 1;
							int y4 = i - x + j + 1;

							if (x2 >= 0 && x2 < n && y2 >= 0 && y2 < n && data[x2][y2] != data[x][y])
								it_works = false;
							if (x3 >= 0 && x3 < n && y3 >= 0 && y3 < n && data[x3][y3] != data[x][y])
								it_works = false;
							if (x4 >= 0 && x4 < n && y4 >= 0 && y4 < n && data[x4][y4] != data[x][y])
								it_works = false;
						}

					if (it_works)
					{
						best = cur;
					}
				}
			}

		printf ("Case #%d: %d\n", ct + 1, best * best - n * n);
	}

	return 0;
}