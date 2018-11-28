#include <stdio.h>
#include <vector>

using std::vector;

int main()
{
	const int maxn = 500;
	const int mod = 100003;
	vector< vector<int> > combs(maxn+1,vector<int>(maxn+1,0));
	for(int p = 0;p <= maxn;++p) combs[p][0] = 1;
	for(int p = 1;p <= maxn;++p)
	{
		for(int i = 1;i <= p;++i)
		{
			combs[p][i] = combs[p-1][i]+combs[p-1][i-1];
			combs[p][i] %= mod;
		}
	}

	vector< vector<int> > dps(maxn+1,vector<int>(maxn+1,0));
	for(int p = 2;p <= maxn;++p) { dps[p][2] = dps[p][1] = 1; }
	dps[2][2] = 0;
	for(int p = 2;p <= maxn;++p)
	{
		for(int i = 3;i < p;++i)
		{
			int low = 2*i-p;
			for(int j = (low>1?low:1);j < i;++j)
			{
				unsigned long long s = dps[i][j],t = combs[p-1-i][i-j-1];
				s *= t;s %= mod;dps[p][i] += (int)s;dps[p][i] %= mod;
			}
		}
	}

	vector<int> result(maxn+1,0);
	for(int p = 2;p <= maxn;++p)
	{
		for(int i = 1;i < p;++i) 
		{
			result[p] += dps[p][i];
			result[p] %= mod;
		}
	}

	int nCases = 0;scanf("%d",&nCases);
	for(int iCases = 1;iCases <= nCases;++iCases)
	{
		int n = 0;scanf("%d",&n);
		printf("Case #%d: %d\n",iCases,result[n]);
	}
	return 0;
}

