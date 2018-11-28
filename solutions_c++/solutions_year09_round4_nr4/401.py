#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<vector>
#include<cstring>
using namespace std;
struct node{
	double x,y,r;
};
node p[50];
double dis(node l,node r)
{
	return sqrt((l.x-r.x)*(l.x-r.x)+(l.y-r.y)*(l.y-r.y));
}
int main(void)
{
	freopen("4.in","r",stdin);
	freopen("4.out","w",stdout);


	int tn;
	int cas=0;
	scanf("%d",&tn);
	while(tn--)
	{
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++)
		scanf("%lf%lf%lf",&p[i].x,&p[i].y,&p[i].r);
	printf("Case #%d: ",++cas);
	if(n==1)
		printf("%lf\n",p[0].r);
	else if(n==2)
		printf("%lf\n",max(p[0].r,p[1].r));
	else if(n==3)
	{
		double ans=1e45;
		double temp;
		double len;
		temp=0.0;
		len=dis(p[0],p[1]);
		temp+=max(len+p[0].r,p[1].r);
		temp+=max(len+p[1].r,p[0].r);
		temp-=len;
		ans=min(ans,max(temp/2.0,p[2].r));
		
		temp=0.0;
		len=dis(p[1],p[2]);
		temp+=max(len+p[1].r,p[2].r);
		temp+=max(len+p[2].r,p[1].r);
		temp-=len;
		ans=min(ans,max(temp/2.0,p[0].r));
		
		temp=0.0;
		len=dis(p[2],p[0]);
		temp+=max(len+p[2].r,p[0].r);
		temp+=max(len+p[0].r,p[2].r);
		temp-=len;
		ans=min(ans,max(temp/2.0,p[1].r));
		
		printf("%lf\n",ans);
	}
	}
	return 0;
}
