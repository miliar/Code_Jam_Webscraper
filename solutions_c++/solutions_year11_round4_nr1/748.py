#include<iostream>
#include<algorithm>
#include<queue>
#include<vector>
using namespace std;
struct dd{
	int l,v;
	double t;
}a[3005],b[3005]; 
bool cmp(dd a,dd b)
{
	return a.v<b.v ;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	int ca,i,s,r,t,x,n,v,st,end,j;
	double temp;
	scanf("%d",&ca);
	for(i=1;i<=ca;i++)
	{
		scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
		if(n==0)
		{
			printf("Case #%d: %.6lf",i,x*1.0/s);
			continue;
		}
		double length=0;
		for(j=0;j<n;j++)
		{
			scanf("%d%d%d",&st,&end,&v);
			length+=end-st;
			a[j].l=end-st;
			a[j].v=v+s;
			a[j].t=a[j].l*1.0/a[j].v;
		} 
		a[j].l=x-length;
		a[j].v=s;
		a[j].t=a[j].l*1.0/a[j].v;
		j++;
		sort(a,a+j,cmp);
	//	for(j=0;j<=n;j++)
	//	cout<<a[j].l<<"~"<<a[j].v<<"~"<<a[j].t<<endl;
		double ans=0;
		double all=t;
		for(j=0;j<=n;j++)
		{
			if(all>0)
			{
				temp=a[j].l*1.0/(a[j].v+r-s);
				if(temp<=all)
				{
					ans+=temp;
					all-=temp;
				}
				else
				{
					ans+=all+(a[j].l-all*(a[j].v+r-s))*1.0/a[j].v;
					all=0;
				}
			}else
			{
				ans+=a[j].t;
			}
		}
		printf("Case #%d: %.6lf\n",i,ans);
		/*start=0;
		y=0;
		for(j=0;j<n;)
		{
			if(a[j].s<=start)
			{
				b[y]=a[j];
				start=a[j].e;
				j++;
				y++;
			}else
			{
				b[y].s=start;
				b[y].e=a[j].s;
				b[y].v=s;
				start=b[y].e;
				y++;
			}
		}
		if(b[y-1].e<x)
		{
			b[y].s=b[y-1].e;
			b[y].e=x;
			b[y].v=s;
			y++;
		}*/
		//printf("Case #%d: ",i);
	}
	return 0;
} 
