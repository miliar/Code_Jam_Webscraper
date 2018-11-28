#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;
struct way{
	double s, t, sp;
} w[1001];
bool operator <(const way &a, const way &b){return a.sp<b.sp;}

int main(){
	int T, n, i, j, time=0;
	double x, s, r, t, ans, len;
	scanf("%d", &T);
	while(T--){
		ans=0;
		scanf("%lf%lf%lf%lf%d", &x, &s, &r, &t, &n);
		for(i=0; i<n; i++){
			scanf("%lf%lf%lf", &w[i].s, &w[i].t, &w[i].sp);
			x-=w[i].t-w[i].s;
		}
		sort(w, w+n);
		if(x/r<=t){
			ans+=x/r;
			t-=x/r;
		}else{
			ans+=t;
			x-=r*t;
			t=0;
			ans+=x/s;
		}
		for(i=0; i<n; i++){
			len=w[i].t-w[i].s;
			if(len/(r+w[i].sp)<=t){
				ans+=len/(r+w[i].sp);
				t-=len/(r+w[i].sp);
			}else{
				ans+=t;
				len-=(r+w[i].sp)*t;
				t=0;
				ans+=len/(s+w[i].sp);
			}
		}
		printf("Case #%d: %.9f\n", ++time, ans);
	}
    return 0;
}
