#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <cmath>
#include <algorithm>
using namespace std;

int n,k,sn;
vector<int> sts[110],st[110];
char g[110][110];
double x[50],y[50],r[50];
double sqr(double z)
{
	return z*z;
}
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,ca,i,j,a,b,c;
	double t,t1,ans,pi=acos(-1.0);
	scanf("%d",&T);
	for (ca = 1 ; ca <= T ; ca++)
	{
		scanf("%d",&n);
		for (i = 0 ; i < n ; i++)
		{
			scanf("%lf%lf%lf",&x[i],&y[i],&r[i]);
		}
		if(n==1)
		{
			ans = r[0];
		}
		if(n==2)
		{
			if(r[0]<r[1])ans=r[1];
			else ans = r[0];
		}
		if(n==3)
		{

			a = 0; b=1; c=2;
			t=r[a];
			t1=(sqrt(sqr(x[b]-x[c])+sqr(y[b]-y[c]))+r[b]+r[c])/2.0;
			if(t<t1)t=t1;
			ans = t;


			a = 1; b=0; c=2;
			t=r[a];
			t1=(sqrt(sqr(x[b]-x[c])+sqr(y[b]-y[c]))+r[b]+r[c])/2.0;
			if(t<t1)t=t1;
			if(ans>t)ans = t;


			a = 2; b=1; c=0;
			t=r[a];
			t1=(sqrt(sqr(x[b]-x[c])+sqr(y[b]-y[c]))+r[b]+r[c])/2.0;
			if(t<t1)t=t1;
			if(ans>t)ans = t;
		}

		printf("Case #%d: %lf\n",ca,ans);
	}

	return 0;
}
