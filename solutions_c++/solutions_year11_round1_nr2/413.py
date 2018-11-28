#include <stdio.h>
#include <string.h>
#include <vector>
#include <string>

using namespace std;

int app[128][128];
vector<string> dic;

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		int n, m;
		scanf("%d%d", &n, &m);
		dic.clear();
		memset(app, 0, sizeof(app));
		for(int i = 0; i < n; i++)
		{
			char ent[32];
			scanf("%s ", ent);
			dic.push_back(string(ent));
			for(int j = 0; ent[j]; j++)
				app[ent[j]-'a'][i] |= (1<<j);

		}
		printf("Case #%d:", t);
		for(int i = 0; i < m; i++)
		{
			string sol;
			int ma = -1;
			char perm[32];
			scanf("%s", perm);
			for(int j = 0; j < n; j++)
			{
				vector<int> pos;
				for(int k = 0; k < dic.size(); k++)
					if(dic[k].size() == dic[j].size())
						pos.push_back(k);
				int pt = 0;
				for(int k = 0; k < 26; k++)
				{
					int ok = 0;
					for(int l = 0; l < pos.size(); l++)
						if(app[perm[k]-'a'][pos[l]])
							ok = 1;
					if(ok && !app[perm[k]-'a'][j]) pt++;
					for(int l = 0; l < pos.size(); l++)
					{
						if(app[perm[k]-'a'][pos[l]] != app[perm[k]-'a'][j])
						{	pos.erase(pos.begin()+l); l--; }
					}
				}
				if(pt > ma) { ma = pt; sol = dic[j]; }
			}
			printf(" %s", sol.c_str());
		}
		printf("\n");
	}
	return 0;
}
