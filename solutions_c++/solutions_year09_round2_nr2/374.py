#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

char N[50];
char K[50];
int lN;

bool getNext(int a)
{
	if (lN == a)
	{
		return false;
	}

	K[a] = N[a];

	if (!getNext(a + 1))
	{
		int minPos = -1;

		for (int i = a + 1 ; i < lN ; ++i)
		{
			if (N[a] < N[i] && (minPos == -1 || N[i] < N[minPos]))
			{
				minPos = i;
			}
		}

		if (minPos == -1)
		{
			return false;
		}

		swap(K[a], K[minPos]);
		sort(K + a + 1, K + lN);
	}

	return true;
}

void solve(void)
{
	lN = strlen(N);
	memset(K, 0, 50);

	if (!getNext(0))
	{
		int minPos = -1;

		for (int i = 0 ; i < lN ; ++i)
		{
			if (N[i] != '0' && (minPos == -1 || N[i] < N[minPos]))
			{
				minPos = i;
			}
		}

		swap(K[0], K[minPos]);
		K[lN] = '0';
		sort(K + 1, K + lN + 1);
	}
}

int main(void)
{
	int T;

	scanf("%d ", &T);

	for (int t = 1 ; t <= T ; ++t)
	{
		scanf("%s ", N);

		solve();

		printf("Case #%d: %s\n", t, K);
	}
}
