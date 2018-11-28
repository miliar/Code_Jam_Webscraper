#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<queue>
using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))

struct node {
	int x,y,z;
	int p;
}nd[15];

int n;

bool ok(double x) {
	int i,j;
	double d,d2;
	rep(i,n) for(j=i+1;j<n;j++) {
		d = fabs(nd[i].x - nd[j].x) + fabs(nd[i].y - nd[j].y) + fabs(nd[i].z - nd[j].z);
		d2 = (nd[i].p + nd[j].p) * x;
		if(d > d2 + 1e-10) return 0;
	}
	return 1;
}

int main() {
	double lo,hi,mid;
	int T,i,kase=1;
	scanf("%d",&T);
	while(T--) {
		scanf(" %d",&n);
		rep(i,n) {
			scanf(" %d %d %d %d",&nd[i].x,&nd[i].y,&nd[i].z,&nd[i].p);
		}

		lo = 0., hi = 1e10;

		while(fabs(hi-lo) > 1e-9) {
			mid = (lo + hi) * .5;
			if(ok(mid) ) hi = mid;
			else lo = mid;
		}

		printf("Case #%d: %.10lf\n",kase++,lo);
	}
	return 0;
}