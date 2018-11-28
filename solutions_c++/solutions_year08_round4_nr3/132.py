#include <stdio.h>
#include <math.h>

#define N 1001

struct Node 
{
	double x,y,z,p;
};

Node A[N];
Node cur;
double deta;
int n;

double dist(Node s)
{
	int i;
	double re;
	re=0;
	for(i=0;i<n;i++) re>?=(fabs(s.x-A[i].x)+fabs(s.y-A[i].y)+fabs(s.z-A[i].z))/A[i].p;
	
		//re+=sqrt((s.x-A[i].x)*(s.x-A[i].x)+(s.y-A[i].y)*(s.y-A[i].y)+(s.z-A[i].z)*(s.z-A[i].z));
	return re;
}
void sol()
{
	double curdist,dd;
	bool f;
	Node tt;

	f=1;
	curdist=dist(cur);
	tt=cur;
	while(cur.x<=1000000)
	{
		tt.x=cur.x+deta;
		dd=dist(tt);
		if(dd<curdist)
		{
			curdist=dd;
			cur=tt;
			f=0;
		}
		else
			break;
	}
	tt=cur;
	while(cur.x>=0)
	{
		tt.x=cur.x-deta;
		dd=dist(tt);
		if(dd<curdist)
		{
			curdist=dd;
			cur=tt;
			f=0;
		}
		else
			break;
	}
	tt=cur;
	while(cur.y<=1000000)
	{
		tt.y=cur.y+deta;
		dd=dist(tt);
		if(dd<curdist)
		{
			curdist=dd;
			cur=tt;
			f=0;
		}
		else
			break;
	}
	tt=cur;
	while(cur.y>=0)
	{
		tt.y=cur.y-deta;
		dd=dist(tt);
		if(dd<curdist)
		{
			curdist=dd;
			cur=tt;
			f=0;
		}
		else
			break;
	}
	tt=cur;
	while(cur.z<=1000000)
	{
		tt.z=cur.z+deta;
		dd=dist(tt);
		if(dd<curdist)
		{
			curdist=dd;
			cur=tt;
			f=0;
		}
		else
			break;
	}
	tt=cur;
	while(cur.z>=0)
	{
		tt.z=cur.z-deta;
		dd=dist(tt);
		if(dd<curdist)
		{
			curdist=dd;
			cur=tt;
			f=0;
		}
		else
			break;
	}
	tt=cur;
	while(cur.z<=1000000&&cur.y<=1000000)
	{
		tt.z=cur.z+deta;
		tt.y=cur.y+deta;
		dd=dist(tt);
		if(dd<curdist)
		{
			curdist=dd;
			cur=tt;
			f=0;
		}
		else
			break;
	}
	tt=cur;
	while(cur.z>=0&&cur.y>=0)
	{
		tt.z=cur.z-deta;
		tt.y=cur.y-deta;
		dd=dist(tt);
		if(dd<curdist)
		{
			curdist=dd;
			cur=tt;
			f=0;
		}
		else
			break;
	}
	while(cur.z<=1000000&&cur.x<=1000000)
	{
		tt.z=cur.z+deta;
		tt.x=cur.x+deta;
		dd=dist(tt);
		if(dd<curdist)
		{
			curdist=dd;
			cur=tt;
			f=0;
		}
		else
			break;
	}
	tt=cur;
	while(cur.z>=0&&cur.x>=0)
	{
		tt.z=cur.z-deta;
		tt.x=cur.x-deta;
		dd=dist(tt);
		if(dd<curdist)
		{
			curdist=dd;
			cur=tt;
			f=0;
		}
		else
			break;
	}
	while(cur.x<=1000000&&cur.y<=1000000)
	{
		tt.x=cur.x+deta;
		tt.y=cur.y+deta;
		dd=dist(tt);
		if(dd<curdist)
		{
			curdist=dd;
			cur=tt;
			f=0;
		}
		else
			break;
	}
	tt=cur;
	while(cur.x>=0&&cur.y>=0)
	{
		tt.x=cur.x-deta;
		tt.y=cur.y-deta;
		dd=dist(tt);
		if(dd<curdist)
		{
			curdist=dd;
			cur=tt;
			f=0;
		}
		else
			break;
	}
	if(!f)
		sol();
}
int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small.out","w",stdout);
	int cas,ic,i;
	scanf("%d",&cas);
	for(ic=1;ic<=cas;ic++)
	{
        scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%lf%lf%lf%lf",&A[i].x,&A[i].y,&A[i].z,&A[i].p);
			/*A[i].x*=1000;
			A[i].y*=1000;
			A[i].z*=1000;*/
		}
		cur.x=cur.y=cur.z=0;
		for(deta=1;deta>1e-18;deta/=10)
			sol();
		/*printf("%lf %lf %lf\n",cur.x,cur.y,cur.z);
		cur.x=2;
		cur.y=2;
        cur.z=2;*/
		printf("Case #%d: %lf\n",ic,dist(cur));
	}
	return 0;
}
