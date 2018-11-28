#include <stdio.h>
#include <vector>
#include <algorithm>
#include <queue>

using std::vector;
using std::queue;

int main()
{
	unsigned int nCases = 0;scanf("%d",&nCases);
	for(unsigned int iCases = 1;iCases <= nCases;++iCases)
	{
		unsigned int n = 0;scanf("%d",&n);
		vector<unsigned int> vine_dis(n),vine_len(n);
		for(unsigned int i = 0;i < n;++i) scanf("%d%d",&vine_dis[i],&vine_len[i]);
		unsigned int goal = 0;scanf("%d",&goal);

		vector<unsigned int> lows(n,0);lows[0] = vine_dis[0];
		std::queue<unsigned int> updates;updates.push(0);
		for(;!updates.empty();)
		{
			unsigned int u = updates.front();updates.pop();

			int min_swinging_dis = vine_dis[u] - lows[u];
			int max_swinging_dis = vine_dis[u] + lows[u];
			if(min_swinging_dis < 0) min_swinging_dis = 0;
			unsigned int ibeg = std::lower_bound(vine_dis.begin(),vine_dis.end(),min_swinging_dis) - vine_dis.begin();
			unsigned int iend = std::upper_bound(vine_dis.begin(),vine_dis.end(),max_swinging_dis) - vine_dis.begin();

			for(unsigned int i = ibeg;i < iend;++i)
			{
				if(i == u) continue;
				int dis = vine_dis[i] - vine_dis[u];
				if(dis < 0) dis = 0 - dis;

				int len = 0;
				if(dis < vine_len[i]) len = dis;
				else len = vine_len[i];

				if(len <= lows[i]) continue;
				updates.push(i);
				lows[i] = len;
			}
		}
		bool ans = false;
		for(unsigned int i = 0;i < n && !ans;++i)
		{
			if(vine_dis[i] + lows[i] >= goal) ans = true;
		}
		printf("Case #%u: %s\n",iCases,(ans?"YES":"NO"));
	}
	return 0;
}