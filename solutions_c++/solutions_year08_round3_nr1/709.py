#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <assert.h>
#include <algorithm>

using namespace std;
//#define DBG_PRINT printf
#define DBG_PRINT 


	
	int main()
	{
		int N,P,K,L,i,j;
		
		scanf("%d\n",&N);
		DBG_PRINT("%d\n",N);
		for (i=0;i<N;i++)//each case
		{
			scanf("%d%d%d\n",&P,&K,&L);
			DBG_PRINT("%d %d %d\n",P,K,L);

			vector<long long> CharFreq;//µ¥´ÊÆµÂÊ
			CharFreq.reserve(L);
			for (j=0;j<L;j++)//each char
			{
				long long word;
				scanf("%lld",&word);
				CharFreq.push_back(word);
			}

			//sort
			//CharFreq.sort();
			sort(CharFreq.begin(),CharFreq.end());
			long long sum = 0;
			int n=0;
			int nLevel=1;
			for (j=L-1;j>=0;j--)
			{
				sum += nLevel*CharFreq[j];
				n++;
				if(n==K)
				{
					nLevel++;
					n=0;
				}
			}
			printf("Case #%lld: %d\n",i+1,sum);
		}
		return 0;
	}

