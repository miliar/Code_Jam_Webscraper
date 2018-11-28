#include <stdio.h>
#include <iostream>
#include <sstream>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

int T,ans,ts;
__int64 i,j,n,p[1000001],k;
int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&T);
	for(i=2;i<1000;i++)
		if(!p[i])
			for(j=i*i;j<=1000000;j+=i)
				p[j]=1;
	for(i=2;i<1000000;i++)
		if(!p[i])
			p[k++]=i;
	while(T--)
	{
		scanf("%I64d",&n);
		if(n==1)
		{
			printf("Case #%d: 0\n",++ts);
			continue;
		}
		ans=1;
		for(i=0;i<k && p[i]*p[i]<=n;i++)
			for(j=p[i]*p[i];j<=n;j*=p[i])
				ans++;
		printf("Case #%d: %d\n",++ts,ans);
	}
	return 0;
}