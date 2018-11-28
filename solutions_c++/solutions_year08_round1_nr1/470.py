// GCJOnlineRound1_1.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>

using namespace std;

char buf[1000];

int main(int argc, char* argv[])
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	vector<int> dp(10, 0);
	dp[9] = 20;

	gets(buf);
	int g_T = atoi(buf);

	for (int i = 0; i < g_T; i++)
	{
		int sum = 0;
		int g_n;
		scanf("%d", &g_n);
		vector<int> arr1(g_n, 0);
		vector<int> arr2(g_n, 0);
		for (int j = 0; j < g_n; j++)
			scanf("%d", &arr1[j]);
		for (int j = 0; j < g_n; j++)
			scanf("%d", &arr2[j]);

		for (int j = 0; j < g_n; j++)
		{
			int minVal1 = j;
			int maxVal2 = j;
			for (int k = j; k < g_n; k++)
			{
				if (arr1[k] < arr1[minVal1])
					minVal1 = k;
				if (arr2[k] > arr2[maxVal2])
					maxVal2 = k;
			}
			sum += (arr1[minVal1] * arr2[maxVal2]);

			int tmp = arr1[j];
			arr1[j] = arr1[minVal1];
			arr1[minVal1] = tmp;

			tmp = arr2[j];
			arr2[j] = arr2[maxVal2];
			arr2[maxVal2] = tmp;
		}
		printf("Case #%d: %d\r\n", i+1, sum);
	}

	return 0;
}

