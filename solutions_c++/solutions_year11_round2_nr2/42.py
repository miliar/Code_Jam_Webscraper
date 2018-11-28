#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <set>
#include <queue>
#include <cmath>
#include <algorithm>
using namespace std;

int p[200],v[200];
bool good(int n,double d,double tm)
{
	double st=-1e18, st2;
	int i;
	for(i=0;i<n;i++)
	{
		st2=p[i]-tm;
		if (st2<st) st2=st;
		if (st2+(v[i]-1)*d>p[i]+tm) return false;
		st=st2+v[i]*d;
	}
	return true;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int n,i,j,k,T,d;

	cin>>T;
	for(int test=1;test<=T;test++)
	{
		cin>>n>>d;
		for(i=0;i<n;i++) cin>>p[i]>>v[i];
		double l=0, r=1e14, mid;
		for(int it=0;it<200;it++)
		{
			mid=(l+r)/2;
			if (good(n,d,mid)) r=mid; else l=mid;
		}
		printf("Case #%d: ",test);
		printf("%.8lf\n",l);
	}

	return 0;
}