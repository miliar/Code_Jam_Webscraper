#include <vector>
#include <algorithm>

#include <cstdio>

using namespace std;

#define ITERATE(it, x) for(__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)

int findAxes(int k, const vector<vector<int> >& given)
{
	for (int axis = 0; axis < k; ++axis)
	{
		// axis == c - r
		// Test whether given[r][c] == given[c - axis][r + axis]
		bool found = true;
		for (int r = 0; r < k - axis; ++r)
		{
			for (int c = axis; c < k; ++c)
			{
				if (given[r][c] != given[c - axis][r + axis])
				{
					found = false;
					goto l_not_sim_2;
				}
			}
		}
		l_not_sim_2:
		if (found)
			return axis;
		found = true;
		if (axis > 0)
		{
			// axis == r - c
			// Test whether given[r][c] == given[c + axis][r - axis]
			for (int r = axis; r < k; ++r)
			{
				for (int c = 0; c < k - axis; ++c)
				{
					if (given[r][c] != given[c + axis][r - axis])
					{
						found = false;
						goto l_not_sim_1;
					}
				}
			}
			l_not_sim_1:
			if (found)
				return axis;
		}
	}
	return k;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int idxCase = 0; idxCase < T; ++idxCase)
	{
		int k;
		scanf("%d", &k);
		vector<vector<int> > given(k);
		ITERATE(it, given)
			it->assign(k, 0);
		for (int i = 0; i < k; ++i)
		{
			for (int j = 0; j <= i; ++j)
				scanf("%d", &given[j][k - 1 - i + j]);
		}
		for (int i = 0; i < k - 1; ++i)
		{
			for (int j = 0; j < k - 1 - i; ++j)
				scanf("%d", &given[i + 1 + j][j]);
		}
		int axis1 = findAxes(k, given);
		reverse(given.begin(), given.end());
		int axis2 = findAxes(k, given);
		int resultk = k + axis1 + axis2;
		int ans = resultk * resultk - k * k;
    	printf("Case #%d: %d\n", idxCase + 1, ans);
	}
	return 0;
}
