#include <stdio.h>
#include <math.h>
int main()
{
	int p[101],b[101],rp[2],rt[2],i,t,n;
	char s[10];
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&t);
	for (int cas = 1; cas<=t; cas++)
	{
		scanf("%d",&n);
		for (i=0; i<n; i++)
		{
			scanf("%s%d",s,&b[i]);
			if (s[0]=='O') p[i]=0;
			else p[i]=1;
		}
		rt[0]=rt[1]=0;
		rp[0]=rp[1]=1;
		for (i=0; i<n; i++)
		{
			if (rt[p[i]] < rt[(p[i]+1)%2])
			{
				rt[p[i]] += abs(rp[p[i]]-b[i]);
				if (rt[p[i]] < rt[(p[i]+1)%2])
					rt[p[i]] = rt[(p[i]+1)%2] + 1;
				else rt[p[i]]++;
				rp[p[i]] = b[i];
			} else {
				rt[p[i]] += abs(rp[p[i]]-b[i]) + 1;
				rp[p[i]]=b[i];
			}
		}
		printf("Case #%d: %d\n",cas,((rt[0]>rt[1])?rt[0]:rt[1]));
	}
	return 0;
}

