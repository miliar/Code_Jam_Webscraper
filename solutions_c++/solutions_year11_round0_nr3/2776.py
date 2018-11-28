#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int T, N;
vector<int> pool;
int val[2];
int xor[2];

bool solver(int depth)
{
	if (depth == N)
		return xor[0] == xor[1] && val[0] >= val[1] && val[1] > 0;

	// takes turn
	for (int i = 0; i < 2; ++i)
	{
		// takes from the pool
		val[i] += pool[depth];
		xor[i] ^= pool[depth];
		if (solver(depth + 1))
			return true;

		// returns to the pool
		val[i] -= pool[depth];
		xor[i] ^= pool[depth];
	}

	return false;
}

int main()
{
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		pool.clear();

		cin >> N;
		for (int i = 0; i < N; ++i)
		{
			int c;
			cin >> c;
			pool.push_back(c);
		}
		sort(pool.begin(), pool.end(), greater<int>());

		val[0] = val[1] = 0;
		xor[0] = xor[1] = 0;

		cout << "Case #" << t << ": ";
		if (solver(0))
			cout << val[0];
		else
			cout << "NO";
		cout << endl;
	}

	return 0;
}
