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
struct node
{
	int P, V;
};
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, N, D, count = 0;
	scanf("%d", &T);
	while (T--)
	{
		printf("Case #%d: ", ++count);
		scanf("%d %d", &N, &D);
		vector <node> num;
		vector <int> sum;
		int size = 0;
		__int64 mx = 0, base = 0;
		for (int i = 0; i < N; ++i)
		{
			node next;
			scanf("%d %d", &next.P, &next.V);
			num.push_back(next);
			if (sum.size() == 0)
			{
				sum.push_back(next.V);
			}
			else
			{
				sum.push_back(next.V + sum[sum.size() - 1]);
			}
		}
		for (int i = 0; i < N; ++i)
		{
			for (int j = i; j < N; ++j)
			{
				__int64 temp = D;

				temp = D;
				if (i - 1 >= 0)
				{
					temp *= sum[j] - sum[i - 1] - 1;
					if (temp > 0 && num[j].P - num[i].P < temp && temp - (num[j].P - num[i].P) > mx)
					{
						mx = temp - (num[j].P - num[i].P);
					}
				}
				else
				{
					temp *= sum[j] - 1;
					if (temp > 0 && num[j].P - num[i].P < temp && temp - (num[j].P - num[i].P) > mx)
					{
						mx = temp - (num[j].P - num[i].P);
					}
				}
			}
		}
		printf("%lf\n", mx / 2.0);
	}
	return 0;
}
