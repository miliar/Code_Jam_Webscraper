#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
int s[1005],seg[1005];
int num[1005];
int findseg(int x)
{
	if(x==seg[x])
		return x;
	else
		return seg[x]=findseg(seg[x]);
}
int main()
{
	int t,cas;
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++)
	{
		memset(num,0,sizeof(num));
		memset(s,0,sizeof(s));
		int n;
		scanf("%d",&n);
		int i;
		for(i=1;i<=n;i++)
		{
			scanf("%d",&s[i]);
			seg[s[i]]=s[i];
		}
		int ans=0;
		for(i=1;i<=n;i++)
		{
			int fa,fb;
			if(s[i]!=i)
			{
				fa=findseg(s[i]);
				fb=findseg(i);
				seg[fa]=fb;
			}
		}
		for(i=1;i<=n;i++)
		{
			int fa;
			fa=findseg(i);
			num[fa]++;
		}
		for(i=1;i<=n;i++)
			if(num[i]>1)
				ans+=num[i];
		printf("Case #%d: %d.000000\n",cas,ans);
	}
	return 0;
}
