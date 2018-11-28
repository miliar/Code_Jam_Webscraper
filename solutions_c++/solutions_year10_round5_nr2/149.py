#include <vector>
#include <algorithm>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstring>

using namespace std;

int table[10001];

int main()
{
	int T;
	cin >> T;
	long long L;
	int N;
	for (int qn = 1; qn <= T; ++qn)
	{
		printf("Case #%d: ", qn);
		cin >> L >> N;
		vector<int> a(N);
		memset(table, -1, sizeof(table));
		table[0] = 0;

		for (int i = 0; i < N; ++i)
			scanf("%d", &a[i]);

		sort(a.rbegin(), a.rend());

		for (int i = 1; i <= 10000; ++i)
		{
			table[i] = 99999999;
			for (int j = 0; j < N; ++j)
			{
				if (i >= a[j] && table[i - a[j]] != -1)
				{
					if (table[i] > table[i - a[j]] + 1)
						table[i] = table[i - a[j]] + 1;
				}
			}
			if (table[i] == 99999999) table[i] = -1;
		}

		long long X = (L - 10000) / a[0] + 1;
		if (table[L - X * a[0]] == -1)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			cout << table[L - X * a[0]] + X << endl;
		}
	}
}

