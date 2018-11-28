#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
int d[105],o[105],b[105],ta[105],tb[105];
char col[105][2];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-small.out","w",stdout);
	int t,cas=0;
	scanf("%d",&t);
	while(1)
	{
		cas++;
		if(cas>t)
			break;
		memset(ta,0,sizeof(ta));
		memset(tb,0,sizeof(tb));
		memset(col,0,sizeof(col));
		int i,n;
		int k1,k2;
		k1=k2=1;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%s%d",col[i],&d[i]);
			if(col[i][0]=='O')
				o[k1++]=d[i];
			else
				b[k2++]=d[i];
		}
		int pa,pb;
		pa=pb=1;
		for(i=1;i<k1;i++)
		{
			ta[i]=ta[i-1]+abs(o[i]-pa)+1;
			pa=o[i];
		}
		for(i=1;i<k2;i++)
		{
			tb[i]=tb[i-1]+abs(b[i]-pb)+1;
			pb=b[i];
		}
		int ans,j;
		pa=pb=1;ans=0;
		for(i=0;i<n;i++)
		{
			if(col[i][0]=='O')
			{
				int tmp=ans-ta[pa]+1;
				if(ta[pa]<=ans)
					for(j=pa;j<k1;j++)
						ta[j]+=tmp;
				ans=ta[pa];
				pa++;
			}
			else
			{
				int tmp=ans-tb[pb]+1;
				if(tb[pb]<=ans)
					for(j=pb;j<k2;j++)
						tb[j]+=tmp;
				ans=tb[pb];
				pb++;
			}
		}
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}
