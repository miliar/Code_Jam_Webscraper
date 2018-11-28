#include<iostream>
#include<cmath>
#include<vector>
#include<cstring>
#include<algorithm>
#include<stdio.h>
using namespace std;
struct A{double s,v;}a[1231223];
int pt(A&a,A&b)
{
	return a.v<b.v;
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,cas=1;
	cin>>t;
	while(t--)
	{
		double v1,v2,t,x;
		int n;
		cin>>x>>v1>>v2>>t>>n;
		for(int i=0;i<n;i++)
		{
			int xx,y,tt;
			scanf("%d%d%d",&xx,&y,&tt);
			a[i].s=y-xx;
			x-=a[i].s;
			a[i].v=tt;
		}
		a[n].s=x;
		a[n++].v=0;
		sort(a,a+n,pt);
		double da=0;
		for(int i=0;i<n;i++)
		{
			if(a[i].s/(a[i].v+v2)<t)
			{
				t-=a[i].s/(a[i].v+v2);
				da+=a[i].s/(a[i].v+v2);
			}
			else 
			{
				//cout<<a[i].s<<"  "<<a[i].v<<"   "<<t<<endl;
				
				a[i].s-=(a[i].v+v2)*t;
				//cout<<a[i].s<<"     "<<endl;
				da+=a[i].s/(a[i].v+v1)+t;t=0;
			}
		}
		printf("Case #%d: %.9lf\n",cas++,da);
	}
}