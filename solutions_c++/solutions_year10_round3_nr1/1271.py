#include <cstdio>
#include <vector>
#include <algorithm>

bool comp(const std::pair<int, int> &a, const std::pair<int, int> &b)
{
	return a.first<b.first;
}

int calc(const std::vector< std::pair<int, int> > &A)
{
	int res = 0;

 	for (int i=0;i<(int)A.size();++i)
 	{
 		for (int j=0;j<(int)A.size();++j)
 		{
 			if (A[i].first<A[j].first && A[i].second>A[j].second) ++res;
 		}
 	}

	return res;
}

void main()
{
	int nCases, N, tA, tB;
	scanf("%d", &nCases);

	for(int nCase=1;nCase<=nCases;++nCase)
	{
		std::vector<std::pair<int, int> > A;
		scanf("%d", &N);
		for (int i=0;i<N;++i)
		{
			scanf("%d %d", &tA,&tB);
			A.push_back(std::make_pair(tA, tB));
		}
		std::sort(A.begin(), A.end(), comp);
		printf("Case #%d: %d\n", nCase, calc(A));
	}
}

