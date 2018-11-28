#include <memory.h>
#include <algorithm>
#include <queue>
#include <cstdio>
#include <vector>
using namespace std;
#define all(x) x.begin(),x.end()
int Check[11111];
int main()
{
	int T;scanf("%d",&T);
	for (int kase=1;kase<=T;++kase)
	{
		int N;
		scanf("%d",&N);
		memset(Check,0,sizeof(Check));
		priority_queue<int> PQ[2];
		for (int q=0;q<N;++q)
		{
			int u; scanf("%d",&u);
			Check[u]++;
		}
		int ret = 987654321;
		for (int q=1;q<=10005;++q)
		{
			const int a = q&1;
			const int b = !a;
			while (!PQ[a].empty() && Check[q]>0)
			{
				PQ[b].push( PQ[a].top() - 1 ); PQ[a].pop();
				Check[q]--;
			}
			if (Check[q]>0) for (int w=0;w<Check[q];++w) PQ[b].push(-1);
			while (PQ[a].empty()==false)
			{
				ret = min(ret,-PQ[a].top());
				PQ[a].pop();
			}
		}
		if (ret ==987654321) ret =0;
		printf("Case #%d: %d\n",kase,ret);
	}

	return 0;
}
