#include <iostream>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <map>
#include <string>
using namespace std;
typedef __int64 ll;
const int N=1100;
int T,x,s,r,n;
double t;
struct dor {
	int b,e,w;
	bool operator < (dor &d2) {
		if (b<d2.b) return 1;
		else return 0;
	}
} d[N];
struct sec {
	double l;
	int w;
	bool operator < (sec &d2) {
		if (w<d2.w) return 1;
		else return 0;
	}
} a[3*N];
int main () {
#ifndef ONLINE_JUDGE
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
#endif
	cin>>T;
	for (int test=0; test<T; test++) {
		cin>>x>>s>>r>>t>>n;
		for (int i=0; i<n; i++) scanf("%d%d%d",&d[i].b,&d[i].e,&d[i].w);
		sort(d,d+n);
		int cnt=0,compl=0;
		double curx=0;
		for (int i=0; i<n; i++) { 
			if (d[i].b!=curx) {
				if (d[i].b>x) {
					a[cnt].l=x-curx;
					a[cnt].w=s;
					cnt++;
					curx=x;
					compl=1;
					break;
				} else {
					a[cnt].l=d[i].b-curx;
					a[cnt].w=s;
					cnt++;
					curx=d[i].b;
				}
			}
			a[cnt].l=d[i].e-d[i].b;
			a[cnt].w=d[i].w+s;
			cnt++;
			curx=d[i].e;
			if (curx>x) {
				a[cnt-1].l=x-d[i].b;
				curx=x;
				compl=1;
				break;
			}
		}
		if (!compl) {
			a[cnt].l=x-curx;
			a[cnt].w=s;
			curx=x;
			cnt++;
		}
		sort(a,a+cnt);
		double ans=0;
		for (int i=0; i<cnt; i++)
			if (t>0) {
				double some=(double(a[i].l))/(a[i].w+r-s);
				if (some>t) {
					a[i].l-=(a[i].w+r-s)*t;
					ans+=t;
					t=0;
					ans+=(double(a[i].l))/(a[i].w);
				} else {
					t-=some;
					ans+=some;
				}
			} else {
				ans+=(double(a[i].l))/(a[i].w);
			}
			printf("Case #%d: %.19lf\n",test+1,ans);
	}
}