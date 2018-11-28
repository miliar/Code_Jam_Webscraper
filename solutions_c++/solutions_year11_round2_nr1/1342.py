#include <stdio.h>
#include <vector>
#include <string>

using std::vector;
using std::string;

int main()
{
	int nCases = 0;scanf("%d",&nCases);
	for(int iCases = 1;iCases <= nCases;++iCases)
	{
		int n = 0;scanf("%d",&n);
		vector<string> schedule(n);
		char buff[0x100] = { 0 };
		for(int i = 0;i < n;++i)
		{
			scanf("%s",buff);
			schedule[i] = buff;
		}

		vector<int> wcounts(n,0);
		vector<int> counts(n,0);
		for(int i = 0;i < n;++i)
		{
			int wcount = 0;
			for(int k = 0;k < n;++k)
			{
				char c = schedule[i][k];
				if('.' == c) continue;
				++counts[i];
				wcounts[i] += (c=='1');
			}
		}

		vector<double> owp(n);
		for(int i = 0;i < n;++i)
		{
			double sum = 0;
			for(int k = 0;k < n;++k)
			{
				char c = schedule[i][k];
				if('.' == c) continue;
				int w = wcounts[k]-('0'==schedule[i][k]);
				int t = counts[k] - 1;
				sum += 1.0*w/t;
			}
			owp[i] = sum/counts[i];
		}

		vector<double> oowp(n);
		for(int i = 0;i < n;++i)
		{
			double sum = 0;
			for(int k = 0;k < n;++k)
			{
				char c = schedule[i][k];
				if('.' == c) continue;
				sum += owp[k];
			}
			oowp[i] = sum/counts[i];
		}

		vector<double> rpi(n);
		for(int i = 0;i < n;++i)
		{
			rpi[i] = 0.25*wcounts[i]/counts[i]+0.50*owp[i]+0.25*oowp[i];
		}

		printf("Case #%d:\n",iCases);
		for(int i = 0;i < n;++i)
		{
			printf("%.12f\n",rpi[i]);
		}

	}
	return 0;
}