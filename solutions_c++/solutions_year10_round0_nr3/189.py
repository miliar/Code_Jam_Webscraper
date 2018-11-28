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

int main(int argc, char* argv[])
{
	freopen("Test.in", "r", stdin);

	int caseCount;
	scanf("%d", &caseCount);
 
	for (int nCase = 1; nCase <= caseCount; nCase++)
	{
		int R, k, N;
		scanf("%d %d %d", &R, &k, &N);

		vector<int> groups(N);

		for (int i = 0; i < N; i++)
		{
			scanf("%d", &groups[i]);
		}

		int first = 0;
		long long res = 0;
		bool jumbed = false;
		
		vector<long long> prev(N, -1);
		vector<int> prevI(N, -1);

		for (int i = 0; i < R; i++)
		{
			if (!jumbed)
			{
				if (prev[first] != -1)
				{
					long long cycle = i - prevI[first];
					long long cnt = ((R - i) / cycle) - 1;
					if (cnt < 0) cnt = 0;

					i += cnt * cycle;
					res += (res - prev[first]) * cnt;

					jumbed = true;
				}
			}

			prev[first] = res;
			prevI[first] = i;

			int cur = 0;
			int j = 0;
			for (j = 0; j < N; j++)
			{
				if (cur + groups[(first + j) % N] <= k)
				{
					cur += groups[(first + j) % N];
				}
				else
				{
					break;
				}
			}
			res += cur;
			first = (first + j) % N;
		}

		printf("Case #%d: %lld\n", nCase, res);		

		fflush(stdout);
	}

	return 0;
}


