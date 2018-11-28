#include <iostream>
#include <map>
#include <sstream>
#include <cstdlib>
#include <string>
#include <set>
#include <vector>
#include <list>
#include <deque>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <bitset>
#include <ctime>

using namespace std;

#define _TEST_TIME
//#define pi_assert(condition, __VA_ARGS__) if (condition) fprintf(stderr, __VA_ARGS__);

#ifdef _TEST_TIME
clock_t start_time;
void print_time()
{
	fprintf(stderr, "Time used: %.4lf\n", double(clock() - start_time) / CLOCKS_PER_SEC);
}
#endif

int nCase, N, K;
int price[200][200], a[200][200], dy[200];
bool ny[200];

bool dfs(int k)
{
	for (int i = 0; i < N; ++i) if (!ny[i] && a[k][i])
	{
		ny[i] = true;
		if (dy[i] < 0 || dfs(dy[i]))
		{
			dy[i] = k;
			return true;
		}
	}
	return false;
}

void solve()
{
	cin >> nCase;
	for (int curCase = 0; curCase < nCase; ++curCase)
	{
		cin >> N >> K;
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < K; ++j)
			{
				cin >> price[i][j];
			}

		for (int i = 0; i < N; ++i)
			for (int j = 0; j < N; ++j)
			{
				a[i][j] = 1;
				for (int k = 0; k < K; ++k)
					if (price[i][k] >= price[j][k])
					{
						a[i][j] = 0;
						break;
					}
			}

		int answer = N;
		memset(dy, 255, sizeof(dy));
		for (int i = 0; i < N; ++i)
		{
			memset(ny, 0, sizeof(ny));
			if (dfs(i)) --answer;
		}

		printf("Case #%d: %d\n", curCase + 1, answer);
	}
}

int	main()
{
#ifdef _TEST_TIME
	start_time = clock();
#endif

	solve();

#ifdef _TEST_TIME
	print_time();
#endif
	return 0;
}
