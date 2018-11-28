#include<iostream>
#include<cstring>
#include<cstdio>
#include<cmath>

using namespace std;
int c;
struct node
{
	double p;
	int v;
}a[5000];
double d;
bool aaa(double r)
{
	if (fabs(r)<0.0001) return true;
	else return false;
}
double Abs(double x)
{
	if (x<0) return -x;
	else return x;
}

double search(double l,double r)
{
	bool f;
	int i,j;
	if (aaa(l-r)) return -1;
	double mid=(l+r)/2;
	double q=a[0].p-mid-d;
	f=true;
	for (i=0;i<c;i++)
	{
		for (j=1;j<=a[i].v;j++)
		{
			if (q+d-a[i].p>mid)
			{
				f=false;
				break;
			}
			q=q+d;
			if (q<a[i].p-mid)
				q=a[i].p-mid;
		}
		if (!f) break;
	}
	if (f)
	{
		double qq=search(l,mid-0.000001);
		if (qq==-1) return mid;
		else return qq;
	}
	else return search(mid+0.000001,r);

}

int main()
{
	int cas;
	int ca=0;
	int i,v;
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&cas);
	while (cas--)
	{
		v=0;
		scanf("%d%lf",&c,&d);
		//	cout<<c<<" "<<d<<endl;
		for (i=0;i<c;i++)
		{
			scanf("%lf%d",&a[i].p,&a[i].v);
			v+=a[i].v;
		}
		double l=0;
		double r=double(v)*d;
		ca++;
		printf("Case #%d: %.1lf\n",ca,search(0,r));

	}
return 0;
}