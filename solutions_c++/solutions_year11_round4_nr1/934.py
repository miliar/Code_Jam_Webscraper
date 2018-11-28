#include<stdio.h>
#include<algorithm>
using namespace std;

int x,s,r,t,n;
typedef struct
{
	int s,e,w;
}Mw;
Mw mw[2010];
int cmp(Mw A,Mw B)
{
	return A.s<B.s;
}
int cmp2(Mw A,Mw B)
{
	return A.w<B.w;
}
int main()
{
	int test,T,i,j,n2;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&test);
	for(T=1;T<=test;T++)
	{
		scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
		for(i=0;i<n;i++)
		{
			scanf("%d%d%d",&mw[i].s,&mw[i].e,&mw[i].w);
			mw[i].w+=s;
		}
		sort(mw,mw+n,cmp);
		r-=s;
		j=0;
		n2=n;
		for(i=0;i<n;i++)
		{
			if(mw[i].s>j)
			{
				mw[n2].s=j;
				mw[n2].e=mw[i].s;
				mw[n2++].w=s;
			}
			j=mw[i].e;
		}
		if(j<x)
		{
			mw[n2].s=j;
			mw[n2].e=x;
			mw[n2++].w=s;
		}
		n=n2;
		sort(mw,mw+n,cmp2);
		double sum=0,ct,tt,l;
		tt=t;
		for(i=0;i<n;i++)
		{
			l=mw[i].e-mw[i].s;
			if(tt==0)
			{
				sum+=l/mw[i].w;
			}
			else
			{
				ct=1.0*l/(mw[i].w+r);
				if(ct>=tt)
				{
					sum+=tt;
					l-=(double)(mw[i].w+r)*tt;
					sum+=l/mw[i].w;
					tt=0;
				}
				else
				{
					tt-=ct;
					sum+=ct;
				}
			}
		}
		printf("Case #%d: %lf\n",T,sum);
	}
	return 0;
}
