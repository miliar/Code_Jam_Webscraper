#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>

using namespace std;

const int maxn=300;
const double zero(1e-8);

int pos[maxn],v[maxn],n,d;

struct rec
{
	double l,r;
	int v;
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
		a[i].v = v[i];
	}
	sort(a,a+n,cmp);
	double nowl = a[0].l;
	for (int i(0);i<n;i++)
	{
		nowl = max(nowl,a[i].l);
		if (nowl + (a[i].v-1) * d > a[i].r) return false;
		nowl = nowl + a[i].v * d;
	}
	return true;
}

int main()
{
      cout.setf(ios::showpoint);
	cout.precision(7); 
	cout.setf(ios::fixed);
	freopen("D:\\B-small-attempt0.in","r",stdin);
	freopen("D:\\out.txt","w",stdout);
	int tot;
	cin>>tot;
	for (int ca=1;ca<=tot;ca++)
	{
		cin>>n>>d;
		for (int i(0);i<n;i++)
			cin>>pos[i]>>v[i];
		
		double l=zero,r=1e10,M;
		while (r / l > 1 + zero)
		{
			M = (r + l) / 2;
			if (can(M)) r = M;
				else l = M;
		}
		cout<<"Case #"<<ca<<": "<<M<<endl;
	}
}
