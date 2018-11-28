#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
struct Segment
{
	char r;
	int p;
} a[200];
int t,o[200],b[200],oo,bb,n;
char s[10];

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&t);
	for (int tt=1;tt<=t;tt++)
	{
		oo=bb=0;
		scanf("%d",&n);
		for (int i=1;i<=n;i++)
		{
			scanf("%s",s);
			a[i].r=s[0];
			scanf("%d",&a[i].p);
			if (a[i].r=='O')
			{
				oo++;
				o[oo]=i;
			}
			else
			{
				bb++;
				b[bb]=i;
			}
		}
		oo++;o[oo]=n+1;
		bb++;b[bb]=n+1;
		int so=1,sb=1,ti=0;
		for (int i=1,j=1;o[i]<=n || b[j]<=n;)
			if (o[i]<b[j])
			{
				while (so!=a[o[i]].p)
				{
					ti++;
					if (so<a[o[i]].p && o[i]<=n)
						so++;
					else so--;
					if (sb<a[b[j]].p && b[j]<=n)
						sb++;
					else if (sb>a[b[j]].p && b[j]<=n)
						sb--;
				}
				ti++;
				i++;
				if (sb<a[b[j]].p && b[j]<=n)
					sb++;
				else if (sb>a[b[j]].p && b[j]<=n)
					sb--;
			}
			else
			{
				while (sb!=a[b[j]].p)
				{
					ti++;
					if (sb<a[b[j]].p && b[j]<=n)
						sb++;
					else sb--;
					if (so<a[o[i]].p && o[i]<=n)
						so++;
					else if (so>a[o[i]].p && o[i]<=n)
						so--;
				}
				ti++;
				j++;
				if (so<a[o[i]].p && o[i]<=n)
					so++;
				else if (so>a[o[i]].p && o[i]<=n)
					so--;
			}
		printf("Case #%d: %d\n",tt,ti);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}