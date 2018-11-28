#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <cstring>
#include <string>
using namespace std;
int c,d;
struct pos
{
	int p,v;
};
pos g[256];
#define EPS 1e-9
bool check(double t)
{
	int tmp;
	double prev;
	//tmp=v[0];
	// (tmp+1)/2 left tmp-(tmp+1)/2 right
	//prev=g[0].p-(t+(g[0].v-1)*d);
	prev=g[0].p-t+(g[0].v-1)*d;
	if(prev>=g[0].p)
	{
		if(prev-g[0].p>t)return false;
	}
	for(int i=1;i<c;i++)
	{
		//printf("prev is %lf\n",prev);
		if(g[i].p-prev==d)continue;
		if(g[i].p-prev<d)
		{
			if(prev+g[i].v*d-g[i].p>t)return false;
			prev=prev+g[i].v*d;
		}
		else
		{
			if(g[i].p-(prev+d)<=t)
			{
				//prev=prev+d;
				if(prev+(g[i].v)*d-g[i].p > t)return false;
				prev=prev+g[i].v*d;
			}
			else
			{
				prev=g[i].p-t;
				if(prev+(g[i].v-1)*d-g[i].p > t)return false;
				prev=prev+(g[i].v-1)*d;
			}
		}


	}
	return true;


}
bool compare(pos x,pos y)
{
	return x.p<y.p;
}
int main()
{
	int X;
	scanf("%d",&X);
	int kase=1;
	while(X--)
	{
		scanf("%d%d",&c,&d);
		for(int i=0;i<c;i++)scanf("%d%d",&g[i].p,&g[i].v);
		sort(g,g+c,compare);
		//for(int i=0;i<c;i++)printf("%d %d\n",g[i].p,g[i].v);
		//return 0;
		double low=0,mid,high=1000000000;
		//bool ttt=check(2.5);
		while(1)
		{
			mid=(low+high)/2;
			if(high>=low)
			{
				if(high-low<=1e-9)break;
			}
			if(check(mid))high=mid;
			else low=mid;
		}
		printf("Case #%d: %0.8lf\n",kase,mid);
		kase++;
	}
}

