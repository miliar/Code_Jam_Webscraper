#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

typedef pair<int, int> T;
typedef pair<T, int> Sch;

Sch times[400];

int main()
{
	int n;
	cin >> n;
	for(int test = 1; test <= n; ++test)
	{
		int t, nn[2], how[2] = {0}, now[2] = {0}, num = 0;
		cin >> t >> nn[0] >> nn[1];
		for(int i = 0; i < 2; ++i)
		{
			for(int j = 0; j < nn[i]; ++j)
			{
				int s_h, s_m, e_h, e_m;
				char c;
				cin >> s_h >> c >> s_m >> e_h >> c >> e_m;
				times[num].first.first = s_h * 60 + s_m;
				times[num].first.second = 1;
				times[num].second = i;
				times[num + 1].first.first = e_h * 60 + e_m + t;
				times[num + 1].first.second = 0;
				times[num + 1].second = 1 - i;
				num += 2;
			}
		}
		sort(times, times + num);
		for(int i = 0; i < num; ++i)
		{
			if(times[i].first.second)
			{
				if(now[times[i].second] == 0)
				{
					++how[times[i].second];
					++now[times[i].second];
				}
				--now[times[i].second];
			}else
			{
				++now[times[i].second];
			}
		}
		printf("Case #%d: %d %d\n", test, how[0], how[1]);
	}
	return 0;
}
