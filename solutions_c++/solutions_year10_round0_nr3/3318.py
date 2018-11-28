#include <cstdio>
#include <vector>

__int64 calc(int R, int K, const std::vector<int> &v)
{
	__int64 result = 0;

	size_t ofs;
	size_t sz = v.size();
	unsigned int rr = R%sz; if (!rr) rr=-1;
	__int64 sum_r=0, sum=0;
	size_t ii=0;
	size_t m = sz;
	if (m>R) m = R;

	for(size_t i=1; i<=R; ++i)
	{
		__int64 ss = v[ii];
		for (size_t j=1; j<sz; ++j)
		{
			ofs = (ii+j)%sz;
			ss += v[ofs];
			if (ss>=K)
			{
				if (ss>K) {ss -= v[ofs]; ii=ofs;}
				else {ii=(ofs+1)%sz;}
				break;
			}
		}
		sum += ss;
		if (i==R) return sum;
		if (i==rr) sum_r=sum;
	}
	
	return (R/sz)*sum + sum_r;
}

void main()
{
	unsigned int T, N;
	int R, K;
	std::vector<int> v;

	scanf("%u\n",&T);
	for (unsigned int i=1;i<=T;++i)
	{
		scanf("%d %d %d\n", &R, &K, &N);
		v.resize(N);
		for (unsigned int j=0;j<N;++j)
		{
			scanf("%d", &v.at(j));
		}
		__int64 kkk = calc(R, K, v);
		printf("Case #%u: %I64d\n", i, kkk);
	}
}
