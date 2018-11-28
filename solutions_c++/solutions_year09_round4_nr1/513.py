#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

int n;
vector<int> matrix;

int solve(void)
{
	int result = 0;

	for (int i = 0 ; i < n ; ++i)
	{
		for (int j = i ; j < n ; ++j)
		{
			if (matrix[j] <= i)
			{
				for (int k = j ; k > i ; --k)
				{
					swap(matrix[k], matrix[k - 1]);
					result++;
				}
				break;
			}
		}
		assert(matrix[i] <= i);
	}

	return result;
}

int main(void)
{
	int T;
	scanf("%d ", &T);

	for (int t = 1 ; t <= T ; ++t)
	{
		matrix.clear();

		scanf("%d ", &n);

		for (int i = 0 ; i < n ; ++i)
		{
			int value = 0;
			for (int j = 0 ; j < n ; ++j)
			{
				char a;
				scanf("%c ", &a);
				if (a == '1')
				{
					value = j;
				}
			}
			matrix.push_back(value);
		}

		printf("Case #%d: %d\n", t, solve());
	}
}
