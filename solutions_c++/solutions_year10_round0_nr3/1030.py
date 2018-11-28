#include <stdio.h>
#include <vector>

using std::vector;

int main()
{
	int nCases = 0;
	scanf("%d",&nCases);
	for(int iCases = 1;iCases <= nCases;++iCases)
	{
		int r = 0,k = 0,n = 0;
		scanf("%d%d%d",&r,&k,&n);
		vector<int> data(n);
		for(int i = 0;i < n;++i) scanf("%d",&data[i]);
		vector<int> used(n,-1);
		vector<int> moneys;
		int p = 0;
		unsigned long long sum = 0;
		for(int i = 0;i < r;++i)
		{
			if(used[p] != -1) break;
			used[p] = i;
			int len = 0,s = 0;
			for(;len < n;++len)
			{
				if(s+data[p] > k) break;
				s += data[p];
				++p;if(p == n) p = 0;
			}
			moneys.push_back(s);
			sum += s;
		}
		printf("Case #%d: ",iCases);
		if(used[p] == -1) { printf("%I64u\n",sum);continue; }
		unsigned long long ret = 0;
		for(int i = 0;i < used[p];++i) ret += moneys[i];
		unsigned long long loop = sum - ret;
		int loop_size = (int)(moneys.size() - used[p]);
		for(int i = used[p];i < moneys.size();++i)
		{
			if(0 == (r-i)%loop_size) { ret += (r-i)/loop_size*loop;break; }
			ret += moneys[i];
		}
		printf("%I64u\n",ret);
	}
	return 0;
}