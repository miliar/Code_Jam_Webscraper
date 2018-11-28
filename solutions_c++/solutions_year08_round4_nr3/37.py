#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

typedef long long LL;

int tc, ntc;
int n;
struct tt
{
	LL x[3];
	LL p;
};

tt ar[2000];
struct tt2
{
	LL v;
	LL p;
};
bool operator<(const tt2& a, const tt2& b)
{
	return a.v < b.v;
}

tt2 tar[2000];

bool ok1(int m, double r)
{
	int i, j;
	for (i=0; i<n; i++)
	{
		tar[i].v = 0;
		for (j=0; j<3; j++) 
			if (m&(1<<j)) 
				tar[i].v += ar[i].x[j];
			else
				tar[i].v -= ar[i].x[j];						
		tar[i].p = ar[i].p;
	}
	
		
	double p = -1e100;
	double q = 1e100;
	
	for (i=0; i<n; i++)
	{
		p >?= tar[i].v - tar[i].p * r;
		q <?= tar[i].v + tar[i].p * r;
	}
	
	return (p <= q);
}

bool ok(double r)
{
	int i;
	for (i=0; i<8; i++) if (!ok1(i,r)) return false;
	return true;
}

double solve()
{
	if (n == 1) return 0;
	
	double a, b, mid;
	a = 0;
	b = 1e8;
	int i;
	for (i=0; i<100; i++)
	{
		mid = (a+b)/2;
		if (ok(mid)) b = mid;
		else a = mid;		
	}
	
	return (a+b)/2;
}

int main()
{
	scanf("%d",&ntc);
	int i;
	double res;
	for (tc=1; tc<=ntc; tc++)
	{
		scanf("%d",&n);
		for (i=0; i<n; i++) 
			scanf("%lld %lld %lld %lld",&ar[i].x[0],&ar[i].x[1],&ar[i].x[2],&ar[i].p);
		
		res = solve();
		printf("Case #%d: %.10lf\n",tc,res);
	}
}