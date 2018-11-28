#include <stdio.h>
#include <memory.h>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

vector<pair<int, int> > v[2];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int N;
	scanf("%d", &N);
	int NA, NB, P;
	for (int t = 0; t < N; t++)
	{
		scanf("%d%d%d", &P, &NA, &NB);
		v[0].clear();
		v[1].clear();
		for (int i = 0; i < NA; i++)
		{
			int fromH, fromM, toH, toM;
			scanf("%d:%d%d:%d", &fromH, &fromM, &toH, &toM);
			v[0].push_back(make_pair(fromH * 60 + fromM, toH * 60 + toM));
		}
		for (int i = 0; i < NB; i++)
		{
			int fromH, fromM, toH, toM;
			scanf("%d:%d%d:%d", &fromH, &fromM, &toH, &toM);
			v[1].push_back(make_pair(fromH * 60 + fromM, toH * 60 + toM));
		}
		sort(v[0].begin(), v[0].end());
		sort(v[1].begin(), v[1].end());
		int res[2];
		res[0] = 0;res[1] = 0;
		while (v[0].size() > 0 || v[1].size() > 0)
		{

			int from;
			int timeLeft = 1000000000;
			vector<pair<int, int> >::iterator itl;
			for (vector<pair<int, int> >::iterator it = v[0].begin(); it != v[0].end(); it++)
			{
				timeLeft = it->first;
				itl = it;
				break;
			}
			int timeRight = 1000000000;
			vector<pair<int, int> >::iterator itr;
			for (vector<pair<int, int> >::iterator it = v[1].begin(); it != v[1].end(); it++)
			{
				timeRight = it->first;
				itr = it;
				break;
			}
			int time;
			if (timeLeft < timeRight)
			{
				from = 1;
				time = itl->second;
				v[0].erase(itl);
			}
			else
			{
				from = 0;
				time = itr->second;
				v[1].erase(itr);
			}
			res[(from + 1) % 2]++;
			bool f = true;
			while (f)
			{
				f = false;
				vector<pair<int, int> >::iterator it;
				for (it = v[from].begin(); it != v[from].end(); it++)
					if (it->first >= time + P)
					{
						f = true;						
						time = it->second;						
						from = (from + 1) % 2;
						break;
					}
				if (f)
					v[(from + 1) % 2].erase(it);
			}
		}
		printf("Case #%d: %d %d\n", t + 1, res[0], res[1]);
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}