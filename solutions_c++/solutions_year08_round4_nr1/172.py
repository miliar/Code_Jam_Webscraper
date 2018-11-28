#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int m, v;
int inNodeN;
vector<int> tree;
vector<int> changeable;

vector<int> zero, one;

int result;

void calc(int a)
{
	if (a >= (m - 1)/2)
	{
		if (tree[a] == 0)
		{
			zero[a] = 0;
		}
		else
		{
			one[a] = 0;
		}

		return;
	}

	int left = a*2 + 1;
	int right = a*2 + 2;

	calc(left);
	calc(right);

	if (tree[a] == 0) // OR
	{
		// ZERO
		int min = 99999;
		if (zero[left] != -1 && zero[right] != -1 && zero[left] + zero[right] < min)
		{
			min = zero[left] + zero[right];
		}
		
		if (changeable[a])
		{
			if (zero[left] != -1 && one[right] != -1 && zero[left] + one[right] + 1 < min)
			{
				min = zero[left] + one[right] + 1;
			}
			if (one[left] != -1 && zero[right] != -1 && one[left] + zero[right] + 1 < min)
			{
				min = one[left] + zero[right] + 1;
			}
			if (zero[left] != -1 && zero[right] != -1 && zero[left] + zero[right] + 1 < min)
			{
				min = zero[left] + zero[right] + 1;
			}

		}
		if (min != 99999)
		{
			zero[a] = min;
		}

		// ONE
		min = 99999;
		if (one[left] != -1 && zero[right] != -1 && one[left] + zero[right] < min)
		{
			min = one[left] + zero[right];
		}
		if (zero[left] != -1 && one[right] != -1 && zero[left] + one[right] < min)
		{
			min = zero[left] + one[right];
		}
		if (one[left] != -1 && one[right] != -1 && one[left] + one[right] < min)
		{
			min = one[left] + one[right];
		}

		if (changeable[a])
		{
			if (one[left] != -1 && one[right] != -1 && one[left] + one[right] + 1 < min)
			{
				min = one[left] + one[right] + 1;
			}
		}

		if (min != 99999)
		{
			one[a] = min;
		}
	}
	else // AND
	{
		// ZERO
		int min = 99999;
		
		if (zero[left] != -1 && one[right] != -1 && zero[left] + one[right] < min)
		{
			min = zero[left] + one[right];
		}
		if (one[left] != -1 && zero[right] != -1 && one[left] + zero[right] < min)
		{
			min = one[left] + zero[right];
		}
		if (zero[left] != -1 && zero[right] != -1 && zero[left] + zero[right] < min)
		{
			min = zero[left] + zero[right];
		}

		if (changeable[a])
		{
			if (zero[left] != -1 && zero[right] != -1 && zero[left] + zero[right] + 1 < min)
			{
				min = zero[left] + zero[right] + 1;
			}
		}
		if (min != 99999)
		{
			zero[a] = min;
		}

		// ONE
		min = 99999;

		if (one[left] != -1 && one[right] != -1 && one[left] + one[right] < min)
		{
			min = one[left] + one[right];
		}

		if (changeable[a])
		{
			if (one[left] != -1 && zero[right] != -1 && one[left] + zero[right] + 1 < min)
			{
				min = one[left] + zero[right] + 1;
			}
			if (zero[left] != -1 && one[right] != -1 && zero[left] + one[right] + 1 < min)
			{
				min = zero[left] + one[right] + 1;
			}
			if (one[left] != -1 && one[right] != -1 && one[left] + one[right] + 1 < min)
			{
				min = one[left] + one[right] + 1;
			}
		}

		if (min != 99999)
		{
			one[a] = min;
		}
	}
}

void solve(void)
{
	zero.clear();
	one.clear();

	for (int i = 0 ; i < m ; ++i)
	{
		zero.push_back(-1);
		one.push_back(-1);
	}

	calc(0);

	if (v == 0)
	{
		result = zero[0];
	}
	else
	{
		result = one[0];
	}
}

int main(void)
{
	int T;
	scanf("%d ", &T);

	for (int t = 1 ; t <= T ; ++t)
	{
		tree.clear();
		changeable.clear();
		result = 0;

		scanf("%d %d ", &m, &v);

		for (int i = 0 ; i < (m - 1)/2 ; ++i)
		{
			int a, b;

			scanf("%d %d ", &a, &b);
			tree.push_back(a);
			changeable.push_back(b);
		}
		for (int i = 0 ; i < (m + 1)/2 ; ++i)
		{
			int a;
			
			scanf("%d ", &a);
			tree.push_back(a);
			changeable.push_back(0);
		}

		solve();

		printf("Case #%d: ", t);
		if (result == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", result);
	}
}
