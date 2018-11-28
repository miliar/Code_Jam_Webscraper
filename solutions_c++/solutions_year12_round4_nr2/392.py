#include<cstring>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<iostream>
#include<cmath>
#define N 1000
using namespace std;

struct Point
{
	int x,y;
};

struct node
{
	int r,num;
};

int cmp(node a,node b)
{
	return a.r>b.r;
}

node a[N];
Point res[N];

main()
{
	int t,n,ys,w,l,i,x,y,mid;

	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&t);
	ys=0;
	while (t--)
	{
		scanf("%d%d%d",&n,&w,&l);
		for (i=0;i<n;i++)
		{
			scanf("%d",&a[i].r);
			a[i].num=i;
		}
		sort(a,a+n,cmp);

		y=a[0].r,x=a[0].r;
		res[a[0].num].x=res[a[0].num].y=0;
		mid=0;

		for (i=1;i<n;i++)
		{
			if (x+a[i].r>w)
			{
				res[a[i].num].x=0;
				res[a[i].num].y=y+a[i].r;
				x=a[i].r;
				mid=y+a[i].r;
				y=y+a[i].r*2;

			}
			else
			{
				res[a[i].num].x=x+a[i].r;
				res[a[i].num].y=mid;
				x=x+a[i].r*2;
			}
		}

		printf("Case #%d: ",++ys);
		for (i=0;i<n;i++)
			printf("%d %d ",res[i].x,res[i].y);
		printf("\n");

	}

	return 0;
}





