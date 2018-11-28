//#include <stdafx.h>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <ctime>
#include <cassert>

using namespace std;

long ans=0;

struct mytriple
{
	long first;
	long second;
	long third;
};

vector <mytriple> list[100];
long n,s,p;
long a[100];

void prepare()
{
	mytriple t;
	for (t.first=0;t.first<=10;t.first++)
		for (t.second=t.first;t.second<=10;t.second++)
			for (t.third=t.second;t.third<=10;t.third++) if (t.third-t.first<=2)
			{
				list[t.first+t.second+t.third].push_back(t);
			}
}

bool surp(mytriple tr)
{
	long t1=max(max(tr.first,tr.second),tr.third);
	long t2=min(min(tr.first,tr.second),tr.third);
	return(t1-t2==2);
}

long get(mytriple tr)
{
	return(max(max(tr.first,tr.second),tr.third));
}

void solve(long step,long snow,long count)
{
	if (step==n+1)
	{
		if (snow==s)
			ans=max(ans,count);
		return;
	}
	for (long j=0;j<list[a[step]].size();j++)
	{
		long pl=0;
		if (get(list[a[step]][j])>=p)
			pl++;
		solve(step+1,snow+surp(list[a[step]][j]),count+pl);
	}
}

int main()
{
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	prepare();
	long tests,q;
	scanf("%ld",&tests);
	for (long test=1;test<=tests;test++)
	{
		scanf("%ld%ld%ld",&n,&s,&p);
		for (q=1;q<=n;q++)
			scanf("%ld",&a[q]);
		ans=0;
		solve(1,0,0);
		printf("Case #%ld: %ld\n",test,ans);
	}
}