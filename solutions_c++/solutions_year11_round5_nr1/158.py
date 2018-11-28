#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#define EPSILON 1e-8
using namespace std;

struct point{long double x,y;};
int TC,U,L,G,tot,t1,t2;
long double area,lo,mid,hi,W,GU[105],GL[105],cur;
point PL[105],PU[105],P[255],A[105],B[105],P_tmp;
bool done;

inline bool eq(long double a,long double b){
	return a-b < EPSILON && b-a < EPSILON;
}

bool cmp(point a,point b){
	return a.x < b.x;
}

long double cal(point a,point b,point c){
	return a.x*b.y + b.x*c.y + c.x*a.y - a.y*b.x - b.y*c.x - c.y*a.x;
}

long double cal_area(){
	double tmp = 0;
	for(int i=0;i<tot;++i) tmp += (P[i].x*P[(i+1)%tot].y - P[i].y * P[(i+1)%tot].x);
	tmp *= 0.5;
	return tmp;
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&TC);
	for(int testcase=1;testcase<=TC;++testcase){
		scanf("%Lf%d%d%d",&W,&L,&U,&G);
		for(int i=0;i<L;++i){
			scanf("%Lf%Lf",&PL[i].x,&PL[i].y);
			P[i] = PL[i];
			if(i > 0) GL[i] = (PL[i].y-PL[i-1].y)/(PL[i].x-PL[i-1].x);
		}
		for(int i=0;i<U;++i){
			scanf("%Lf%Lf",&PU[i].x,&PU[i].y);
			P[L+U-1-i] = PU[i];
			if(i > 0) GU[i] = (PU[i].y-PU[i-1].y)/(PU[i].x-PU[i-1].x);
		}
		tot = U+L;
	//	for(int i=0;i<tot;++i) printf("(%Lf %Lf\n",P[i].x,P[i].y);
		area = cal_area()/((long double)(G));
		lo = PU[0].x;
		hi = W;
	//	printf("each piece = %Lf\n",area);
		printf("Case #%d:\n",testcase);
		for(int a=0;a<G-1;++a){
			hi = W;
			done = 0;
			while(!eq(lo,hi)){
				mid = P_tmp.x = (lo+hi)/2.0;
				t1 = lower_bound(PL,PL+L,P_tmp,cmp) - PL;
				if(PL[t1].x < mid) ++t1;
				t2 = lower_bound(PU,PU+U,P_tmp,cmp) - PU;
				if(PU[t2].x < mid) ++t2;
				for(int i=0;i<t1;++i) P[i] = PL[i];
				P[t1].x = mid;
				P[t1].y = PL[t1].y - GL[t1] * (PL[t1].x-mid);
				P[t1+1].x = mid;
				P[t1+1].y = PU[t2].y - GU[t2] * (PU[t2].x-mid);
				for(int i=t2-1;i>=0;--i) P[t1+2+t2-1-i] = PU[i];
			//	if(eq(mid,5.0)){
				//	printf("new points have coords (%Lf %Lf) (%Lf %Lf)\n",P[t1].x,P[t1].y,P[t1+1].x,P[t1+1].y);
					
			//	}
				tot = t1+t2+2;
		//		for(int i=0;i<tot;++i) printf("(%Lf %LF) ",P[i].x,P[i].y);
		//		printf("\n");
		//		printf("tot = %d and %Lf\n",tot,cal_area());
				cur = cal_area() - (long double)(a)*area;
			//	printf("mid = %Lf and cur = %Lf\n",mid,cur);
				if(eq(cur,area)){
					printf("%Lf\n",mid);
					done = 1;
					break;
				}
				else if(cur > area) hi = mid;
				else if(cur < area) lo = mid;
			}
			if(!done) printf("%Lf\n",hi);
		}
	}
}
