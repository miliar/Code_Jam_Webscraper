#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <fstream>

using namespace std;

unsigned long long int solveBig (unsigned long long int R, unsigned long long int k, unsigned long long int N, unsigned long long int *g)
{
	int i;
 	unsigned long long int count = 0;
	for (i = 0; i < N; ++i) count += g[i];

	if (count <= k) return count * R;

	count = 0;

	int *nextIdx = (int*)malloc(sizeof(int) * N);
	unsigned long long int *total = (unsigned long long int*)malloc(sizeof(unsigned long long int) * N);

	int j;
	unsigned long long int gtotal = 0;

	for (i = 0, j = 0; i < 2 * N - 1 && j < N; ++i)
	{
		if (count + g[i % N] <= k)
		{
			count += g[i % N];
			//cout << "i = " << i << " count = " << count << endl;
		}
		else
		{
			//cout << "i = " << i << " total[" << j << "] = " << count << ", nextIdx[" << j << "] = " << (i % N) << endl;
			nextIdx[j] = i % N;
			total[j] = count;
			count -= g[j];
			++j;
			--i;
		}
	}
	assert(j == N);

	for (i = 0, j = 0; i < R; ++i)
	{
		gtotal += total[j];
		j = nextIdx[j];
	}
	free (total);
	free(nextIdx);

	return gtotal;
}

unsigned long long int solve (unsigned long long int R, unsigned long long int k, unsigned long long int N, unsigned long long int *g, unsigned long long int start)
{
	//cout << "solving for " << R << ", " << k << ", " << N << ", " << start << endl;

	if (R == 0) return 0;
	if (k == 0) return 0;
	if (N == 0) return 0;

	unsigned long long int count = 0, i;
	for (i = start; i < start + N; ++i)
	{
		if (count + g[i % N] <= k)
			count += g[i % N];
		else
			break;
	}

	return count + solve (R - 1, k, N, g, i % N);
}

int main()
{
	//cout << (sizeof(unsigned long long int) * 1000) << endl;
	ifstream input ("B-small.in", ios::in);
	unsigned long long int T = 0;
	if (input.is_open())
	{
		input >> T;
		for (unsigned long long int i = 0; i < T; ++i)
		{
			unsigned long long int R, k, N;
			input >> R;
			input >> k;
			input >> N;

			unsigned long long int g[N];
			for (unsigned long long int j = 0; j < N; ++j)
			{
				input >> g[j];
			}

			cout << "Case #" << (i+1) << ": " << solveBig (R, k, N, (unsigned long long int*)g) << endl;
			//cout << "Case #" << (i+1) << ": " << solve (R, k, N, (unsigned long long int*)g, 0) << endl;
		}
	}
	return 0;
}
