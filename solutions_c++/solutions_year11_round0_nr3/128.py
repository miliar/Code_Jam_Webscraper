#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
int s[1005];
bool cmp(int a,int b)
{return a<b;}
int main()
{
	int t,cas;
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++)
	{
		memset(s,0,sizeof(s));
		int n;
		scanf("%d",&n);
		int i;
		for(i=0;i<n;i++)
			scanf("%d",&s[i]);
		int tmp=s[0];
		for(i=1;i<n;i++)
			tmp^=s[i];
		if(tmp!=0)
		{
			printf("Case #%d: NO\n",cas);
			continue;
		}
		int ans=0;
		sort(s,s+n,cmp);
		for(i=1;i<n;i++)
			ans+=s[i];
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}
