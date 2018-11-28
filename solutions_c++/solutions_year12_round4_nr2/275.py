#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstdlib>
using namespace std;

#define sqr(x) ((x)*(x))

#define debug(x) cout << #x << "=" << x << endl

int test,tests,swp,low,n,w,l;
int xx,yy;

struct tdot
{
	int x,y,id,r;
}d[1100];

int cmpr(tdot a, tdot b)
{
	return a.r > b.r;
}
int cmpid(tdot a, tdot b)
{
	return a.id < b.id;
}

int main()
{
	freopen("b1.in","r",stdin);
	freopen("b1.out","w",stdout);
	scanf("%d",&tests);
	for (int test=1;test<=tests;test++)
	{
		scanf("%d%d%d",&n,&w,&l);
		for (int i=1;i<=n;i++)
		{
			scanf("%d",&d[i].r);
			d[i].id = i;
		}
		swp = 0;
		if (w>l)
		{
			swp = 1;
			swap(w,l);
		}
		
		sort(d+1,d+n+1,cmpr);
		
		low = d[1].r;
		d[1].x = d[1].y = 0;
		for (int i=2;i<=n;i++)
		{
			d[i].x = d[i-1].x + d[i-1].r + d[i].r;
			if (d[i].x <= w)
			{
				d[i].y = d[i-1].y;
				continue;
			}
			d[i].x = 0;
			d[i].y = low + d[i].r;
			low = d[i].y + d[i].r;
		}
		sort(d+1,d+n+1,cmpid);
		if (swp)
		{
			for (int i=1;i<=n;i++) swap(d[i].x,d[i].y);
			swap(w,l);
		}
		
		int ok  =1;
		for (int i=1;i<n;i++) for (int j=i+1;j<=n;j++) if (sqr((long long)d[i].r+d[j].r)  >  sqr((long long)d[i].x-d[j].x)+sqr((long long)d[i].y-d[j].y))
		{
			printf("### %d %d %d %d\n",d[i].x,d[i].y,d[j].x,d[j].y);
		}
		if (!ok) printf("\nERROR dis\n\n");
		for (int i=1;i<=n;i++) if (d[i].x<0 || d[i].x > w || d[i].y < 0 || d[i].y > l) ok =  0;
		if (!ok) printf("\nERROR range\n\n");
		
		printf("Case #%d:",test);
		for (int i=1;i<=n;i++) printf(" %d %d",d[i].x,d[i].y);
		printf("\n");
	}
	return 0;
}
