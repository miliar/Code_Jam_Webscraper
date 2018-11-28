#include <iostream>
#include <string>
#include <cstring>
#include <string.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;

struct corr{
	double s,f;
	double w;
};

double s,r;
double t;
double x;
int n;
corr c[3000];

int cmp(corr a,corr b){
	//return ((1/(a.w+r)-1/(a.w+s))<(1/(b.w+r)-(1/(b.w+s))));
	return a.w<b.w;
}

void solve(int tst){
	scanf("%lf%lf%lf%lf",&x,&s,&r,&t);
	scanf("%d",&n);
	double d=x;
	for (int i=0; i<n; i++){
		scanf("%lf%lf%lf",&c[i].s,&c[i].f,&c[i].w);
		d-=(c[i].f-c[i].s);
	}

	//sort(c,c+n,cmp);
	c[n].s=0, c[n].f=d, c[n].w=0;
	sort(c,c+n+1,cmp);

	double res=0;

	for (int i=0; i<=n; i++){
		double len=c[i].f-c[i].s;
		double tm=len/(c[i].w+r);
		if (tm>t){
			res+=t;
			len-=t*(r+c[i].w);
			t=0;
			res+=len/(s+c[i].w);
		} else{
			t-=tm;
			res+=tm;
		}
	}
	printf("Case #%d: %.10lf\n",tst,res);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	scanf("%d",&tests);

	for (int tt=1; tt<=tests; tt++){
		solve(tt);
	}

	return 0;
}