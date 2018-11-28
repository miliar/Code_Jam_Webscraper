#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<list>
#include<queue>
#include<map>
#include<algorithm>
using namespace std;

int csK, csN;
int N, ans;
map<int, int> M, M2;

int main()
{
	int i, j, k, m, t;
	map<int, int>::iterator itr;
	scanf("%d", &csN);
	for(csK = 1; csK <= csN; ++csK)
	{
		scanf("%d", &N);
		M.clear();
		ans = m = 0;
		for(i = 0; i < N; ++i)
		{
			scanf("%d %d", &j, &k);
			M[j] = k;
			if(k > 1) m = 1;
		}
		while(m > 0)
		{
			M2.clear();
			m = 0;
			for(itr = M.begin(); itr != M.end(); ++itr)
			{
				if(itr->second&1) ++M2[itr->first];
				if(itr->second > 1)
				{
					t = itr->second >> 1;
					M2[itr->first-1] += t;
					M2[itr->first+1] += t;
					ans += t;
				}
			}
			for(itr = M2.begin(); itr != M2.end(); ++itr)
				if(itr->second > 1) break;
			if(itr == M2.end()) break;
			M.clear();
			for(itr = M2.begin(); itr != M2.end(); ++itr)
			{
				if(itr->second&1) ++M[itr->first];
				if(itr->second > 1)
				{
					t = itr->second >> 1;
					M[itr->first-1] += t;
					M[itr->first+1] += t;
					ans += t;
				}
			}
			for(itr = M.begin(); itr != M.end(); ++itr)
				if(itr->second > 1) break;
			m = (itr==M.end()) ? 0 : 1;
		}

		printf("Case #%d: %d\n", csK, ans);
	}
}




