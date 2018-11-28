#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
using namespace std;
const int MAXN =1050;
int cases;
struct Tline{
	double f,r,d,len;
}l[MAXN];
bool cmp(const Tline&a,const Tline&b)
{
	return a.d<b.d;
}
double len,sw,sr;
int n;
double tr;
int main()
{
	scanf("%d",&cases);
	for (int tcase=1;tcase<=cases;tcase++)
	{
		scanf("%lf%lf%lf%lf%d",&len,&sw,&sr,&tr,&n);
		for (int i=1;i<=n;i++)
		{
			scanf("%lf%lf%lf",&l[i].f,&l[i].r,&l[i].d);
			l[i].len=l[i].r-l[i].f;
			len -= l[i].len;
		}
		n++;
		l[0].len=len; l[0].d=0;
		sort(l,l+n,cmp);
		double ans=0;
		for (int i=0;i<n;i++)
		{
			if (tr>0)
			{
				double t=min(l[i].len/(l[i].d+sr),tr);
				ans += t;
				tr -= t;
				l[i].len -= t*(l[i].d+sr);
			}
			if (l[i].len>0)
			{
				ans+=l[i].len/(l[i].d+sw);
			}
		}
		printf("Case #%d: %.10f\n",tcase,ans);
	}
	return 0;
}
