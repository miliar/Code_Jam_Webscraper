#include <stdio.h>
#include <string.h>
#include <algorithm>

int n, d;
double st,ed;
struct node {
	double p, v;
	
	void get() {
		scanf("%lf%lf",&p,&v);
	}
	
	bool operator <(const node &t) const {
		return (p < t.p);
	}
} ven[220];

int main() {
	int t,c=0;
	
	scanf("%d",&t);
	while(t--) {
		scanf("%d%d",&n,&d);
		for(int i=0;i<n;++i)
			ven[i].get();
		std::sort(ven,ven+n);
		
		st = 0, ed = 1e20;
		while( (ed-st) > 1e-2 ) {
			double mid = (st+ed)/2;
			
			int ptr = 0;
			int peo[210];
			for(int i=0;i<n;++i)
				peo[i] = (int)ven[i].v;
			double next_p = (double)ven[0].p-mid;
			while(ptr < n) {
				//printf("%d %lf\n",ptr,next_p);
				if(ven[ptr].p < next_p) {	//to right
					if(ven[ptr].p+mid < next_p)	break;
					next_p += d;
					--peo[ptr];
				} else if(ven[ptr].p == next_p) {	//don't move
					next_p += mid;
					--peo[ptr];
				} else {	//to left
					if(ven[ptr].p-mid > next_p) {
						next_p = ven[ptr].p-mid+d;
						--peo[ptr];
					} else {
						next_p += d;
						--peo[ptr];
					}
				}
				if(peo[ptr] <= 0)	++ptr;
			}
			//printf("%d\n",ptr);
			//puts("VVVVVVVVVVVV");
			//scanf("%*d");
			if(ptr >= n) { //yes
				ed = mid;
			} else {	//no
				st = mid;
			}
		}
		
		printf("Case #%d: %.1lf\n", ++c, ed);
	}
	
	return 0;
}
