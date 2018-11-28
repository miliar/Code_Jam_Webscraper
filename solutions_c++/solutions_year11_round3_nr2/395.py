#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>
#include <cstring>
using namespace std;

struct COST
{
	long long cost;
	long long idx;
	COST():cost(-1), idx(-1){}
};

bool cmp(const COST& c1, const COST& c2)
{
	return c1.cost > c2.cost;
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int tcase=1; tcase <= T; ++tcase)
	{
		long long L, t, N, C;
		scanf("%lld %lld %lld %lld", &L, &t, &N, &C);

		vector<int> cs(C, 0);
		for(long long i=0; i < C; ++i)
			scanf("%d", &cs[i]);
		for(long long i=0; i < C; ++i)
			cs[i]*=10;
		
		long long spent=0;
		vector<COST> bs(N,COST());
		for(long long _i=0; _i < N; ++_i)
		{
			long long i = _i%C;
			long long far = cs[i];
			if( spent+(far/5) > t )
			{
				
				for(long long _j=0; _j < _i; ++_j)
					bs[_j].cost=-1, bs[_j].idx=_j;
				long long rest = (t-spent)*5;
				bs[_i].cost = (far-rest);
				bs[_i].idx=_i;
				for(long long _j=_i+1; _j < N; ++_j)
				{
					long long j = _j%C;
					long long far2 = cs[j];
					bs[_j].cost = far2;
					bs[_j].idx=_j;
					
				}
				sort(bs.begin(), bs.end(), cmp);
				
				for(size_t _j=0; _j < bs.size(); ++_j)
				{
					if(bs[_j].idx==-1)break;
					if(bs[_j].idx < _i) continue;
					long long j = bs[_j].idx%C;
					if( _j < L )
					{
						if( bs[_j].idx == _i )
						{
							spent += ((rest/5)+(bs[_j].cost/10));
						}
						else
							spent += (cs[j]/10);
					}
					else
						spent += (cs[j]/5);
				}
				break;
			}
			else
			{
				spent += (far/5);
			}
		}
		printf("Case #%d: %lld\n",tcase, spent);

		
	}
	return 0;
}

