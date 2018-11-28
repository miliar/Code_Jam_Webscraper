#include "stdio.h"
#include "string.h"
#include "math.h"
#include <algorithm>
using namespace std;
#define M 110

bool notp[M];//素数判定
int pr[110000],pn,ans;//pr存放素数,pn当前素数个数。
void getprime()
{
	pn=0;
	memset(notp,0,sizeof(notp));
	for(int i=2;i<M;i++) 
	{
		if(!notp[i])
			pr[pn++]=i;
		for(int j=0;j<pn && pr[j]*i<M;j++) 
		{
			notp[pr[j]*i]=1;
			if(i%pr[j]==0)break;
		}
	}
	//pr[pn++]=M;
}

struct point
{
	double x,y;
}all[M*2],ap[M*2];

int w,l,u,g;
int apn;

double polyArea(){
	double res=0; all[u+l]=all[0];
	for(int i=0;i<u+l;i++) res+=all[i].x*all[i+1].y - all[i].y*all[i+1].x ;
	if(res<0)
		return -res/2.0;
	else
		return (res)/2.0;
}

double poly(){
	double res=0; ap[apn]=ap[0];
	for(int i=0;i<apn;i++) res+=ap[i].x*ap[i+1].y - ap[i].y*ap[i+1].x ;
	if(res<0)
		return -res/2.0;
	else
		return (res)/2.0;
}


int main()
{
	int i,j,k,t,tc=1;
	double ans;
	int pu,pl;
	double low,high,mid;
	freopen("gcj/2011.6.11/A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	//getprime();
	while(t--)
	{
		printf("Case #%d: \n", tc++);
		scanf("%d%d%d%d",&w,&l,&u,&g);
		ans=0;
		for(i=0;i<l;i++)
		{
			scanf("%lf%lf",&all[i].x,&all[i].y);
		}
		for(i=0;i<u;i++)
			scanf("%lf%lf",&all[u+l-1-i].x,&all[u+l-1-i].y);
		ans=polyArea();
		ans/=g;
		low=0;high=w;
		if(g==2)
		{
			while(low<high-0.0000001)
			{
				mid=(low+high)/2;
				apn=0;
				for(i=0;all[i].x<=mid;i++)
					ap[apn++]=all[i];
				if(all[i].x>mid)
				{
					ap[apn].x=mid;
					ap[apn].y=all[i].y-(all[i].x-mid)*(all[i].y-all[i-1].y)/(all[i].x-all[i-1].x);
					apn++;
				}
				while(all[i].x>mid) i++;
				if(all[i].x<mid)
				{
					ap[apn].x=mid;
					ap[apn].y=all[i].y-(all[i].x-mid)*(all[i].y-all[i-1].y)/(all[i].x-all[i-1].x);
					apn++;
				}
				for(;i<u+l;i++)
					ap[apn++]=all[i];
				if(poly()>ans)
					high=mid;
				else
					low=mid;
			}
			printf("%.6lf\n",(low+high)/2);
		}
		else
		{
			while(low<high-0.0000001)
			{
				mid=(low+high)/2;
				apn=0;
				for(i=0;all[i].x<=mid;i++)
					ap[apn++]=all[i];
				if(all[i].x>mid)
				{
					ap[apn].x=mid;
					ap[apn].y=all[i].y-(all[i].x-mid)*(all[i].y-all[i-1].y)/(all[i].x-all[i-1].x);
					apn++;
				}
				while(all[i].x>mid) i++;
				if(all[i].x<mid)
				{
					ap[apn].x=mid;
					ap[apn].y=all[i].y-(all[i].x-mid)*(all[i].y-all[i-1].y)/(all[i].x-all[i-1].x);
					apn++;
				}
				for(;i<u+l;i++)
					ap[apn++]=all[i];
				if(poly()>ans)
					high=mid;
				else
					low=mid;
			}
			printf("%.6lf\n",(low+high)/2);

			low=(low+high)/2;high=w;
			while(low<high-0.0000001)
			{
				mid=(low+high)/2;
				apn=0;
				for(i=0;all[i].x<mid;i++);
				if(all[i].x>mid)
				{
					ap[apn].x=mid;
					ap[apn].y=all[i].y-(all[i].x-mid)*(all[i].y-all[i-1].y)/(all[i].x-all[i-1].x);
					apn++;
				}
				while(all[i].x>=mid)
				{ 
					ap[apn++]=all[i];i++;
				}
				if(all[i].x<mid)
				{
					ap[apn].x=mid;
					ap[apn].y=all[i].y-(all[i].x-mid)*(all[i].y-all[i-1].y)/(all[i].x-all[i-1].x);
					apn++;
				}
				if(poly()<ans)
					high=mid;
				else
					low=mid;
			}
			printf("%.6lf\n",(low+high)/2);
		}
	}
	return 0;
}

/*
2
15 3 3 3
0 6
10 8
15 9
0 10
5 11
15 13
8 3 4 2
0 2
5 4
8 3
0 5
3 4
4 7
8 5
*/

