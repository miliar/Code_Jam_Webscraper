#include <cmath>
#include <ctime>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#define maxl 1000000000
#define maxn 50000
using namespace std;

typedef long long ll;

struct dt{
	double s,t,w;
}a[maxn];

bool cmp1(const dt &d1,const dt &d2){
	return d1.s<d2.s;
}

bool cmp2(const dt &d1,const dt &d2){
	return d1.w<d2.w;
}

const double eps=1e-8;

void solve(){
	double x,s,r,t,len,t1,ans;
	int i,n;
	scanf("%lf%lf%lf%lf%d",&x,&s,&r,&t,&n);
	for(i=1;i<=n;++i)scanf("%lf%lf%lf",&a[i].s,&a[i].t,&a[i].w);
	sort(&a[1],&a[n+1],cmp1);
	a[0].s=0;
	a[0].t=a[1].s;
	a[0].w=0;
	for(i=2;i<=n;++i)a[0].t+=a[i].s-a[i-1].t;
	a[0].t+=x-a[n].t;
	ans=0;
	sort(&a[1],&a[n+1],cmp2);
	for(i=0;i<=n;++i){
		len=a[i].t-a[i].s;
		if(t<eps){
			ans+=len/(s+a[i].w);
			continue;
		}
		t1=min(t,len/(r+a[i].w));
		ans+=t1;
		t-=t1;
		len-=(r+a[i].w)*t1;
		if(t<eps)ans+=len/(s+a[i].w);
	}
	printf("%.8f\n",ans);
}
	

int main(){
	int t,i;
	scanf("%d",&t);
	for(i=1;i<=t;++i){
		printf("Case #%d: ",i);
		solve();
	}
} 
