// Saving the Universe.cpp : Defines the entry point for the console application.
//

#include <string>
#include <vector>
#include <stdio.h>
using namespace std;


int main()
{
	int n, s, q;
	vector<string> vS, vQ;

	scanf("%d", &n);
	for(int i = 0; i < n; i++)
	{
		scanf("%d", &s);
		getchar();
		vS.clear();
		vQ.clear();
		for(int j = 0; j < s; j++)
		{
			char sz[110];
			gets(sz);
			vS.push_back(sz);
		}
		scanf("%d", &q);
		getchar();
		for(int j = 0; j < q; j++)
		{
			char sz[110];
			gets(sz);
			vQ.push_back(sz);
		}
		size_t num = 0;
		int nOut = 0;
		if(vQ.size() == 0)
		{
			nOut = 1;
		}
		while(1)
		{
			if(num >= vQ.size()) break;
			size_t nMax = 0;
			for(size_t j = 0; j < vS.size(); j++)
			{
				size_t nCount = vQ.size();
				for(size_t k = num; k < vQ.size(); k++)
				{
					if(vS[j] == vQ[k])
					{
						nCount = k;
						break;
					}
				}
				if(nCount > nMax)
				{
					nMax = nCount;
				}
			}
			num = nMax;
			nOut++;
		}
		printf("Case #%d: %d\n", i + 1, nOut - 1);
	}
	getchar();

	return 0;
}

