#include<iostream>
#include<algorithm>
using namespace std;
#define eps 1e-9
int sgn(const double &t)
{
	return t>eps?1:(t<-eps?-1:0);
}
struct node
{
	int s,e,w;
}a[3000];
bool cmp1(const node &aa,const node &bb)
{
	return aa.s<bb.s;
}
bool cmp2(const node &aa,const node &bb)
{
	return aa.w<bb.w;
}
int main()
{
	int cas,len,s,r,t,n,i,k,end;
	double t1,tmp,ans;
	//freopen("1.txt","r",stdin);
	//freopen("Al.in","r",stdin);
	//freopen("2.txt","w",stdout);
	scanf("%d",&cas);
	for(int ii=1;ii<=cas;ii++)
	{
		printf("Case #%d: ",ii);
		scanf("%d%d%d%d%d",&len,&s,&r,&t,&n);
		for(i=0;i<n;i++)
			scanf("%d%d%d",&a[i].s,&a[i].e,&a[i].w);
		k=n;
		sort(a,a+n,cmp1);
		end=0;
		i=0;
		while(i<n)
		{
			if(end<a[i].s)
			{
				a[k].s=end;a[k].e=a[i].s;a[k++].w=0;
			}
			end=a[i++].e;
		}
		if(a[n-1].e!=len)
		{
			a[k].s=a[n-1].e;a[k].e=len;a[k++].w=0;
		}
		sort(a,a+k,cmp2);
		bool flag=false;
		t1=0;
		for(i=0;i<k&&flag==false;i++)
		{
			tmp=t1+1.0*(a[i].e-a[i].s)/(a[i].w+r);
			if(sgn(tmp-t)>0)
			{
				flag=true;
				ans=t+(a[i].e-a[i].s-(t-t1)*(a[i].w+r))/(a[i].w+s);
			}
			else
				t1=tmp;
		}
		if(flag==false)
			ans=t1;
		while(i<k)
		{
			ans+=1.0*(a[i].e-a[i].s)/(a[i].w+s);
			i++;
		}
		printf("%.7lf\n",ans);
	}
	return 0;
}