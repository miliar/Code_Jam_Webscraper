#include <iostream>
#include <string>
#include <cstring>
#include <string.h>
#include <set>
#include <map>
#include <vector>

using namespace std;

int n;
double x[300];
int cnt[300];
int v=0;
double d;
int c;

int solve(double t){
	double curl=-1e15;
	for (int i=0; i<c; i++){
		double lf=x[i]-t, rt=x[i]+t;
		if (lf<curl) lf=curl;
		double tk=lf+(cnt[i]-1.0)*d;
		if (tk<rt+1e-9){
			curl=tk+d;
		} else
			return 0;
	}
	return 1;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;

	scanf("%d\n",&tests);
	for (int tt=1; tt<=tests; tt++){
		printf("Case #%d: ",tt);
		scanf("%d%lf",&c,&d);
		v=0;
		for (int i=0; i<c; i++){
			double p;
			int y;
			scanf("%lf%d",&p,&y);
			x[i]=p, cnt[i]=y;
		}

		double l=0, r=1e13;

		for (int k=0; k<100; k++){
			double key=(r+l)/2;

			if (solve(key)) r=key; else l=key;
		}
		printf("%.10lf\n",l);
	}

	return 0;
}