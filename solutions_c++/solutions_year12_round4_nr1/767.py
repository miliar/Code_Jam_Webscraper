#include <stdafx.h>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <ctime>
#include <cassert>

using namespace std;

const long maxn=10005;

long dp[maxn];
long d[maxn];
long l[maxn];
long n;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	long tests;
	scanf("%ld",&tests);
	for (long test=1;test<=tests;test++)
	{
		long q;
		printf("Case #%ld: ",test);
		scanf("%ld",&n);
		for (q=1;q<=n;q++)
			scanf("%ld%ld",&d[q],&l[q]);
		long final;
		scanf("%ld",&final);
		n++;
		d[n]=final;
		l[n]=0;
		for (q=1;q<=n;q++)
			dp[q]=-1;
		dp[1]=d[1];
		for (long it=1;it<n;it++) if (dp[it]!=-1)
		{
			for (long next=it+1;next<=n;next++)
			{
				if (d[it]+dp[it]>=d[next])
					dp[next]=max(dp[next],min(l[next],d[next]-d[it]));
				else break;
			}
		}
		if (dp[n]!=-1)
			printf("YES\n");
		else printf("NO\n");
	}
}