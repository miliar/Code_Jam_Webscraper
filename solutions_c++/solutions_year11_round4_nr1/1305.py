#include <stdio.h>
#include <string.h>
#include <algorithm>

int n;
double len, tt, vf, vr;
struct node {
	double a, b, sp;
	
	bool operator < (const node &t) const {
		return (sp < t.sp);
	}
	
	void get() {
		scanf("%lf%lf%lf",&a,&b,&sp);
	}
} road[1010];

int main() {
	int t,c=0;
	
	scanf("%d",&t);
	while(t--) {
		scanf("%lf%lf%lf%lf%d",&len,&vf,&vr,&tt,&n);
		for(int i=0;i<n;++i)
			road[i].get();
		for(int i=0;i<n;++i)
			len -= road[i].b-road[i].a;
		
		//printf("%lf %lf\n",tt,len);
		std::sort(road, road+n);
		double sum = 0;
		if(vr*tt >= len) {
			sum = len/vr;
			tt -= sum;
			len = 0;
		} else {
			sum = tt;
			len -= vr*tt;
			sum += len/vf;
			tt = 0;
		}
		//printf("%lf %lf %lf\n",tt,len,sum);
		
		int i = 0;
		if(tt > 0) {
			for(i=0;i<n;++i) {
				if( (vr+road[i].sp)*tt >= (road[i].b-road[i].a) ) {
					double temp = (double)(road[i].b-road[i].a)/(vr+road[i].sp);
					sum += temp;
					tt -= temp;
					//printf("vv:%lf %lf %lf\n",tt,len,sum);
				} else {
					sum += tt;
					sum += (road[i].b-road[i].a-(vr+road[i].sp)*tt)/(vf+road[i].sp);
					tt = 0;
					++i;
					//printf("dd:%lf %lf %lf\n",tt,len,sum);
					break;
				}

			}
		}
		
		for(;i<n;++i)
			sum += (road[i].b-road[i].a)/(vf+road[i].sp);
		
		printf("Case #%d: %lf\n",++c,sum);
	}
	
	return 0;
}
