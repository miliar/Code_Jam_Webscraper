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

void solve()
{
	int nCase, N;
	string line;
	int x[100];

	cin >> nCase;
	for (int nowCase = 0; nowCase < nCase; ++nowCase)
	{
		cin >> N;
		int i;
		for (i = 0; i < N; ++i) 
		{
			cin >> line;
			x[i] = N - 1;
			while (x[i] >= 0 && (line[x[i]] == '0')) --x[i];
		}

		int cnt = 0;

		for (i = 0; i < N; ++i)
			if (x[i] > i)
			{
				for (int j = i + 1; j < N; ++j) if (x[j] <= i)
				{
					for (int k = j - 1; k >= i; --k) swap(x[k], x[k + 1]);
					cnt += (j - i);
					break;
				}
			}
		printf("Case #%d: %d\n", nowCase + 1, cnt);
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
