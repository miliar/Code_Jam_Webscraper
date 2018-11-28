#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;


int M; //no. of node
int value[10010];
int cost[10010][2];
int gate[5012];
int change[5012];
int ngate;
int goal;

int go(int pos,int g)
{
	int& v= cost[pos][g];
	if(v>=0) return v;
	if(value[pos] == g)
	{
		v = 0;
		return 0;
	}
	v = 10000;
	if(pos > ngate) return v;
	if(gate[pos])
	{
		if(0 == g)
			v = min(v,go(pos*2,0)+go(pos*2+1,0));
		if(0 == g)
			v = min(v,go(pos*2,0)+go(pos*2+1,1));
		if(0 == g)
			v = min(v,go(pos*2,1)+go(pos*2+1,0));
		if(1 == g)
			v = min(v,go(pos*2,1)+go(pos*2+1,1));

		if(change[pos])
		{
			if(0 == g)
				v = min(v,go(pos*2,0)+go(pos*2+1,0)+1);
			if(1 == g)
				v = min(v,go(pos*2,0)+go(pos*2+1,1)+1);
			if(1 == g)
				v = min(v,go(pos*2,1)+go(pos*2+1,0)+1);
			if(1 == g)
				v = min(v,go(pos*2,1)+go(pos*2+1,1)+1);

		}

	}
	else
	{
		if((0|0) == g)
			v = min(v,go(pos*2,0)+go(pos*2+1,0));
		if((0|1) == g)
			v = min(v,go(pos*2,0)+go(pos*2+1,1));
		if((1|0) == g)
			v = min(v,go(pos*2,1)+go(pos*2+1,0));
		if((1|1) == g)
			v = min(v,go(pos*2,1)+go(pos*2+1,1));


		if(change[pos])
		{
			if(0 == g)
				v = min(v,go(pos*2,0)+go(pos*2+1,0)+1);
			if(0 == g)
				v = min(v,go(pos*2,0)+go(pos*2+1,1)+1);
			if(0 == g)
				v = min(v,go(pos*2,1)+go(pos*2+1,0)+1);
			if(1 == g)
				v = min(v,go(pos*2,1)+go(pos*2+1,1)+1);
		}

	}
	return v;

	

}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	//freopen("B-large.in","r",stdin);
	//freopen("B-large.out","w",stdout);
	int T = 0;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		memset(cost,-1,sizeof(cost));
		memset(value,0,sizeof(value));
		
		scanf("%d",&M);
		ngate = (M-1)/2;
		scanf("%d",&goal);
		int t_gate,t_change;
		for(int j=1;j<=ngate;j++)
		{
			scanf("%d",&t_gate);
			gate[j]=t_gate;
			scanf("%d",&t_change);
			change[j] = t_change;

		}
		int tv;
		for(int j=ngate+1;j<=M;j++)
		{
			scanf("%d",&tv);
			value[j] = tv;
		}
		//computevalues();
		for(int j=ngate;j>=1;j--)
		{
			if(gate[j])
			{
				value[j] = value[2*j] & value[2*j+1];
			}
			else
			{
				value[j] = value[2*j] | value[2*j+1];
			}
		}
		int res = go(1,goal);

		if(res>=0 && res<10000)
		{
			printf("Case #%d: %d\n",i+1,res);			

		}
		else
		{
			printf("Case #%d: IMPOSSIBLE\n",i+1);
		}
	}
	return 0;
}