#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>

#define FOR(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define FORD(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define REP(i,n) for (int i(0),_n(n); i < _n; ++i)
#define REPD(i,n) for (int i((n)-1); i >= 0; --i)

#define LL __int64

LL scalar(const std::vector<LL>&v1,const std::vector<LL>&v2)
{
	LL res=0;
	REP(i,v1.size())
	{
		res+=v1[i]*v2[i];
	}
	return res;
}

bool LLb(const LL& lhs, const LL& rhs)
{
	return lhs > rhs;
}

bool LLm(const LL& lhs, const LL& rhs)
{
	return lhs < rhs;
}

LL min_scalar(std::vector<LL> v1,std::vector<LL> v2)
{
	std::sort(v1.begin(),v1.end(),LLb);
	std::sort(v2.begin(),v2.end(),LLm);
	return scalar(v1,v2);
}

void main()
{
	int N,K;
	scanf("%d", &N);

	int t;
	std::vector<LL> v1,v2;


	FOR(nCase,1,N)
	{
		scanf("%d", &K);
		v1.clear();
		v2.clear();
		REP(i,K)
		{
			scanf("%d",&t);
			v1.push_back(t);
		}
		REP(i,K)
		{
			scanf("%d",&t);
			v2.push_back(t);
		}
		printf("Case #%d: %I64d\n",nCase,min_scalar(v1,v2));
	}
}
