#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <string.h>
using namespace std;
int s[10002];
int main()
{
	int tc,cas,i,j,n,ans;
	freopen("B-large.in","r",stdin);
	freopen("output_la.txt","w",stdout);
	scanf("%d",&tc);
	for (cas=1;cas<=tc;++cas)
	{
		memset(s,0,sizeof(s));
		scanf("%d",&n);
		for(i=0;i<n;++i) {scanf("%d",&j); s[j]++;}
		if (n)
		{
			ans=100000;
			for (i=0;i<=10000;++i)
				while (s[i])
				{
					for (j=i+1;s[j]>=s[j-1];++j);
					for (int k=i;k<j;++k) s[k]--;
					if (j-i<ans) ans=j-i;
				}
		}
		else ans=0;
		printf("Case #%d: %d\n", cas,ans);
	}
	return 0;
}