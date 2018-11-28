#include <stdio.h>
#include <algorithm>
using namespace std;
struct pp
{
	int l,r;
}nod[1010];
bool cmp(pp a,pp b)
{
	return a.l<b.l||(a.l==b.l&&a.r<b.r);
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int id=1;id<=T;id++)
	{
		int n;
		scanf("%d",&n);
		int i,j;
		for(i=0;i<n;i++)
		{
			scanf("%d%d",&nod[i].l,&nod[i].r);
		}
		int ans=0;
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{
				if(i==j)
					continue;
				if(nod[i].l>nod[j].l&&nod[i].r<nod[j].r)
					ans++;
				else if(nod[i].l<nod[j].l&&nod[i].r>nod[j].r)
					ans++;
			}
		}
		printf("Case #%d: %d\n",id,ans/2);
	}
	return 0;
}
