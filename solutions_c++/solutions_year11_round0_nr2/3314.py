#include <iostream>
#include <cmath>
#include <algorithm>
#include <map>
#include <string>
#include <vector>
#include <queue>

using namespace std;

int main()
{
	freopen("test.in", "rt", stdin);
	freopen("test.out", "wt", stdout);
	int t;
	scanf("%d ", &t);
	for (int i = 0; i < t; i++)
	{
		map < char, vector < pair< char, char > > > mp_cm;
		map < char, vector < char>  > mp_op;
		int c,d,n;
		scanf("%d ", &c);
		char buf[5] = {0};
		for (int j = 0; j < c; j++)
		{
			scanf("%s ", &buf);
			mp_cm[buf[0]].push_back(make_pair(buf[1], buf[2]));
			mp_cm[buf[1]].push_back(make_pair(buf[0], buf[2]));
		}
		scanf("%d ", &d);
		for (int j = 0; j < d; j++)
		{
			scanf("%s ", &buf);
			mp_op[buf[0]].push_back(buf[1]);
			mp_op[buf[1]].push_back(buf[0]);
		}
		vector <char> inn;
		scanf("%d ", &n);
		char en = 0;
		int beg = 0;
		//int cur = 0;
		for (int j = 0; j < n; j++)
		{
			scanf("%c", &en);
			bool f = false;
			map < char, vector < pair< char, char > > > ::iterator iter = mp_cm.find(en);
			map < char, vector < char > > ::iterator iter2 = mp_op.find(en);
			if (iter != mp_cm.end() && !inn.empty())
			{
				char cur = inn.back();
				for (int g = 0; g < iter->second.size(); g++)
				{
					if (iter->second[g].first == cur)
					{
						inn.pop_back();
						inn.push_back(iter->second[g].second);
						f = true;
						break;
					}
				}
			}
			if (!f)
			{
				if (iter2 != mp_op.end() && !inn.empty())
				{
					int cur = inn.size();
					for (int h = 0; h < cur; h++)
					{
					for (int g = 0; g < iter2->second.size(); g++)
					{
						if (iter2->second[g] == inn[h])
						{
							inn.clear();
							f = true;
							break;
						}
					}
					if (f)
						break;
					}
				}
			}
			if (!f)
				inn.push_back(en);
		}
		printf("Case #%d: [", i + 1);
		if (!inn.empty()){
		int ss = inn.size();
		for (int g = beg; g < ss - 1; g++)
		{
			printf("%c, ", inn[g]);
		}
		printf("%c", inn[ss - 1]);}
		printf("]\n");
	}
	
	return 0;
}