#include <stdio.h>
#include <string.h>
#include <vector>

using std::vector;

int main()
{
	static const size_t buffsize = 0x100;
	static const size_t charset = 0x100;

	char buff[buffsize] = { 0 };
	int nCases = 0;scanf("%d",&nCases);
	for(int iCases = 1;iCases <= nCases;++iCases)
	{
		char combines[charset][charset] = { 0 };
		bool opposed[charset][charset] = { 0 };
		// deal with input
		{
			int c = 0,d = 0,n = 0;scanf("%d",&c);
			for(int i = 0;i < c;++i)
			{
				scanf("%s",buff);
				char c0 = buff[0],c1 = buff[1],c2 = buff[2];
				combines[c0][c1] = c2;
				combines[c1][c0] = c2;
			}
			scanf("%d",&d);
			for(int i = 0;i < d;++i)
			{
				scanf("%s",buff);
				char c0 = buff[0],c1 = buff[1];
				opposed[c0][c1] = true;
				opposed[c1][c0] = true;
			}
			scanf("%d",&n);scanf("%s",buff);
		}

		int p = 0,n = (int)(strlen(buff));
		vector<char> ret(n);
		for(int i = 0;i < n;++i)
		{
			char c = buff[i];;ret[p] = c;
			if(0 == p) { ++p;continue; }
			char prev = ret[p-1];
			if(combines[prev][c]) ret[p-1] = combines[prev][c];
			else
			{
				bool opp = false;
				for(int k = 0;k < p && !opp;++k)
				{
					if(opposed[ret[k]][c]) opp = true;
				}
				if(opp) p = 0;
				else ++p;
			}
		}

		printf("Case #%d: [",iCases);
		for(int i = 0;i < p;++i)
		{
			if(0 != i) printf(", ");
			printf("%c",ret[i]);
		}
		printf("]\n");
	}
	return 0;
}