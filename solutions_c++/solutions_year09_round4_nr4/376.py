#include<map>
#include<cmath>
#include<cstdio>
#include<vector>
#include<string>
#include<cstdlib>
#include<algorithm>

#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)

using namespace std;

struct circle
{
	double x, y, r;
}c[40];

double dis(circle a, circle b)
{
	return sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y))+a.r+b.r;
}

int main()
{
	int T, cas, ans;
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	scanf("%d", &T);
	rep(cas,T)
	{
		int n;
		scanf("%d", &n);
		for(int i = 0; i < n; i ++)
		{
			scanf("%lf %lf %lf", &c[i].x, &c[i].y, &c[i].r);
		}
		double ans;
		if(n == 1){
			ans = c[0].r;
		}
		if(n == 2){
			ans = c[0].r;
			ans >?= c[1].r;
		}
		if(n == 3){
			double r1, r2, r3;
			r1 = dis(c[0], c[1])/2.0;
			r1 >?= c[2].r;
			r2 = dis(c[0], c[2])/2.0;
			r2 >?= c[1].r;
			r3 = dis(c[2], c[1])/2.0;
			r3 >?= c[0].r;
			ans = r1;
			ans <?= r2;
			ans <?= r3;
		}
		printf("Case #%d: %lf\n", cas+1, ans);
	}
	return 0;
}
