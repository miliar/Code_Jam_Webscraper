#include <stdio.h>
#include <math.h>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <set>
#include <map>
#include <deque>
#include <queue>
#include <algorithm>
#include <cassert>
#include <memory.h>

using namespace std;

#define pb push_back
#define mp make_pair
typedef long long lint;
const int INF = 2000000000;

int m, n;
int board[513][513];
int row[513], col[513];
bool use[513][513];

char tmp[500];

__forceinline int wtf(int x)
{
	if (x != 0)
		return 1;
	else
		return 0;
}

int ans[513];
bool solve(int case_num)
{
	scanf("%d%d", &m, &n);
	for (int i = 0; i < m; i++)
	{
		int k = 0;
		scanf("%s", tmp);
		for (int j = 0; j < n; j += 4, k++)
		{
			int v = 0;
			if (tmp[k] <= '9')
				v = tmp[k] - '0';
			else
				v = tmp[k] - 'A' + 10;
			board[i][j + 3] = wtf(v & 1);
			board[i][j + 2] = wtf(v & 2);
			board[i][j + 1] = wtf(v & 4);
			board[i][j + 0] = wtf(v & 8);
		}
	}

	memset(ans, 0, sizeof(ans));
	while (true)
	{
		int maxsz = -1, ll, tt;

		//memset(use, 0, sizeof(use));
		for (int i = 0; i < m; i++)
			for (int j = 0; j < n; j++)
				if (board[i][j] != 2)
				{
					int g = board[i][j];

					int k;
					for (k = 1; ; k++)
					{
						g = 1 - g;

						if (i + k == m || j + k == n)
							break;

						int q = g;

						bool ok = true;
						for (int s = 0; s <= k && ok; s++, q = 1 - q)
							ok = board[i + s][j + k] == q;
						q = g;
						for (int s = 0; s <= k && ok; s++, q = 1 - q)
							ok = board[i + k][j + s] == q;

						if (!ok)
							break;

						//if (ok)
						//{
							//for (int s = 0; s <= k; s++)
								//use[i + s][j + k] = true;
							//for (int s = 0; s <= k; s++)
								//use[i + k][j + s] = true;
						//}
						//else
							//break;
					}

					if (k != 1)
					{
						if (maxsz < k)
						{
							maxsz = k;
							tt = i;
							ll = j;
						}
						else if (maxsz == k)
						{
							if (i < tt)
							{
								tt = i;
								ll = j;
							}
							else if (i == tt)
							{
								ll = min(ll, j);
							}
						}
					}
				}

		if (maxsz != -1)
		{
			for (int i = 0; i < maxsz; i++)
				for (int j = 0; j < maxsz; j++)
					board[i + tt][j + ll] = 2;

			ans[maxsz]++;
		}
		else
			break;
	}

	int ansdiff = 0, anscc = 0;
	for (int i = 0; i < 513; i++)
		if (ans[i] > 0)
		{
			ansdiff++;
			anscc += (ans[i] * i * i);
		}


	anscc = n * m - anscc;
	if (anscc > 0)
	{
		ansdiff++;
		ans[1] = anscc;
	}

	printf("Case #%d: ", case_num);
	//answer
	printf("%d\n", ansdiff);
	for (int i = 512; i >= 0; i--)
		if (ans[i] > 0)
			printf("%d %d\n", i, ans[i]);
	//======
	//printf("\n");
	return true;
}

int main()
{
	freopen("input.txt", "r", stdin);
#ifndef _DEBUG
	freopen("output.txt", "w", stdout);
#endif
	int tn;
	scanf("%d", &tn);
	for (int i = 0; i < tn; i++)
		solve(i + 1);
	return 0;
}