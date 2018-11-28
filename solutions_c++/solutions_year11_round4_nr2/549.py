#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

typedef long long int64;

char v[512][512];
int s[512][512];
int su[512][512], tu[512][512];
int sd[512][512], td[512][512];
int sl[512][512], tl[512][512];
int sr[512][512], tr[512][512];

int getS(int s[512][512], int x0, int y0, int x1, int y1)
{
	return s[x1][y1] - s[x0 - 1][y1] - s[x1][y0 - 1] + s[x0 - 1][y0 - 1];
}

bool check(int x0, int y0, int sz, int R, int C)
{

	int x1 = x0 + sz - 1, y1 = y0 + sz - 1;

	int x = getS(su, x0, y0, x0 + sz / 2 - 1, y1);
	int SU = -(sz - 1) * (v[x0][y0] + v[x0][y1]) + getS(su, x0, y0, x0 + sz / 2 - 1, y1) - ((sz%2==0)+2 * (R - (x0 + sz / 2 - 1) + 1 - 1)) * getS(s, x0, y0, x0 + sz / 2 - 1, y1);
	int SD = -(sz - 1) * (v[x1][y1] + v[x1][y0]) + getS(sd, x1 - sz / 2 + 1, y0, x1, y1) - ((sz%2==0)+2 * (x1 - sz / 2 + 1 - 1)) * getS(s, x1 - sz / 2 + 1, y0, x1, y1) ;

	int SL = -(sz - 1) * (v[x0][y0] + v[x1][y0]) + getS(sl, x0, y0, x1, y0 + sz / 2 - 1) - ((sz%2==0)+2 * (C - (y0 + sz / 2 - 1)) + 1 - 1) * getS(s, x0, y0, x1, y0 + sz / 2 - 1);
	int SR = -(sz - 1) * (v[x1][y1] + v[x0][y1]) + getS(sr, x0, y1 - sz / 2 + 1, x1, y1) - ((sz%2==0)+2 * (y1 - sz / 2 + 1 - 1)) * getS(s, x0, y1 - sz / 2 + 1, x1, y1);

	//if (sz == 4)
	//{
	//	printf("%d %d (su %d, sd %d, sl %d, sr %d)\n", x0, y0, SU, SD, SL, SR);
	//}
	if (SU != SD) return false;
	if (SL != SR) return false;

	return true;
}

int main()
{
	freopen("f:\\B-small-attempt1.in", "r", stdin);
	freopen("f:\\B-small-attempt1.out", "w", stdout);

	int T, R, C, D;
	scanf("%d", &T);
	for (int t_case = 1; t_case <= T; t_case++)
	{
		scanf("%d %d %d", &R, &C, &D);
		for (int i = 1; i <= R; i++)
		{
			scanf("%s", v[i] + 1);
			for (int j = 1; j <= C; j++)
			{
				v[i][j] -= '0';
				s[i][j] = v[i][j] +				   s[i - 1][j] +  s[i][j - 1] - s[i - 1][j - 1];
				v[i][j] *= 2;
				su[i][j] = (R - i + 1) * v[i][j] + su[i - 1][j] + su[i][j - 1] - su[i - 1][j - 1];
				sd[i][j] = i * v[i][j] +		   sd[i - 1][j] + sd[i][j - 1] - sd[i - 1][j - 1];
				sl[i][j] = (C - j + 1) * v[i][j] + sl[i - 1][j] + sl[i][j - 1] - sl[i - 1][j - 1];
				sr[i][j] = j * v[i][j] +	       sr[i - 1][j] + sr[i][j - 1] - sr[i - 1][j - 1];
				v[i][j] /= 2;
			}
		}

		int res = 0;

		for (int sz = min(R, C); sz >= 3; sz--)
		{
			for (int x0 = 1; x0 + sz - 1 <= R; x0++)
			{
				for (int y0 = 1; y0 + sz - 1 <= C; y0++)
				{
					if (check(x0, y0, sz, R, C))
					{
						res = sz;
						goto next;
					}
				}
			}
		}

		next:;
		if (res >= 3)
			printf("Case #%d: %d\n", t_case, res);
		else
			printf("Case #%d: IMPOSSIBLE\n", t_case);
	}
	return 0;
}
