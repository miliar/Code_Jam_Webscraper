#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
int T,n,d[11111],l[11111],a[11111],D;
bool ok;

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&T);
	for (int tt=1; tt<=T; tt++)
	{
		scanf("%d",&n);
		memset(a,0,sizeof a);
		for (int i=1; i<=n; i++)
			scanf("%d%d",&d[i],&l[i]);
		a[1]=d[1];
	    for (int i=1; i<=n; i++)
	        if (a[i]>0)
	        {
				for (int j=i+1; j<=n; j++)
				{
					if (d[i]+a[i]<d[j])
					    break;
					int x=min(l[j],d[j]-d[i]);
					a[j]=max(a[j],x);
			    }
		    }
		scanf("%d",&D);
		ok=false;
		for (int i=1; i<=n; i++)
			if (d[i]+a[i]>=D)
			{
			    ok=true; break;
	        }
	    printf("Case #%d: ",tt);
	    if (ok)
	        printf("YES\n");
	    else
	        printf("NO\n");
    }
}
