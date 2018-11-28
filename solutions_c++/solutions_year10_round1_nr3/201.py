#pragma comment(linker,"/STACK:67108864")
#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>
#include <math.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

const int inf = 1000*1000*1000;
#define CL(x,a) memset(x,a,sizeof(x));
#define ALL(v) (v).begin(),(v).end();
typedef long long LL;
int T,A1,A2,B1,B2;
struct P
{
	int x,y;
	P(int _x = 0, int _y = 0)
	{
		x = _x; y = _y;
	}
	friend bool operator < (const P & a, const P & b)
	{
		return a.x < b.x || a.x == b.x && a.y < b.y;
	}
};
map<P,bool> mp;
int DP(int a, int b)
{
	bool res = 0;
	map<P,bool>::iterator it = mp.find(P(a,b));
	if (it != mp.end())
	{
		return it->second;
	}
	int x=1;
	int t=0;
	x = (int)(ceil((a+0.0)/b))-1;
	if (x > 0)
	{
		t = DP(a-b*x,b);
		if (t == 0)
		{
			res=1;
		}
	}
	x = (int)(ceil((b+0.0)/a))-1;
	if (x > 0)
	{
		t = DP(a,b-a*x);
		if (t == 0)
		{
			res=1;
		}
	}

	x = (int)(ceil((a+0.0)/b))-2;
	if (x > 0)
	{
		t = DP(a-b*x,b);
		if (t == 0)
		{
			res=1;
		}
	}
	x = (int)(ceil((b+0.0)/a))-2;
	if (x > 0)
	{
		t = DP(a,b-a*x);
		if (t == 0)
		{
			res=1;
		}
	}
	mp[P(a,b)]=res;
	return res;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for (int i=0;i<T;i++)
	{
		scanf("%d%d%d%d",&A1,&A2,&B1,&B2);
		int res=0;
		for (int j=A1;j<=A2;j++)
		{
			for (int k=B1;k<=B2;k++)
			{
				res+=DP(j,k);
			}
		}
		printf("Case #%d: %d\n",i+1,res);
	}
	return 0;
}