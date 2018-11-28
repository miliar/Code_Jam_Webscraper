#include<iostream>
#include<cmath>
#include<cstdio>
using namespace std;
struct bb
{
	double x,y,r;
}c[10];
double dis (bb a,bb b)
{
	return sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));
}
int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	double ma1,ma2,ma3,ans;
	int cs,kk,i,n;
	cin>>cs;
	for (kk=1;kk<=cs;kk++)
	{
		cin>>n;
		for (i=1;i<=n;i++)
			cin>>c[i].x>>c[i].y>>c[i].r;
		if (n==1) printf("Case #%d: %.6lf\n",kk,c[1].r);
		if (n==2) 
		{
			if (c[1].r>c[2].r) printf("Case #%d: %.6lf\n",kk,c[1].r);
			else printf("Case #%d: %.6lf\n",kk,c[2].r);
		}
		if (n==3)
		{
			if ( (dis(c[1],c[2])+c[1].r+c[2].r)/2 > c[3].r) ma1=(dis(c[1],c[2])+c[1].r+c[2].r)/2;
			else ma1=c[3].r;
			if ( (dis(c[1],c[3])+c[1].r+c[3].r)/2 > c[2].r) ma2=(dis(c[1],c[3])+c[1].r+c[3].r)/2;
			else ma2=c[2].r;
			if ( (dis(c[2],c[3])+c[2].r+c[3].r)/2 > c[1].r) ma3=(dis(c[2],c[3])+c[2].r+c[3].r)/2;
			else ma3=c[1].r;
			ans=min(ma1,ma2);
			ans=min(ans,ma3);
			printf("Case #%d: %.6lf\n",kk,ans);
		}
	}
	return 0;
}
