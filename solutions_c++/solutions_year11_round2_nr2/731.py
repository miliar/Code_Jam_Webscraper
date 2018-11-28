#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
struct Po
{
	int p,v;
} a[300];
int t,n,c,d;

bool cmp(Po p,Po q)
{
	return (p.p<q.p);
}

bool pass(double k)
{
	bool b=true;
	double s=-k;
	for (int i=1;i<=c;i++)
	{
		s+=(a[i].v-1)*d;
		if (s>k) return false;
		if (i<c)
		{
			b=false;
			s=s-(a[i+1].p-a[i].p)+d;
			if (s<-k)
			{
				b=true;
				s=-k;
			}
		}
	}
	return true;
}

double bin(double p,double q)
{
	double mid=(p+q)/2;
	if (q-p<1e-8)
		return mid;
	if (pass(mid))
		return bin(p,mid);
	else return bin(mid,q);
}

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&t);
	for (int tt=1;tt<=t;tt++)
	{
		scanf("%d%d",&c,&d);
		for (int i=1;i<=c;i++)
			scanf("%d%d",&a[i].p,&a[i].v);
		sort(a+1,a+c+1,cmp);
		double ans=bin(0,1e13);
		printf("Case #%d: %.7lf\n",tt,ans);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}