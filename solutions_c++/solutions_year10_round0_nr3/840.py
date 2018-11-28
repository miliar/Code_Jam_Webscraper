#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <cstdio>
#include <vector>
#include <iostream>
using namespace std;
typedef long long Long;
#define MAX 1024

Long dp[MAX][2];
int groups[MAX];

int main()
{
	int T;
	freopen("A-small.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	scanf("%d", &T);
	for (int k = 1 ; k <= T ; ++k)
	{
		Long result = 0;
		int R, K, N;
		scanf("%d%d%d", &R, &K, &N);
		
		for (int i = 0 ; i < N ; ++i)
		{
			scanf("%d", &groups[i]);
		}

		for (int i = 0 ; i < N ; ++i)
		{
			Long total = 0;
			int j;
			for (j = 0 ; j < N ; ++j)
			{
				int t = (i + j) % N;
				if (total + groups[t] > K)
				{
					break;
				}
				total += groups[t];
			}
			dp[i][0] = total;
			dp[i][1] = (i + j) % N;
		}

		int pos = 0;
		
		for (int i = 0 ; i < R ; ++i)
		{
			result += dp[pos][0];
			pos = dp[pos][1];
		}

		cout << "Case #" << k << ": " << result << endl;
	}

	return 0;
}
