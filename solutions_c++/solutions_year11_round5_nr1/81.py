#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<list>
#define fr(i,a,b) for(i=a;i<=b;i++)
#define x first
#define y second
#define point(a,b) make_pair(a,b)
using namespace std;
typedef pair<double,double> point;
typedef vector<point> polygon;
const double zero=1e-8;
const double limit=1e8;
const double pi=acos(-1.0);
point operator+(point a,point b){
	return make_pair(a.x+b.x,a.y+b.y);
}
point operator-(point a,point b){
	return make_pair(a.x-b.x,a.y-b.y);
}
point operator*(point a,double b){
	return make_pair(a.x*b,a.y*b);
}
point operator/(point a,double b){
	return make_pair(a.x/b,a.y/b);
}
double area2(point a,point b,point c){
	return (b.x-a.x)*(c.y-a.y)-(c.x-a.x)*(b.y-a.y);
}
double dis(point a,point b){
	return sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));
}
ostream& operator<<(ostream& os,point r){
	os<<r.x<<" "<<r.y<<" ";
	return os;
}
void print(polygon p){
	int i;
	cout<<p.size()<<":";
	fr(i,0,(int)p.size()-1)
		cout<<"("<<p[i].x<<","<<p[i].y<<")";
	cout<<endl;
}
point poi(point a,point b,point c,point d){
	double s1=area2(a,b,c),s2=area2(a,b,d);
	return make_pair((c.x*s2-d.x*s1)/(s2-s1),(c.y*s2-d.y*s1)/(s2-s1));
}
bool onseg(point a,point b,point c){
	return dis(a,c)+dis(b,c)-dis(a,b)<zero;
}
point rotate(point a,point b,double angle){
	return make_pair((b.x-a.x)*cos(angle)-(b.y-a.y)*sin(angle)+a.x,(b.x-a.x)*sin(angle)+(b.y-a.y)*cos(angle)+a.y);
}
bool intersect(point &a,point &b,point &c,point &d){
	return area2(a,b,c)*area2(a,b,d)<-zero&&area2(c,d,a)*area2(c,d,b)<-zero;
}
double newy(point a,point b,double x){
	return (x-a.x)*(b.y-a.y)/(b.x-a.x)+a.y;
}
vector<point> bot,up;
int n,m,g,i,ca,ti;
double w,xx,yy,tot;
double cal(point a,point b){
	return fabs(b.x-a.x)*(a.y+b.y)*0.5;
}
double area(vector<point> p,double cut){
	double sum=0;
	int i;
	fr(i,0,(int)p.size()-2)
		if(p[i+1].x<cut)
			sum+=cal(p[i],p[i+1]);
		else{
			sum+=cal(p[i],point(cut,newy(p[i],p[i+1],cut)));
			break;
		}
	return sum;
}
double find(double le,double ri,double v){
	double mid=(le+ri)/2,now=area(up,mid)-area(bot,mid);
	if(ri-le<zero)
		return mid;
	if(now<v)
		return find(mid,ri,v);
	else
		return find(le,mid,v);
}
int main(){
	freopen("a2.in","r",stdin);
	freopen("a2.out","w",stdout);
	cin>>ca;
	fr(ti,1,ca){
		cin>>w>>n>>m>>g;
		up.clear();
		bot.clear();
		fr(i,0,n-1){
			cin>>xx>>yy;
			bot.push_back(point(xx,yy));
		}
		fr(i,0,m-1){
			cin>>xx>>yy;
			up.push_back(point(xx,yy));
		}
		tot=area(up,w)-area(bot,w);
		cout<<"Case #"<<ti<<":"<<endl;
		fr(i,1,g-1)
			printf("%.8lf\n",find(0,w,tot/g*i));
	}
}
