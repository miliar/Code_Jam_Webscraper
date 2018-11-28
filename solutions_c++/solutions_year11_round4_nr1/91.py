#include <stdio.h>
#include <algorithm>
#define MAXN 1050

class Belt {
	public:
		double l,v;
		Belt() {}
		Belt(double li,double vi):l(li),v(vi) {}
		const bool operator<(const Belt &b) const { return v<b.v; }
};

int n;
double len,ws,rs,rt,rem;
//double bl[MAXN],bv[MAXN];
Belt blt[MAXN];

inline double min(double a,double b) { return a<b?a:b; }

inline double solve() {
	int i;
	double t1,t2,sol=0.0;
	std::sort(blt,blt+n);
	for(i=0;i<n;i++) {
		t1=min(rt,blt[i].l/(blt[i].v+rs));
		t2=(blt[i].l-(blt[i].v+rs)*t1)/(blt[i].v+ws);
//		printf("<%.3lf %.3lf> %.3lf %.3lf\n",bl[i],bv[i],t1,t2);
		sol+=t1+t2;
		rt-=t1;
	}
	return sol;
}

int main(void)
{
	int t,casenum=1,i;
	double bs,be,bv;
	scanf("%d",&t);
	while(t--) {
		scanf("%lf%lf%lf%lf%d",&len,&ws,&rs,&rt,&n);
		rem=len;
		for(i=0;i<n;i++) {
			scanf("%lf%lf%lf",&bs,&be,&bv);
//			bl[i]=be-bs;
			blt[i]=Belt(be-bs,bv);
			rem-=blt[i].l;
		}
		blt[n++]=Belt(rem,0.0);
//		bl[n]=rem;
//		bv[n]=0;
//		n++;
		printf("Case #%d: %.9lf\n",casenum++,solve());
	}
}
