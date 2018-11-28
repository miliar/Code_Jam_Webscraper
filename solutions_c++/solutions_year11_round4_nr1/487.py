#include <iostream>

using namespace std;

void swap(int &a, int &b)
{
	int t=a;
	a=b;
	b=t;
}

int x[10000],y[10000];

void qsort(int i,int j)
{
	int l=i,r=j,a=x[(i+j)/2];
	while (l<=r) {
		while (x[l]<a) l++;
		while (x[r]>a) r--;
		if (l<=r) {
			swap(x[l],x[r]);
			swap(y[l],y[r]);
			l++,r--;
		}
	}
	if (i<r) qsort(i,r);
	if (l<j) qsort(l,j);
}

int main()
{
	int t;
	cin >> t;
	int ca=0;
	while (++ca<=t) {
		int l,s,r,n;
		double tt;
		cin >> l >> s >> r >> tt >> n;
		r=r-s;
		int tot=0;
		int sum=l;
		for (int i=0;i<n;i++) {
			int st,en,w;
			cin >> st >> en >> w;
			if (en>l) en=l;
			if (st<l && en-st>0) {
				x[tot]=w+s;
				y[tot]=en-st;
				sum-=y[tot++];
			}
		}
		x[tot]=s;
		y[tot]=sum;
		qsort(0,tot);
		double ans=0;
		for (int i=0;i<=tot;i++) {
			double t1=y[i]/double(x[i]+r);
			double t2=y[i]/double(x[i]);
			if (tt>=t1) {
				ans+=t1;
				tt-=t1;
			} else if (tt==0) {
				ans+=t2;
			} else {
				double temp=tt*(x[i]+r);
				ans+=tt;
				tt=0;
				ans+=(y[i]-temp)/double(x[i]);
			}
		}
		printf("Case #%d: %0.8lf\n",ca,ans);
	}
}