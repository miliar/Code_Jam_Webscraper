#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

long long dynamic[2048][11];
int p;
int info[2048], data[1024];
int base;

long long getDynamic(int ind, int used);

int main(void)
{
	int t;
	scanf("%d", &t);
	for(int caseN=1;caseN<=t;caseN++)
	{
		memset(dynamic, -1, sizeof(dynamic));

		scanf("%d", &p);
		base = (1<<p);

		long long ans=0;
		for(int i=0;i<(1<<p);i++) 
			scanf("%d", info+i+base);
		
		int curBase = base/2;
		while(curBase>0)
		{
			int ind=0;
			while(ind<curBase)
			{
				int t1 = info[(ind+curBase)*2];
				int t2 = info[(ind+curBase)*2+1];

				info[curBase+ind] = min(t1, t2);
				scanf("%d", data+curBase+ind);
				ans+=data[curBase+ind];
				ind++;
			}
			curBase/=2;
		}

		ans -= getDynamic(1, 0);
		printf("Case #%d: %lld\n", caseN, ans);
	}
	
	return 0;
}

long long getDynamic(int ind, int used)
{
	long long &ret=dynamic[ind][used];
	if(ret!=-1) return ret;

	if(ind>=(1<<p))
	{
		if(used>info[ind]) return ret=-9999999999LL;
		else return ret=0;
	}

	int lim = info[ind];
	if(lim<used) ret=-99999999999LL;
	else
	{
		ret = getDynamic(ind*2, used) + getDynamic(ind*2+1, used);
		if(lim>used) ret = max(ret, data[ind] + getDynamic(ind*2, used+1) + getDynamic(ind*2+1, used+1));
		ret = max(ret, 0LL);
	}

	return ret;
}
