#include <cmath>
#include <ctime>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <set>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#define maxn 101000
using namespace std;


const double eps=1e-8;

double sqr(double x){
	return x*x;
}

struct Point{
	double x,y;
	int num;
	Point(double xx=0,double yy=0){
		x=xx;
		y=yy;
	}
	Point operator-(const Point &p)const{
		return Point(x-p.x,y-p.y);
	}
	double operator /(const Point &p)const{
		return x*p.y-y*p.x;
	}
	bool operator <(const Point &p)const{
		if(fabs(x-p.x)>eps)return x<p.x;else return y<p.y; 
	}
	double operator *(const Point &p)const{
		return x*p.x+y*p.y;
	}
	double len(){
		return sqrt(sqr(x)+sqr(y));
	}
};

struct Line{
	double a,b,c;
	Line(Point p1,Point p2){
		a=p2.y-p1.y;
		b=p1.x-p2.x;
		c=p2.x*p1.y-p1.x*p2.y;
	}
	Line(double aa=0,double bb=0,double cc=0){
		a=aa;
		b=bb;
		c=cc;
	}
	Point operator *(const Line &l1)const {
		double temp=a*l1.b-l1.a*b;
		if(fabs(temp)<eps)return Point(1e30,1e30);
		return Point((l1.c*b-c*l1.b)/temp,(c*l1.a-l1.c*a)/temp);
	}
};

int sgn(double x){
	if(x<-eps)return -1;else if(x>eps)return 1;else return 0;
}

int t1;
Point low[maxn],up[maxn];
int c[maxn],a[maxn],a2[maxn],b[maxn],b2[maxn];
double len[maxn];

double calc(double x){
	double ans=0,temp;
	int i;
	for(i=2;i<=t1;++i)if(x>c[i]){
		ans+=(len[i]+len[i-1])*(c[i]-c[i-1])/2;
	}else {
		temp=(len[i]-len[i-1])/(c[i]-c[i-1])*(x-c[i-1])+len[i-1];
		ans+=(len[i-1]+temp)*(x-c[i-1])/2;
		break;
	}
	return ans;
}


void solve(){
	double w;
	int l,u,i,now,g;
	scanf("%lf%d%d%d",&w,&l,&u,&g);
	for(i=1;i<=l;++i)scanf("%d%d",&a[i],&a2[i]);
	for(i=1;i<=u;++i)scanf("%d%d",&b[i],&b2[i]);
	for(i=1;i<=l;++i)c[i]=a[i];
	for(i=1;i<=u;++i)c[i+l]=b[i];
	sort(&c[1],&c[l+u+1]);
	t1=unique(&c[1],&c[l+u+1])-c-1;
	//for(i=1;i<=t1;++i)cout<<c[i]<<" ";
	//cout<<endl;
	now=1;
	for(i=1;i<=t1;++i){
		while(a[now]<c[i])++now;
		if(a[now]==c[i]){
			low[i]=Point(a[now],a2[now]);
		}else {
			low[i]=Point(c[i],(double)(a2[now]-a2[now-1])/(a[now]-a[now-1])*(c[i]-a[now-1])+a2[now-1]);
		}
	}
	now=1;
	for(i=1;i<=t1;++i){
		while(b[now]<c[i])++now;
		if(b[now]==c[i]){
			up[i]=Point(b[now],b2[now]);
		}else {
			up[i]=Point(c[i],(double)(b2[now]-b2[now-1])/(b[now]-b[now-1])*(c[i]-b[now-1])+b2[now-1]);
		}
	}

	for(i=1;i<=t1;++i){
		len[i]=up[i].y-low[i].y;
		//cout<<len[i]<<" ";
	}
	//cout<<endl;
	//cout<<calc(5)<<" ";
	//cout<<calc(10)<<" ";
	//cout<<calc(15)<<" "<<endl;
	double tot=calc(w);
	double each=tot/g;
	double last=0,temp,small,big,mid;
	for(i=1;i<g;++i){
		temp=each*i;
		small=last;big=w;
		while(big-small>eps){
			mid=(big+small)/2;
			if(calc(mid)>temp)big=mid;else small=mid;
		}
		mid=(big+small)/2;
		printf("%.8f\n",mid);
		last=mid;
	}
}

int main(){
	int t,i;
	scanf("%d",&t);
	for(i=1;i<=t;++i){
		printf("Case #%d:\n",i);
		solve();
	}
}
