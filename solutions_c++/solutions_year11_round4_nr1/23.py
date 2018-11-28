#include <cstdio>
#include <cmath>
#include <cstring>
#include <memory.h>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <map>
#include <queue>
using namespace std;
const int maxn=1001;
struct walkway{
	int st,en,l,sp;
};
walkway a[maxn];
struct for_compare{
	bool operator()(const walkway& A,const walkway& B) const{
		return A.sp<B.sp;
	}
};
int l,sp,r,trt,n;
double rt;

void init(){
	scanf("%d%d%d%d%d",&l,&sp,&r,&trt,&n);
	rt=trt;
	int sumlen=0;
	for (int i=0;i<n;i++){
		scanf("%d%d%d",&a[i].st,&a[i].en,&a[i].sp);
		sumlen+=(a[i].l=a[i].en-a[i].st);
	}
	a[n].l=l-sumlen;
	a[n].sp=0;
	n++;
	sort(a,a+n,for_compare());
	return;
}

double calc(){
	double ans=0;
	for (int i=0;i<n;i++){
		double cur=a[i].l/((double)(a[i].sp+r));
//		printf("%.12f ",cur);
		if (cur>rt){
			double delta=(a[i].sp+r)*rt;
//			printf("aa %.12f ",delta);
			cur=rt+(a[i].l-delta)/((double)(a[i].sp+sp));
			rt=0;
		} else {
			rt-=cur;
		}
//		printf("%.12f \n",cur);
		ans+=cur;
	}
	return ans;
}

int main(){
	int tcase;
	scanf("%d",&tcase);
	for (int i=1;i<=tcase;i++){
		init();
		printf("Case #%d: %.12f\n",i,calc());
	}
	return 0;
}
