#include <stdio.h>
#include <vector>

using std::vector;

int main()
{
	int nCases = 0;scanf("%d",&nCases);
	for(int iCases = 1;iCases <= nCases;++iCases)
	{
		int p = 0;scanf("%d",&p);
		int n = 1<<p;
		vector<int> require(n,0);
		for(int i = 0;i < n;++i) scanf("%d",&require[i]);
		for(int i = 0;i < p;++i)
		{
			int je = 1<<(p-i-1);
			for(int j = 0;j < je;++j)
			{
				int t = 0;
				scanf("%d",&t);
			}
		}
		int ret = 0;
		vector<int> rank(n,p);
		for(;;)
		{
			int i = 0;
			for(;i < n && p == require[i];++i);
			if(i == n) break;
			int u = rank[i];
			int v = 1<<u;u;
			++ret;--rank[i];
			int kb = i/v*v;
			int ke = kb + v;
			for(int k = kb;k < ke;++k)
			{
				if(rank[k] >= u) rank[k] = u-1;
				if(require[k] != p) ++require[k];
			}
		}
		printf("Case #%d: %d\n",iCases,ret);
	}
	return 0;
}