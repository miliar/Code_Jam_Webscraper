#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, tc = 0;
	scanf("%d", &T);
	int N;
	vector <int> num;
	while (T--)
	{
		printf("Case #%d: ", ++tc);
		scanf("%d", &N);
		num.resize(N);
		int mn = 1000000000, sm = 0;
		vector <int> bits(32, 0);
		for (int i = 0; i < N; ++i)
		{
			scanf("%d", &num[i]);
			sm += num[i];
			if (num[i] < mn)
			{
				mn = num[i];
			}
			for (int j = 0; j < 30; ++j)
			{
				bits[j] += (((1 << j) & num[i]) >> j);
			}
		}
		int isok = 1;
		for (int i = 0; i < 30; ++i)
		{
			if (bits[i] % 2 != 0)
			{
				isok = 0;
				break;
			}
		}
		if (isok == 0)
		{
			printf("NO\n");
		}
		else
		{
			printf("%d\n", sm - mn);
		}		
	}
	return 0;
}
