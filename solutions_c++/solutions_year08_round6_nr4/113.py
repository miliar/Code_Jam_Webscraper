#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
using namespace std;

int adjMatrix[9][9];
int small[9][9];
int mutated[9][9];

int cb(int v)
{
	int ret = 0;
	for (;v;v = v >> 1)
		ret += v & 1;
	return ret;
}

int main()
{
	int t, ti;
	scanf("%d", &t);
	for (ti = 1;ti <= t;ti++)
	{
		fprintf(stderr, "%d of %d ..\r", ti, t);


		printf("Case #%d: ", ti);

		memset(adjMatrix, 0, sizeof(adjMatrix));
		memset(small, 0, sizeof(small));

		int N;
		scanf("%d", &N);
		int i;
		for (i = 0;i < N - 1;i++)
		{
			int p, q;
			scanf("%d %d", &p, &q);
			p--;
			q--;
			adjMatrix[p][q] = adjMatrix[q][p] = true;
		}

		int M;
		scanf("%d", &M);
		for (i = 0;i < M - 1;i++)
		{
			int p, q;
			scanf("%d %d", &p, &q);
			p--;
			q--;
			small[p][q] = small[q][p] = true;
		}

		if (M == 1)
		{
			printf("YES\n");
			continue;
		}
		int h = false;
		int j, k;
		for (i = 0;i < (1 << N);i++)
		{
			memcpy(mutated, adjMatrix, sizeof(adjMatrix));
			if (N - cb(i) != M)
				continue;
			int c = 0;
			int idx[8] = {0, };
			for (j = 0;j < N;j++)
			{
				if (i & (1 << j))
				{
					int p, q;
					p = -1, q = -1;
					for (k = 0;k < N;k++)
					{
						if (mutated[j][k])
						{
							p = k;
							break;
						}
					}
					for (k++;k < N;k++)
					{
						if (mutated[j][k])
						{
							q = k;
							break;
						}
					}
					if (p == -1)
					{
						j = N + 2;
						break;
					}
					mutated[p][j] = mutated[j][p] = false;
					if (q != -1)
					{
						mutated[q][j] = mutated[j][q] = false;
						mutated[p][q] = mutated[q][p] = true;
					}
				}
				else
				{
					idx[c++] = j;
				}
			}

			if (j == N + 2)
				continue;

			int arr[8] = {0, 1, 2, 3, 4, 5, 6, 7};

			do
			{
				int other;
				int i, j;
				for (i = 0;i < M;i++)
				{
					for (j = 0;j < M;j++)
					{
						if (small[i][j] != mutated[idx[arr[i]]][idx[arr[j]]])
							break;
					}
					if (j != M)
						break;
				}
				if (i == M)
				{
					h = true;
					break;
				}
			} while(next_permutation(arr, arr + M));

			if (h)
				break;
		}
		printf("%s\n", h ? "YES" : "NO");
	}
}