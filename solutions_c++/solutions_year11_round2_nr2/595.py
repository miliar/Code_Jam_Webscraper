#include<cmath>
#include<cstdio>
#include<algorithm>
using namespace std;
const double eps=1e-8;
struct TPoint{
	long long x,y;
	bool operator<(const TPoint &t)const{
		return x<t.x;
	}
}a[200];
long long n,d;
bool ok(double mid){
	long long i;
	double v;
	v=a[0].x-mid+(a[0].y-1)*d;
	if(fabs(v-a[0].x)-eps>mid)return false;
	for(i=1;i<n;i++){
		v=max(v+a[i].y*d,a[i].x-mid+(a[i].y-1)*d);
		if(fabs(v-a[i].x)-eps>mid)return false;
	}
	return true;
}
int main(){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	long long i,t,tt=1,low,up,mid;
	double v;
	scanf("%I64d",&t);
	while(t--){
		scanf("%I64d%I64d",&n,&d);
		for(i=0;i<n;i++)
			scanf("%I64d%I64d",&a[i].x,&a[i].y);
		sort(a,a+n);
		low=0;up=1000000000;
		while(low<=up){
			mid=(low+up)/2;
			if(ok((double)mid/2))up=mid-1;
			else low=mid+1;
		}
		printf("Case #%I64d: %.1lf\n",tt++,(double)low/2);
	}
	return 0;
}