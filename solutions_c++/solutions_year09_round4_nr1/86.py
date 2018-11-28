#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	char tmp[100];

	for (int cn = 1; cn <= T; ++cn)
	{
		printf("Case #%d: ", cn);

		int N;
		scanf("%d", &N);
		vector<int> a;

		for (int i = 0; i < N; ++i)
		{
			scanf("%s", tmp);
			int last = 0;
			for (int j = N - 1; j >= 0; --j)
			{
				if (tmp[j] == '1') { last = j; break; }
			}
			a.push_back(last);
		}

		int ret = 0;
		for (int i = 0; i < N; ++i)
		{
			for (int j = i; j < N; ++j)
			{
				if (a[j] <= i)
				{
					for (int k = j - 1; k >= i; --k)
					{
						swap(a[k], a[k + 1]);
						ret++;
					}
					break;
				}
			}
		}
		printf("%d\n", ret);
	}
}

