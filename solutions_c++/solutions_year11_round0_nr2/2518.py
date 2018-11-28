#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	for(int ca = 1; ca <= T; ca++)
	{
		int c, d, n;
		int ta[256];
		map<pair<char, char>, char> combo;
		set<char> opo[256];
		memset(ta, 0, sizeof(ta));
		vector<char> sol;

		scanf("%d", &c);
		for(int i = 0; i < c; i++)
		{
			char comb[4];
			scanf("%s", comb);
			combo[make_pair(min(comb[0], comb[1]),
				  max(comb[0],comb[1]))] = comb[2];
		}
		scanf("%d", &d);
		for(int i = 0; i < d; i++)
		{
			char opp[4];
			scanf("%s", opp);
			opo[opp[0]].insert(opp[1]);
			opo[opp[1]].insert(opp[0]);
		}
		scanf("%d", &n);
		char seq[128];
		scanf("%s", seq);
		for(int i = 0; seq[i]; i++)
		{
			char vai = seq[i];
			if(!sol.empty())
			{
				if(combo[make_pair(min(seq[i], sol[sol.size()-1]),
							max(seq[i], sol[sol.size()-1]))])
				{
					vai = combo[make_pair(min(seq[i], sol[sol.size()-1]),
							max(seq[i], sol[sol.size()-1]))];
					ta[sol[sol.size()-1]]--;
					sol.pop_back();
				}
				for(set<char>::iterator it = opo[vai].begin();
						it != opo[vai].end(); it++)
				{
					if(ta[*it])
					{
						vai = 0;
						memset(ta, 0, sizeof(ta));
						sol.clear();
						break;
					}
				}
			}
			if(vai) sol.push_back(vai);
			ta[vai]++;
		}
		printf("Case #%d: [", ca);
		for(int i = 0; i < sol.size(); i++)
			printf("%s%c", i?", ":"", sol[i]);
		printf("]\n");
	}
	return 0;
}
