#include <stdio.h>
#include <vector>

using std::vector;

int main()
{
	int nCases = 0;scanf("%d",&nCases);
	for(int iCases = 1;iCases <= nCases;++iCases)
	{
		int l = 0,n = 0,c = 0;__int64 t = 0;
		scanf("%d%I64d%d%d",&l,&t,&n,&c);
		vector<int> dis(c);
		for(int i = 0;i < c;++i) scanf("%d",&dis[i]);
		vector<__int64> basetimes(n+1,0);
		for(int i = 1;i <= n;++i)  basetimes[i] = basetimes[i-1]+dis[(i-1)%c]*2;

		__int64 ret = basetimes[n];
		//printf("ret = %I64u\n",ret);
		if(t < ret)
		{
			if(1 <= l)
			{
				for(int i = 0;i < n;++i)
				{
					if(t >= basetimes[i+1]) continue;
					__int64 remain = 0;
					if(t > basetimes[i]) remain = t-basetimes[i];

					int tomove = dis[i%c];
					__int64 s = basetimes[n]-tomove*2;
					s += remain + tomove-remain/2;

					if(s < ret) ret = s;
					//printf("ret = %I64u\n",ret);
				}
			}
			if(2 <= l)
			{
				for(int i = 0;i < n;++i)
				{
					__int64 opt = 0;
					if(t < basetimes[i+1])
					{
						__int64 remain = 0;
						if(t > basetimes[i]) remain = t-basetimes[i];
						int tomove = dis[i%c];
						opt = tomove*2 - (remain+tomove-remain/2);
					}
					//printf("opt = %I64u\n",opt);

					for(int k = i+1;k < n;++k)
					{
						if(t+opt >= basetimes[k+1]) continue;
						__int64 remain = 0;
						if(t > basetimes[k]) remain = t-basetimes[k]+opt;

						int tomove = dis[k%c];
						__int64 s = basetimes[n]-opt-tomove*2;
						s += remain + tomove-remain/2;

						if(s < ret) ret = s;
						//printf("i = %d,k = %d,ret = %I64u\n",i,k,ret);
					}
				}
			}
		}
		printf("Case #%d: %I64u\n",iCases,ret);
	}
	return 0;
}