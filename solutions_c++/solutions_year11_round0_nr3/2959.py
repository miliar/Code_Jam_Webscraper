#include <stdafx.h>
#include <stdio.h>

const long maxn=1005;

long mark[maxn];
long mas[maxn];
long n,best,tests,q;

void solve(long i)
{
	long q;
	if (i==n+1)
	{
		long first=0;
		long second=0;
		long sum=0;
		bool pp=false;
		for (q=1;q<=n;q++)
			if (mark[q]==1)
			{
				first=first ^ mas[q];
				sum+=mas[q];
			}
			else
			{
				second=second ^ mas[q];
				pp=true;
			}
		if ((first==second)&&(pp==true))
			if (sum>best)
				best=sum;
		return;
	}

	mark[i]=1;
	solve(i+1);
	mark[i]=2;
	solve(i+1);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%ld",&tests);
	for (long it=1;it<=tests;it++)
	{
		scanf("%ld",&n);
		for (q=1;q<=n;q++)
			scanf("%ld",&mas[q]);
		best=-1;
		solve(1);
		printf("Case #%ld: ",it);
		if (best==-1) printf("NO\n");
		else printf("%ld\n",best);
	}
}