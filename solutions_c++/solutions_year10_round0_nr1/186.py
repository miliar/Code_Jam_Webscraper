#include <stdio.h>
#include <assert.h>
#include <math.h>
#include <iostream>
#include <string>
#include <set>
#include <queue>
#include <vector>
#include <algorithm>
#include <map>
#include <stack>
#include <memory.h>
#include <time.h>

using namespace std;

bool solveSlow(int N, int K)
{

	vector<int> state(N);

	for (int i = 0; i < K; i++)
	{
		for (int j = 0; j < state.size(); j++)
		{
			bool power = state[j];

			state[j] ^= 1;

			if (!power)
				break;
		}
	}

	int j;
	for (j = 0; j < state.size(); j++)
		if (state[j] != 1)
			return false;

	return true;

}


int main(int argc, char* argv[])
{
	freopen("Test.in", "r", stdin);

	int caseCount;
	scanf("%d", &caseCount);


	for (int nCase = 1; nCase <= caseCount; nCase++)
	{
		int N, K;
		scanf("%d %d", &N, &K);

		//bool res = solveSlow(N, K);

		K &= (1 << N) - 1;

		printf("Case #%i: ", nCase);

		if (K == (1 << N) - 1)
		{
			//assert (res);
			printf("ON\n");
		}
		else
		{
			//assert (!res);
			printf("OFF\n");
		}

		fflush(stdout);
	}

	return 0;
}


