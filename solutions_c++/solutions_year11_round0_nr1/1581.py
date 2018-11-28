#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <string.h>

using namespace std;

const int MAX = 105;

vector<pair<int, int> > all;
vector<int> one, two;

int go()
{
	int res = 0;
	int pos_i = 1, pos_j = 1;
	int cmd_i = 0, cmd_j = 0;

	for(int i = 0; i < all.size(); i++)
	{
		if(all[i].first == 0)
		{
			//两个人并行最优执行
			int t = abs(pos_i - all[i].second) + 1; 
			pos_i = all[i].second;
			res += t;

			if(cmd_j < two.size())
			{
				int step = abs(pos_j - two[cmd_j]);
				if(step <= t)  pos_j = two[cmd_j];
				else  
				{
					if(pos_j < two[cmd_j])  pos_j += t;
					else  pos_j -= t;
				}
			}

			cmd_i++;
		}
		else
		{
			int t = abs(pos_j - all[i].second) + 1;
			pos_j = all[i].second;
			res += t;

			if(cmd_i < one.size())
			{
				int step = abs(pos_i - one[cmd_i]);
				if(step <= t)  pos_i = one[cmd_i];
				else
				{
					if(pos_i < one[cmd_i])  pos_i += t;
					else  pos_i -= t;
				}
			}

			cmd_j++;
		}
	}

	return res;
}

int main()
{
	freopen("f:\\A-large.in", "r", stdin);
	freopen("f:\\A-large.out", "w", stdout);

	int T, c = 0;
	scanf("%d", &T);
	while(T--)
	{
		int N;
		scanf("%d", &N);

		all.clear();
		one.clear();
		two.clear();

		for(int i = 0; i < N; i++)
		{
			char cmd[2];
			int b;

			scanf("%s%d", cmd, &b);
			if(cmd[0] == 'O')  
			{
				all.push_back(make_pair(0, b));
				one.push_back(b);
			}
			else 
			{
				all.push_back(make_pair(1, b));
				two.push_back(b);
			}
		}

		printf("Case #%d: %d\n", ++c, go());
	}
}
