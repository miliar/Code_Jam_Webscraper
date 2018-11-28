#include<iostream>
#include<cstdio>

using namespace std;

struct node{
	double l,r,v;
}a[2000000];
const double eps = 1e-8;

bool cmp(const node &a ,const node &b){
	return a.l<b.l;
}
bool cmp1(const node &a,const node &b){
	return a.v<b.v;
}
double x,s,r,t,ret;
int w,cnt,tot,tp,Test;
double ans;

void work(){
	cnt = 0;
	cin >> x >> s >> r >> t >> w;
	r = r-s;
	for (int i =0;i<w;++i){
		++cnt;
		cin >> a[cnt].l >> a[cnt].r;
		cin >> a[cnt].v;
		a[cnt].v+=s;
	}
	tot = cnt;
	sort(a+1,a+cnt+1,cmp);
//		for (int i = 1;i<=cnt;++i) printf("%.2lf %.2lf %.2lf\n",a[i].l,a[i].r,a[i].v);
	//	printf("\n");
	++cnt;
	a[cnt].l = a[cnt-1].r;
	a[cnt].r = x;
	a[cnt].v = s;
	++cnt; 
	a[cnt].l = 0;
	a[cnt].r = a[1].l;
	a[cnt].v = s;

	for (int i = 1;i<tot;++i){
		++cnt;
		a[cnt].l = a[i].r;
		a[cnt].r = a[i+1].l;
		a[cnt].v= s;
	}
	sort(a+1,a+cnt+1,cmp1);
//	for (int i = 1;i<=cnt;++i) printf("%.2lf %.2lf %.2lf\n",a[i].l,a[i].r,a[i].v);
	
	tp = 1;
	ans = 0;
	while (t>eps && tp<=cnt){
		ret = (a[tp].r-a[tp].l)/(a[tp].v+r);
		if (t>ret) {
			t = t-ret;
			ans += ret;
			++tp;
			continue;
		} else{
			ans += (a[tp].r-a[tp].l - t*(a[tp].v+r) )/a[tp].v;
			ans += t;
			++tp;
			break; 
		}
	}
	while (tp<=cnt){
		ans += (a[tp].r-a[tp].l)/a[tp].v;
		++tp;
	}
	
	printf("%.6lf\n",ans);
}

int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	cin >> Test;
	for (int ii = 1;ii<=Test;++ii){
		printf("Case #%d: ",ii);
		work();
	}
	return 0;
}
