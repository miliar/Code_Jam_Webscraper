#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <queue>
#include <sstream>
#include <iostream>
#include <math.h>
#include <stdio.h>

#define LL long long

using namespace std;

double dist(int x, int y, int x2, int y2) {
	return sqrt((double)(x-x2)*(x-x2)+(y-y2)*(y-y2));
}

bool eq(double a, double b) {
	return fabs(a-b)<1e-6;
}

int main() {
	freopen("B-small-attempt3.in","r",stdin);
	freopen("B-small-attempt3.out","w",stdout);
	int t,T;
	scanf("%d", &T);
	for (t=1; t<=T; t++) {
		int W,H,A;
		int x,y,x2,y2;
		scanf("%d %d %d", &W, &H, &A);
		if (A>W*H) {
			printf("Case #%d: IMPOSSIBLE\n",t);
			continue;
		}
		for (x=0; x<=W; x++) {
			for (y=0; y<=H; y++) {
				for (x2=0; x2<=W; x2++) {
					for (y2=0; y2<=H; y2++) {
						double a=dist(x,y,x2,y2);
						double b=dist(0,0,x,y);
						double c=dist(0,0,x2,y2);
						double s=(a+b+c)/2;
						double L=sqrt(s*(s-a)*(s-b)*(s-c));
						if (eq(L,(double)A/2)) {
							printf("Case #%d: %d %d %d %d %d %d\n",t,0,0,x,y,x2,y2);
							goto yy;
						}
					}
				}
			}
		}
		printf("Case #%d: IMPOSSIBLE\n",t);
		yy: ;

	}
	return 0;
}
