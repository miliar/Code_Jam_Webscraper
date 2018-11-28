#include<iostream>
#include<stdio.h>
#include<algorithm>
using namespace std;
struct Pos
{
	int pos,num;
}xx[205];

int n,d;

int cmp(Pos a,Pos b)
{ return a.pos<b.pos;}
int work(int ans)
{
	int i,j,last;
	last=xx[0].pos-ans;
	for(i=0;i<n;i++)
	{
		for(j=0;j<xx[i].num;j++)
		{
			if(i==0 && j==0)continue;
			if(abs(xx[i].pos-(last+d))<=ans)//可以到last 位置
			{
				last+=d;
			}else
			{
				if(last+d<xx[i].pos)
				{
					last=xx[i].pos-ans;
				}
				else {return 0;}
			}
		}		
	}
	return 1;
} 
int main()
{
//	freopen("B-small-attempt0.in","r",stdin);
//	freopen("B.out","w",stdout);
	int ct,i,minn,maxn;
	int tt=0;
	int total;
	int high,low,mid;
	scanf("%d",&ct);
	while(ct--)
	{
		scanf("%d%d",&n,&d);
		total=0;
		d*=2;
		for(i=0;i<n;i++)
		{
			scanf("%d%d",&xx[i].pos,&xx[i].num);
			xx[i].pos*=2;
			total+=xx[i].num;
		}
		sort(xx,xx+n,cmp);
		
		high=(total-1)*d;
		low=0;
		while(low<high-1)
		{
			mid=(low+high)/2;
			if(work(mid)==1)
				high=mid;
			else low=mid;			
		}
		if(work(low)==0)low=high;
		printf("Case #%d: %.1lf\n",++tt,1.0*low/2);
	}
	return 0;
}