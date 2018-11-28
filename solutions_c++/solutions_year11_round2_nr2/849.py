#include<stdio.h>
#include<stdlib.h>
#include<memory.h>
#include<iostream>
#include<memory.h>
#include<memory>
#include<algorithm>
using namespace std;
int p[1000010];
int main()
{
	freopen("B-small-attempt0.in","r",stdin); 
	freopen("B.txt","w",stdout);
	int cas=0;
	scanf("%d",&cas);
	for(int ca=1;ca<=cas;ca++)
	{
		int n,c,d,pp,v;
		double ans;
		memset(p,sizeof(p),0);
		scanf("%d %d",&c,&d);
		int num=0;
		for(int i=0;i<c;i++)
		{
			scanf("%d %d",&pp,&v);
			for(int j=0;j<v;j++)
				p[num++]=pp;
		}
		sort(p,p+num);
		double l,r,m;
		l=0.0;
		r=10000000.0;;
		while(r-l>1e-7)
		{
			m=(l+r)/2;
			bool ok=true;
			double last=p[0]-m;
			double cur,tmp;
			
			for(int i=1;i<num;i++)
			{
				cur=last+d;
				if(cur<p[i])
				{
					if(m<p[i]-cur)tmp=m;
					else tmp=p[i]-cur;
					last=p[i]-tmp;
				}
				else
				{
					if(cur>p[i]+m){ ok=false; break;}
					last=cur;
				}
			}	
			if(ok==true) r=m;
			else l=m;
		}
cout<<"Case #"<<ca<<": ";
printf("%.7lf\n",r);
	}
	return 0;
}
