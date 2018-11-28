#include<stdio.h>
#include<math.h>
#include<algorithm>

using namespace std;

const int maxn = 50;
const double eps = 1e-7;

struct circle
{
	double x,y,r;
}p[maxn],c[maxn*maxn*maxn];

int ntest;
int n,cnt;
long long a[maxn];

double dist(circle a,circle b)
{
	a.x -= b.x; a.y -= b.y;
	return sqrt(a.x*a.x+a.y*a.y);
}

void getinfo()
{
	scanf("%d",&n);
	for(int i=0;i<n;i++)
		scanf("%lf%lf%lf",&p[i].x,&p[i].y,&p[i].r);
}

void getc(circle x)
{
	c[cnt++] = x;
}

void getc(circle x,circle y)
{
	double d = dist(x,y);
	double u = x.r - y.r;
	c[cnt].x = (x.x * (d+u) + y.x * (d-u)) / 2 / d;
	c[cnt].y = (x.y * (d+u) + y.y * (d-u)) / 2 / d;
	c[cnt].r = dist(c[cnt],x)+x.r;
	cnt++;
}

long long getm(circle x)
{
	long long res = 0;
	for(int i=0;i<n;i++)
		if(dist(p[i],x)<=x.r-p[i].r+eps)
			res |= (1ll<<i);

//	printf("%lf %lf %lf %I64d\n",x.x,x.y,x.r,res);
	return res;
}

void process(int test)
{
	cnt = 1;
	for(int i=0;i<n;i++) getc(p[i]);
	for(int i=0;i<n;i++) for(int j=i+1;j<n;j++) getc(p[i],p[j]);

	for(int i=0;i<cnt;i++)
		a[i] = getm(c[i]);

	double ans = 1e100;
	for(int i=0;i<cnt;i++)
		for(int j=i+1;j<cnt;j++)
			if((a[i]|a[j])==(1ll<<n)-1)
				ans = min(ans,max(c[i].r,c[j].r));
	
	printf("Case #%d: %.10lf\n",test,ans);
}

int main()
{
	scanf("%d",&ntest);
	for(int test=1;test<=ntest;test++)
	{
		getinfo();
		process(test);
	}
	return 0;
}

