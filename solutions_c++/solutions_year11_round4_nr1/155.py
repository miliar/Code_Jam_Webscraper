#include <stdio.h>
#include <algorithm>

struct dtype {
	int b,e,w;
	bool operator <(const dtype &rhs) const {
		return this->w < rhs.w;
	}
} dat[1003];

using namespace std;

int main(){
	int TT;
	scanf("%d",&TT);
	for(int testcase = 1; testcase <= TT; testcase ++) {
		int X,S,R,n;
		double t;
		scanf("%d%d%d%lf%d",&X,&S,&R,&t,&n);
		for(int i = 0;i < n;i ++){
			scanf("%d%d%d",&dat[i].b,&dat[i].e,&dat[i].w);
			X -= dat[i].e - dat[i].b;
		}
		dat[n].b = 0;
		dat[n].e = X;
		dat[n].w = 0;
		n ++;
		sort(dat,dat+n);
		double ans = 0;
		for(int i = 0; i < n;i ++) {
			if( (dat[i].e - dat[i].b) <= t * (R+dat[i].w)) {
				ans += (dat[i].e - dat[i].b) / (double)(R+dat[i].w);
				t -= (dat[i].e - dat[i].b) / (double)(R+dat[i].w);
			}else {
				ans += t;
				ans += ((dat[i].e - dat[i].b) - t * (R+dat[i].w)) / (double)(S+dat[i].w);
				t = 0;
			}
		}
		printf("Case #%d: %.9f\n",testcase, ans);
	}
	return 0;
}

