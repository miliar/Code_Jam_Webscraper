#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cmath>
#include <string>
#include <climits>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;

long double PI;
typedef pair<int, int> pii;

int main(void)
{
	PI = acos(-1.0L);
	int number_of_tests;
	scanf("%d", &number_of_tests);
	for (int test_no = 1; test_no <= number_of_tests; test_no++)
	{
		int N;
		int res = INT_MAX;
		scanf("%d", &N);
		map<string, vector<pii> > colors;
		for (int i = 0; i < N; i++)
		{
			 char color_str[1000];
			 int a, b;
			 scanf("%s%d%d", color_str, &a, &b);
			 colors[color_str].push_back(pii(a-1, b));
			 sort(colors[color_str].begin(), colors[color_str].end());
		}
		map<string, vector<pii> >::iterator it1, it2, it3;
		for (it1 = colors.begin(); it1 != colors.end(); it1++)
		{
			for (it2 = colors.begin(); it2 != colors.end(); it2++)
			{
				for (it3 = colors.begin(); it3 != colors.end(); it3++)
				{
					int cur = 0;
					int cur1=0, cur2=0, cur3=0;
					int curres = 0;
					while (cur != 10000)
					{
						int curmax = cur;
						while ((cur1 < (int)it1->second.size()) && (it1->second[cur1].first <= cur))
						{
							curmax = max(curmax, it1->second[cur1].second);
							cur1 ++;
						}
						while ((cur2 < (int)it2->second.size()) && (it2->second[cur2].first <= cur))
						{
							curmax = max(curmax, it2->second[cur2].second);
							cur2 ++;
						}
						while ((cur3 < (int)it3->second.size()) && (it3->second[cur3].first <= cur))
						{
							curmax = max(curmax, it3->second[cur3].second);
							cur3 ++;
						}
						if (curmax == cur)
						{
							curres = INT_MAX;
							break;
						} else
						{
							curres ++;
							cur = curmax;
						}
					}
					res = min(res, curres);
				}
			}
		}
		printf("Case #%d: ", test_no);
		if (res == INT_MAX)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", res);
	}
	return 0;
}
