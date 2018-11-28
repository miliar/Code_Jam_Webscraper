#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int K;
int len;
char str[60000];

char check[20];
int pArray[20];

int result;

void perm(int a)
{
	if (a == K)
	{
		char strAfter[60000];
		for (int i = 0 ; i < len ; i += K)
		{
			for (int j = 0 ; j < K ; ++j)
			{
				strAfter[i + j] = str[i + pArray[j]];
			}
		}

		char last = 0;
		int count = 0;
		for (int i = 0 ; i < len ; ++i)
		{
			if (strAfter[i] != last)
			{
				count++;
				last = strAfter[i];
			}
		}

		if (result == -1 || count < result)
			result = count;

		return;
	}

	for (int i = 0 ; i < K ; ++i)
	{
		if (check[i]) continue;

		pArray[a] = i;
		check[i] = 1;

		perm(a + 1);

		check[i] = 0;
	}
}

void solve(void)
{
	result = -1;

	memset(check, 0, K);

	perm(0);
}

int main(void)
{
	int T;
	scanf("%d ", &T);

	for (int t = 1 ; t <= T ; ++t)
	{
		scanf("%d ", &K);
		scanf("%s ", str);

		len = strlen(str);

		solve();

		printf("Case #%d: %d\n", t, result);
	}
}
