#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>

using namespace std;

const int maxn(205);
const double zero(1e-8);

int pos[maxn],num[maxn],n,d;

struct rec
{
	double l,r;
	int num;
} a[maxn];

bool cmp(const rec &a,const rec &b)
{
	return a.l < b.l;
}

bool can(double t)
{
	for (int i(0);i<n;i++)
	{
		a[i].l = pos[i] - t;
		a[i].r = pos[i] + t;
		a[i].num = num[i];
		/*if (t < 0.5)
		{
			cout<<a[i].l << " " << a[i].r << " "<< a[i].num << endl;
			
		}*/
	}
	/*if (t < 0.5)
		cout<<endl<<endl;*/
	sort(a,a+n,cmp);
	double nowl = a[0].l;
	for (int i(0);i<n;i++)
	{
		nowl = max(nowl,a[i].l);
		if (nowl + (a[i].num-1) * d > a[i].r) return false;
		nowl = nowl + a[i].num * d;
	}
	return true;
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int task;
	scanf("%d",&task);
	for (int cases(1);cases<=task;cases++)
	{
		scanf("%d %d",&n,&d);
		for (int i(0);i<n;i++)
			scanf("%d %d",&pos[i],&num[i]);
		
		double L(0),R(1000000000),M;
		R = R * R;
		while (R - L > zero)
		{
			M = (R + L) / 2;
			if (can(M)) R = M;
				else L = M;
		}
		M = M + zero;
		printf("Case #%d: %.8lf\n",cases,M);
	}
	return 0;
}
