#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
typedef long long INT;

int T,K,R,N,ti[1000];
INT g[1000],use[1000];

int main()
{
	int i,j;
	//freopen("C-large.in","r",stdin);
	//freopen("input","r",stdin);
	//freopen("C.out","w",stdout);
	scanf("%d",&T);
	for(int Case = 1;Case <= T;Case++)
	{
		scanf("%d%d%d",&R,&K,&N);
		for(i = 0;i < N;i++)
			scanf("%lld",&g[i]);
		memset(use,-1,sizeof(use));
		memset(ti,-1,sizeof(ti));
		int idx = 0,depth = 0;
		INT tot = 0;
		while(true)
		{
			INT t = g[idx];
			int tidx = idx;
			for(idx = (idx + 1)%N;idx != tidx;idx = (idx + 1)%N)
			{
				t += g[idx];
				if(t > K)
					break;
			}
			if(t > K)
				t -= g[idx];
			tot += t,depth++;
			if(use[idx] != -1)
				break;
			use[idx] = tot;
			ti[idx] = depth;
		}
		printf("Case #%d: ",Case);
		if(R < depth)
		{
			for(i = 0;i < N;i++)
			{
				if(ti[i] == R)
				{
					printf("%lld\n",use[i]);
					break;
				}
			}
		}
		else
		{
			INT ans = use[idx] + (INT)(R - ti[idx])/(INT)(depth - ti[idx])*(tot - use[idx]);
			for(i = 0;i < N;i++)
			{
				if(ti[i] - ti[idx] == (R - ti[idx])%(depth - ti[idx]))
				{
					ans += use[i] - use[idx];
					break;
				}
			}
			printf("%lld\n",ans);
		}
	}
	return 0;
}


