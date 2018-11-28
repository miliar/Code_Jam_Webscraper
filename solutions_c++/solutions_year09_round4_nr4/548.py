#include<iostream>
#include<math.h>
#include<algorithm>
using namespace std;
struct pt
{
	int x,y;
};
float dist(pt A,pt B)
{
	int dx=A.x-B.x;
	int dy=A.y-B.y;
	return sqrt(dx*dx+dy*dy);
}
int main()
{
	int c,n,p,i;
	float ans,mini;
	scanf("%d",&c);
	for(p=1;p<=c;p++)
	{
		scanf("%d",&n);
		pt a[3];
		int r[3];
		for(i=0;i<n;i++)
		{
			scanf("%d%d%d",&a[i].x,&a[i].y,&r[i]);
		}
		if(n==1)
		{
			ans=r[0];
		}
		else if(n==2)
		{
			mini=max(r[0],r[1]);
			ans=mini;
		}
		else if(n==3)
		{
			
			mini=max((double)(dist(a[0],a[1])+r[0]+r[1])/2.0,(double)r[2]);
			mini=min((double)mini,(double)max((double)(dist(a[0],a[2])+r[0]+r[2])/2.0,(double)r[1]));
			mini=min((double)mini,(double)max((double)(dist(a[1],a[2])+r[1]+r[2])/2.0,(double)r[0]));
			ans=mini;
		}
		printf("Case #%d: %.6f\n",p,ans);
	}
}