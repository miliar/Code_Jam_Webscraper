#include <iostream>
#include <algorithm>
using namespace std;
struct node
{
	double s,t;
	double v;
};

int cmp(node aa,node bb)
{
	return aa.s<bb.s;
}
int cmp2(node aa,node bb)
{
	return aa.v<bb.v;
}
node mm[1005];
node mm2[1005];
int main ()
{
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	double x,s,r,t;
	int cc,i,n;
	double last;
	int xxx=0;
	scanf("%d",&T);
	while(T--)
	{
		xxx++;
		scanf("%lf%lf%lf%lf%d",&x,&s,&r,&t,&n);
		for(i=0;i<n;i++)
		{
			scanf("%lf%lf%lf",&mm[i].s,&mm[i].t,&mm[i].v);
		}
		sort(mm,mm+n,cmp);
		cc=0;
		last=0;
		for(i=0;i<n;i++)
		{
			if(last<mm[i].s)
			{
				mm2[cc].s=last;
				mm2[cc].t=mm[i].s;
				last=mm[i].t;
				cc++;
			}
			else
			{
				last=mm[i].t;
			}
		}
		if(x>mm[n-1].t)
		{
			mm2[cc].s=mm[n-1].t;
			mm2[cc].t=x;
			cc++;
		}
		double t1,temp;
		t1=0;
		double templen;
		for(i=0;i<cc;i++)
		{
			temp=(mm2[i].t-mm2[i].s)/(r);
			if(temp<=t-t1)
			{
				t1+=temp;
			}
			else
			{
				if(t1>=t)
				{
					t1+=(mm2[i].t-mm2[i].s)/(s);
				}
				else
				{
					templen=(r)*(t-t1);
					t1=t+(mm2[i].t-mm2[i].s-templen)/s;
				}
			}
		}
		sort(mm,mm+n,cmp2);
		for(i=0;i<n;i++)
		{
			temp=(mm[i].t-mm[i].s)/(double)(r+mm[i].v);
			if(temp<=t-t1)
			{
				t1+=temp;
			}
			else
			{
				if(t1>=t)
				{
					t1+=(mm[i].t-mm[i].s)/(double)(s+mm[i].v);
				}
				else
				{
					templen=(double)(r+mm[i].v)*(t-t1);
					t1=t+(double)(mm[i].t-mm[i].s-templen)/(s+mm[i].v);
				}
			}
		}
		printf("Case #%d: ",xxx);
		printf("%lf\n",t1);
	}
}