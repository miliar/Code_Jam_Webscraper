#include<stdio.h>
#include<algorithm>
using namespace std;

struct line{
	int a,b;
}l[1005];

int cmp(struct line x,struct line y)
{
	return x.a<y.a;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t,c;
	int n,i,j;
	int ans;
	scanf("%d",&t);
	for(c=1;c<=t;c++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%d%d",&l[i].a,&l[i].b);
		sort(l,l+n,cmp);
		ans=0;
		for(i=1;i<n;i++)
		{
			for(j=0;j<i;j++)
			{
				if(l[i].b<l[j].b)ans++;
			}
		}
		printf("Case #%d: %d\n",c,ans);
	}
	return 0;
}
