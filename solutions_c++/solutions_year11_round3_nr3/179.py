#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
int s[105];
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("Bout.out","w",stdout);
	int t,cas;
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++)
	{
		memset(s,0,sizeof(s));
		int n,l,h;
		scanf("%d%d%d",&n,&l,&h);
		int i,j,flag;
		for(i=0;i<n;i++)
			scanf("%d",&s[i]);
		for(i=l;i<=h;i++)
		{
			flag=1;
			for(j=0;flag&&j<n;j++)
				if(i%s[j]!=0&&s[j]%i!=0)
					flag=0;
			if(flag)
				break;
		}
		if(flag)
			printf("Case #%d: %d\n",cas,i);
		else
			printf("Case #%d: NO\n",cas);
	}
	return 0;
}
