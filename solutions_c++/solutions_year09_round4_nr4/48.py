#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
#define sqr(x) ((x)*(x))
#define maxn 50
#define inf 1e4
#define eps 1e-7

struct node
{
	int x,y,r;
}C[maxn],c[maxn];
int N,n;
double ans;

inline double dist(double a,double b,double x,double y)
{
	return sqrt(sqr(x-a)+sqr(y-b));
}

inline int Triangle(double a,double b,double c)
{
	if (a>b) swap(a,b);
	if (b>c) swap(b,c);
	if (a+b>c+eps) return 1;
	if (fabs(a+b-c)<=eps) return 0;
	return -1;
}

inline bool Check(double ox,double oy,double R)
{
	for (int i=0;i<n;++i)
	if (dist(ox,oy,c[i].x,c[i].y)+c[i].r>R+eps)
		return false;
	return true;
}

inline bool check(double ox,double oy,double R)
{
	n=0;
	for (int i=0;i<N;++i)
	if (dist(ox,oy,C[i].x,C[i].y)+C[i].r>R+eps)
		c[n++]=C[i];
	
	if (n==0) return true;
	else if (n==1) return c[0].r<=R;
	else
	{
		double oox,ooy;
		for (int i=0;i<n;++i)
		for (int j=i+1;j<n;++j)
		{
			double a=R-c[i].r,b=dist(c[i].x,c[i].y,c[j].x,c[j].y),cc=R-c[j].r;
			int t=Triangle(a,b,cc);
			if (t==-1) continue;
			if (t==0)
			{
				oox=c[i].x+(c[j].x-c[i].x)/b*a,ooy=c[i].y+(c[j].y-c[i].y)/b*a;
				if (Check(oox,ooy,R)) return true;
			}else
			{
				double cosa=(sqr(a)+sqr(b)-sqr(cc))/2.0/a/b,sina=sqrt(1-sqr(cosa));
				double dx=(c[j].x-c[i].x)/b*a,dy=(c[j].y-c[i].y)/b*a;
				double tx=dx,ty=dy;
				dx=tx*cosa-ty*sina;
				dy=tx*sina+ty*cosa;
				oox=c[i].x+dx,ooy=c[i].y+dy;
				if (Check(oox,ooy,R)) return true;
				
				sina=-sina;
				dx=(c[j].x-c[i].x)/b*a,dy=(c[j].y-c[i].y)/b*a;
				tx=dx,ty=dy;
				dx=tx*cosa-ty*sina;
				dy=tx*sina+ty*cosa;
				oox=c[i].x+dx,ooy=c[i].y+dy;
				if (Check(oox,ooy,R)) return true;
			}
		}
		return false;
	}
}

inline bool solve(double R)
{
	for (int i=0;i<N;++i)
		for (int j=i+1;j<N;++j)
		{
			double ox,oy;
			double a=R-C[i].r,b=dist(C[i].x,C[i].y,C[j].x,C[j].y),c=R-C[j].r;
			int t=Triangle(a,b,c);
			if (t==-1) continue;
			if (t==0)
			{
				ox=C[i].x+(C[j].x-C[i].x)/b*a,oy=C[i].y+(C[j].y-C[i].y)/b*a;
				if (check(ox,oy,R)) return true;
			}else
			{
				double cosa=(sqr(a)+sqr(b)-sqr(c))/2.0/a/b,sina=sqrt(1-sqr(cosa));
				double dx=(C[j].x-C[i].x)/b*a,dy=(C[j].y-C[i].y)/b*a;
				double tx=dx,ty=dy;
				dx=tx*cosa-ty*sina;
				dy=tx*sina+ty*cosa;
				ox=C[i].x+dx,oy=C[i].y+dy;
				if (check(ox,oy,R)) return true;
				
				sina=-sina;
				dx=(C[j].x-C[i].x)/b*a,dy=(C[j].y-C[i].y)/b*a;
				tx=dx,ty=dy;
				dx=tx*cosa-ty*sina;
				dy=tx*sina+ty*cosa;
				ox=C[i].x+dx,oy=C[i].y+dy;
				if (check(ox,oy,R)) return true;
			}
		}
	return false;
}

int main()
{
	freopen("D_large.in","r",stdin);
	freopen("D_large.out","w",stdout);
	
	int T,test=1;
	for (scanf("%d",&T);test<=T;++test)
	{
		ans=inf;
		scanf("%d",&N);
		for (int i=0;i<N;++i)
			scanf("%d%d%d",&C[i].x,&C[i].y,&C[i].r);
		if (N==1) ans=C[0].r;
		else if (N==2)
		{
			ans=max(C[0].r,C[1].r);
		}else if (N==3)
		{
			for (int i=0;i<N;++i)
				for (int j=i+1;j<N;++j)
				{
					double t=(dist(C[i].x,C[i].y,C[j].x,C[j].y)+C[i].r+C[j].r)/2.0;
					if (C[3-i-j].r>t) t=C[3-i-j].r;
					if (t<ans) ans=t;
				}
		}else
		{
			double l=0,r=inf;
			while (l+eps<r)
			{
				double mid=(l+r)/2.0;
				if (solve(mid)) r=mid;
				else l=mid;
//				printf("%lf\n",mid);
			}
			ans=r;
		}
		
		printf("Case #%d: %.7lf\n",test,ans);
	}
	
//	printf("%lf\n",(double)clock()/CLOCKS_PER_SEC);
	
	return 0;
}
