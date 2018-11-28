#include<stdio.h>
#include<string.h>
#include<assert.h>
#include<algorithm>
using namespace std;
struct node
{
	int r,x,y,number;
};
bool operator <(const node &a,const node &b)
{
	return a.r>b.r;
}
bool cmp(node a,node b)
{
	return a.number<b.number;
}
node a[1000];
int main()
{
	int t,tt,n,w,l,i,j,x,y,z,zz,temp;
	scanf("%d",&t);
	for (tt=1;tt<=t;tt++)
	{
		scanf("%d %d %d",&n,&w,&l);
		for (i=0;i<n;i++)
		{
			scanf("%d",&a[i].r);
			a[i].number=i;
		}
		sort(a,a+n);
		printf("Case #%d:",tt);
		i=0;
		y=0;
		zz=0;
		while (i<n)
		{
			x=0;
			j=i;
			z=0;
			while (j<n)
			{
				if (z==0)
				{
					x+=a[j].r;
					z=1;
				}
				else if (x+a[j].r<=w)
					x+=a[j].r*2;
				else
					break;
				j++;
			}
			temp=a[i].r;
			x=0;
			z=0;
			while (i<j)
			{
				if (z==0)
				{
					a[i].x=0;
					x+=a[i].r;
					z=1;
				}
				else
				{
					a[i].x=x+a[i].r;
					x+=a[i].r*2;
				}
				if (zz==0)
					a[i].y=0;
				else
					a[i].y=y+a[i].r;
				i++;	
			}
			if (zz==0)
			{
				y+=temp;
				zz=1;
			}
			else
				y+=temp*2;
		}
		sort(a,a+n,cmp);
		for (i=0;i<n;i++)
		{
			assert(a[i].x<=w&&a[i].y<=l);
			printf(" %d %d",a[i].x,a[i].y);
		}
		printf("\n");
	}
	return 0;
}