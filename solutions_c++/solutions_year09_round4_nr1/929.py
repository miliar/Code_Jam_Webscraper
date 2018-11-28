#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>

using namespace std;

int main()
{
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		int N;
		scanf("%d", &N);
		char s[100];
		int res = 0;
		int mas[100];
		for (int i = 0; i < N; i++)
		{
			scanf("%s", s);
			int mx = 0;
			for (int j = 0; s[j]; j++)
				if (s[j] == '1')
					mx = j + 1;
			mas[i] = mx;
		}
		bool use[100];
		memset(use, 0, sizeof(bool) * 100);
		for (int i = 0; i < N; i++)
		{
			int cnt = 0;
			for (int j = 0; j < N; j++)
				if (!use[j])
				{
					if (mas[j] - 1 <= i)
					{
						use[j] = true;
						res += cnt;
						break;
					}
					cnt++;
				}
		}
		printf("Case #%d: %d\n", t+1, res);
	}
	fclose(stdout);

	return 0;
}