#include <iostream>
#include <vector>

using namespace std;

const int oo = 1000;
int stock[32][32];
int comp[32][32];
int mem[1 << 16];
int covered[1 << 16];
vector<int> poss;
int n, k;

bool valid(int x)
{
	for (int i = 0; i < n; i++)
		if (x & (1 << i))
			for (int j = i+1; j < n; j++)
				if (x & (1 << j))
					if (!comp[i][j])
						return false;
	return true;
}

void cover(int x)
{
	if (covered[x])
		return;
	covered[x] = 1;
	for (int i = 0; i < n; i++)
		if (x & (1 << i))
			cover(x ^ (1 << i));
}

int solve(int x)
{
	if (x == 0)
		return 0;
	if (mem[x] != -1)
		return mem[x];
	mem[x] = oo;
	for (vector<int>::const_iterator it = poss.begin(); it != poss.end(); ++it)
		if ((*it & x) != x)
			mem[x] = min(mem[x], solve(*it & x)+1);
	return mem[x];
}

int main()
{
	int kases;
	cin >> kases;
	for (int kase = 1; kase <= kases; kase++)
	{
		cin >> n >> k;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < k; j++)
				cin >> stock[i][j];
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
			{
				comp[i][j] = 1;
				for (int l = 0; l < k; l++)
					if (stock[i][l] == stock[j][l] ||
							(stock[i][l] < stock[j][l]) != (stock[i][0] < stock[j][0]))
					{
						comp[i][j] = 0;
						break;
					}
			}

		for (int i = 0; i < (1 << n); i++)
		{
			covered[i] = 0;
			mem[i] = -1;
		}
		poss.clear();
		for (int m = (1 << n) - 1; m > 0; m--)
		{
			if (covered[m] || !valid(m))
				continue;
			poss.push_back(((1 << n) - 1) ^ m);
			cover(m);
		}

		printf("Case #%d: %d\n", kase, solve( (1 << n) - 1 ));
	}
	return 0;
}
