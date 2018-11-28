#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

const int inf = 1000*1000*1000;
#define CL(x,a) memset(x,a,sizeof(x));
#define ALL(v) (v).begin(),(v).end()
typedef long long LL;

int T,S,C;
LL res;
map<int,int> mp;
void solve()
{
	scanf("%d",&C);
	S=0;
	res=0;
	mp.clear();
	for (int i=0;i<C;i++)
	{
		int t1,t2;
		scanf("%d%d",&t1,&t2);
		mp[t1]=t2;
		S+=t2;
	}
	bool ok = 1;
	map<int,int>::iterator it = mp.begin();
	while(1)
	{
		//map<int,int>::iterator next = it+1;
		if (it == mp.end())
		{
			it = mp.begin();
			if (ok)
				break;
			ok=1;
		}
		int ind = it->first, c = it->second;
		if (c > 1)
			ok = 0;
		if (c == 0)
		{
			
		}
		else
		{
			c/=2;
			res+=c;
			mp[ind-1]+=c; mp[ind+1]+=c;
			it->second-=c*2;
		}
		it++;
	}
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for (int i=0;i<T;i++)
	{
		solve();
		printf("Case #%d: %lld\n",i+1,res);
	}
	return 0;
}