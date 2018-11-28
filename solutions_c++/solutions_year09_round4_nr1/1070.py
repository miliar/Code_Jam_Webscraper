#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#include <memory>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <iostream>

using namespace std;

#define task "a"

typedef long long ll;
typedef long double ld;

#define MAXN 50

int T, N;

char a[MAXN][MAXN];

int rows[MAXN];

/*int bubble_sort()
{
	int res = 0;
	for (int i = N - 1; i >= 0; i--)
	{
		int mi = -1;
		for (int j = 0; j < N; j++)
			if (rows[j] > j && (mi == -1 || rows[j] <= rows[mi]))
				mi = j;
		
		while (mi != -1 && mi < N && rows[mi] > mi)
			swap(rows[mi], rows[mi + 1]), mi++, res++;  
	}
	return res;
}*/

int bubble_sort()
{
	int res = 0;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N - 1; j++)
			if (rows[j] > rows[j + 1])
				res++, swap(rows[j], rows[j + 1]);
	return res;
}                               

int main()
{
	freopen(task ".in", "rt", stdin);
	freopen(task ".out", "wt", stdout);
	scanf("%d", &T);

	for (int t = 1; t <= T; t++)
	{
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
		{
			scanf("\n");
			for (int j = 0; j < N; j++)
				scanf("%c", &a[i][j]);
		}		

		memset(rows, 0, sizeof(rows));

		for (int i = 0; i < N; i++)
			for (int j = N - 1; j >= 0; j--)
				if (a[i][j] == '1')
				{
					rows[i] = j;
					break;
				}

		bool used[MAXN];
		memset(used, 0 ,sizeof(used));
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j++)
				if (!used[j] && rows[j] <= i)
				{
					rows[j] = i;
					used[j] = true;
					break;
				}
		}

		printf("Case #%d: %d\n", t, bubble_sort());					
	}
	           
	return 0;
}
