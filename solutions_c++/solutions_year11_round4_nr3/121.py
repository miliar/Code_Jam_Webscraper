#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <string.h>
using namespace std;
const int MAX=1000001;
__int64 su[MAX],ns;
int main()
{
	int tc,cas,i,j,k;
	__int64 s,r;
	ns=0;
	for (i=2;i<MAX&&i*i<MAX;++i)
		if (!su[i])
		{
			su[ns++]=i;
			for (j=i*i;j<MAX;j+=i) su[j]=1;
		}
	for (;i<MAX;++i) if (!su[i]) su[ns++]=i;
	freopen("C-large.in","r",stdin);
	freopen("output_la.txt","w",stdout);
	scanf("%d",&tc);
	for (cas=1;cas<=tc;++cas)
	{
		scanf("%I64d", &s);
		int ans=0;
		if (s>1)
		{
		for (i=0;i<ns&&su[i]*su[i]<=s;++i)
		{
			int ct=0;
			r=su[i];
			while (r*su[i]<=s) {r*=su[i]; ++ct;}
			ans+=ct;
		}
		ans+=1;
		}
		printf("Case #%d: %d\n", cas,ans);
	}
	return 0;
}