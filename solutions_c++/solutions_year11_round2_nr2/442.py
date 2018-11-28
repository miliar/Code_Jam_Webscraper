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

using namespace std;

int a[1000010];
double ta[1000010];
int p,v,c,d,x;

bool func(double t)
{
	for(int i=0;i<x;i++) ta[i]=(double)a[i];
	
	ta[0]-=t;
	
	for(int i=1;i<x;i++)
	{
		double pos=ta[i-1]+d;
		double left=ta[i]-t;
		double right=ta[i]+t;
		if(pos<right || fabs(pos-right)<1e-7)
		{
			if(left<pos||fabs(left-pos)<1e-7) ta[i]=pos;
			else if(pos<left) ta[i]=left;
			else ta[i]=right;
		}
		else 
			return false;
	}
	return true;
}

double solve()
{
	double lo=0,hi=(double)1e15,mid;
	int itr=400;
	while(itr--)
	{
		mid=(lo+hi)/2.00;
		
		if(func(mid)) hi=mid;
		else lo=mid;
		
		if(fabs(lo-hi)<1e-7) break;
	}
	if(func(lo)) return lo;
	if(func(mid)) return mid;
	if(func(hi)) return hi;
}

int main()
{
	int cases;
	FILE* pFile=fopen("22.out","w");
	
	scanf("%d",&cases);
	for(int cas=1;cas<=cases;cas++)
	{
		scanf("%d %d",&c,&d);
		x=0;
		for(int i=0;i<c;i++)
		{
			scanf("%d %d",&p,&v);
			while(v--) a[x++]=p;
		}
		fprintf(pFile,"Case #%d: %.9lf\n",cas,solve());
	}
	return 0;
}