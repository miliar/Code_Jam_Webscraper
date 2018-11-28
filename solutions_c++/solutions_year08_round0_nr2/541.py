#include <string>
#include <assert.h>
#include <stdio.h>
#include <vector>
#include <algorithm>

#define MAX_TIME 24*60

unsigned int count(const std::vector<unsigned int>&v_out,const std::vector<unsigned int>&v_ready)
{
	unsigned int res=v_out.size();
	unsigned int kk=0;

	for (unsigned int j=0;j<v_out.size();++j)
	{
		if (!res) break;
		for (unsigned int k=kk;k<v_ready.size();++k)
		{
			if (v_out[j]>=v_ready[k])
			{
				--res;
				kk=k+1;
				break;
			}
		}
	}

	return res;
}

void main()
{
	unsigned int n, T, NA, NB;
	unsigned int h1,m1,h2,m2,tmp;
	unsigned int cntA,cntB;

	std::vector<unsigned int> v_outA;
	std::vector<unsigned int> v_readyA;
	std::vector<unsigned int> v_outB;
	std::vector<unsigned int> v_readyB;


	scanf("%d\n",&n);
	for (unsigned int i=1;i<=n;++i)
	{
		v_outA.clear();
		v_readyA.clear();
		v_outB.clear();
		v_readyB.clear();

		cntA=0;
		cntB=0;

		scanf("%d\n",&T);
		scanf("%d %d\n",&NA,&NB);

		for (unsigned int j=0;j<NA;++j)
		{
			scanf("%d:%d %d:%d\n",&h1,&m1,&h2,&m2);
			v_outA.push_back(h1*60+m1);
			tmp=h2*60+m2+T;
			if (tmp>MAX_TIME) 
			{
				tmp-=MAX_TIME;
				++cntB;
			}
			v_readyB.push_back(tmp);
		}

		for (unsigned int j=0;j<NB;++j)
		{
			scanf("%d:%d %d:%d\n",&h1,&m1,&h2,&m2);
			v_outB.push_back(h1*60+m1);
			tmp=h2*60+m2+T;
			if (tmp>MAX_TIME) 
			{
				tmp-=MAX_TIME;
				++cntA;
			}
			v_readyA.push_back(tmp);
		}

		std::sort(v_outA.begin(),v_outA.end());
		std::sort(v_readyA.begin(),v_readyA.end());
		std::sort(v_outB.begin(),v_outB.end());
		std::sort(v_readyB.begin(),v_readyB.end());

		cntA += count(v_outA,v_readyA);
		cntB += count(v_outB,v_readyB);

		printf("Case #%d: %d %d\n",i,cntA,cntB);
	}
}