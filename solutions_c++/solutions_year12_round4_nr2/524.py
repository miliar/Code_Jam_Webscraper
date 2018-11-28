#include <cstdio>
#include <cmath>
#include <algorithm>
const int N=1010;
int n,L,W;
struct unit{
	double r;
	int pos;
	bool operator<(const unit &A)const
	{return r>A.r;}
}t[N];
double X[N],Y[N],r[N];
double ansx[N],ansy[N];
inline int dis(double x,double y){return sqrt(x*x+y*y);}
bool ok(double x,double y,int p)
{
	for(int i=1;i<p;i++)
		if(dis(X[i]-x,Y[i]-y) < r[i]+r[p])return false;
	return true;
}
double bs(double x,int p)
{
	double low=0.0,up=L,mid;
	for(int z=1;z<=40;z++)
	{
		mid=(low+up)/2;
		if(!ok(x,mid,p))
			low=mid;
		else up=mid;
	}
	return up+0.05;
}
bool calc()
{
	for(int i=1;i<=n;i++)
		r[i]=t[i].r;
	int now=1;
	X[1]=0.0;Y[1]=0.0;
	double left=r[1];
	for(now=2;now<=n;now++)
	{
		if(left+r[now] <= W)
		{
			X[now]=left+r[now];
			Y[now]=0.0;
			left=X[now]+r[now];
		}
		else break;
	}
	bool from=1,OAO=false;
	double right=W;
	while(now<=n)
	{
		if(from==1)
		{
			X[now]=right;
			if(OAO)X[now]-=r[now];
			if(X[now]<0.0)
			{
				OAO=false;
				from=0;
				left=0.0;
				continue;
			}
			OAO=true;
			Y[now]=bs(X[now],now);
			if(Y[now]>=L)return false;
			right=X[now]-r[now];
			now++;
		}
		else
		{
			X[now]=left;
			if(OAO)X[now]+=r[now];
			if(X[now]>W)
			{
				OAO=false;
				from=1;
				right=W;
				continue;
			}
			OAO=true;
			Y[now]=bs(X[now],now);
			if(Y[now]>=L)return false;
			left=X[now]+r[now];
			now++;
		}
	}
	return true;
}
int main()
{
	int T,w=1;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d%d",&n,&W,&L);
		for(int i=1;i<=n;i++)
		{
			scanf("%lf",&t[i].r);
			t[i].pos=i;
		}
		std::sort(t+1,t+n+1);
		if(!calc())while(1);
		for(int i=1;i<=n;i++)
		{
			ansx[t[i].pos]=X[i];
			ansy[t[i].pos]=Y[i];
		}
		for(int i=1;i<=n;i++)
			if(X[i]<0.0||X[i]>W||Y[i]<0.0||Y[i]>L)while(1);
		for(int i=1;i<=n;i++)
			for(int j=i+1;j<=n;j++)
				if(dis(X[i]-X[j],Y[i]-Y[j])<r[i]+r[j])
					while(1);
		printf("Case #%d:",w++);
		for(int i=1;i<=n;i++)
			printf(" %lf %lf",ansx[i],ansy[i]);
		puts("");
	}
}
