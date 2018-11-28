#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;
double b[1005],e[1004],w[1005];
struct Node {
	double d;
	int num;
	inline bool operator < (Node a) const {
		return num > a.num;
	}
};
Node p[304];
int main () {
	freopen ("A-large.in","r",stdin);
	freopen ("a-large.out","w",stdout);
	int t;
	scanf ("%d",&t);
	for (int ca = 1; ca<=t;ca++) {
		for (int i=1;i<=300;i++) {
			p[i].d = i;
			p[i].num = 0;
		}
		double x,s,r,t;
		int n;
		scanf ("%lf%lf%lf%lf%d",&x,&s,&r,&t,&n);
		p[int (s)].num = x;
		for (int i=1;i<=n;i++) {
			scanf ("%lf%lf%lf",&b[i],&e[i],&w[i]);
			p[int (w[i]+s)].num += e[i]-b[i];
			p[int (s)].num -= e[i]-b[i];
		}
		//sort (p+1,p+300);
		double left = t,ans=0;
		
		for (int i=1;i<=300;i++) {
			if (p[i].num == 0)continue;
			if (left * (p[i].d-s+r) >= double (p[i].num)) {
				double use =  (p[i].num)/(p[i].d-s+r);
				ans += use;
				left -= use;
			} else {
				ans += left;
				double mm = p[i].num;
				mm -= left * (p[i].d-s+r);
				ans += mm / (p[i].d);
				left = 0;
			}
		}
		printf ("Case #%d: %lf\n",ca,ans);
	}
	return 0;
}
