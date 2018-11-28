 #include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>


using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define foru(i,a,b) for(i=(a);i<=(b);i++)
#define ford(i,a,b) for(i=(a);i>=(b);i--)

int n;


double eps = 1e-8;

int cmp(double a) {
    return a < -eps ? -1 : a > eps;
}
double sqr(double a) {
    return a * a;
}




struct line{
       double a,b,c;
};

class point{
    public:
        double x,y;
        point(){}
        point(double x,double y) : x(x) , y(y) {}   
        
        
        void input(){scanf("%lf %lf",&x,&y);}
        double operator *(point a){return x*a.y-y*a.x;}
        double operator ^(point a){return x*a.x+y*a.y;}
        point operator -(point a){a.x=x-a.x;a.y=y-a.y;return a;}
        point operator +(point a){a.x=x+a.x;a.y=y+a.y;return a;}
        point operator /(double a){ return point(x/a,y/a);}
        bool operator == (const point &b) {return !cmp(x - b.x) && !cmp(y - b.y);}
};


double area(point a,point b,point c){
  return (b-a)*(c-a);
}

double dot(point a, point b,point c){
  return (b-a) ^ (c-a);        
}

double dis(point a){return sqrt(a.x*a.x+a.y*a.y);}
double dis(point a,point b){return dis(b-a);}


point a[10];
double r[10];

double work(point a, point b, double r1, double r2){
	double lens,t,i,j,l,r,p1,p2;
	lens=dis(a,b);
	p1=0;
	p2=lens;
	l=0-r1;
	r=lens+r2;
	
	l=min(l,p2-r2);
	r=max(r,p1+r1);
	return (r-l)/2;
}

int main(){
    freopen("d.in","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j,k,test,cases;
	scanf("%d",&test);
	cases=0;
    while (test){
		test--;
		cases++;
		scanf("%d",&n);
		printf("Case #%d: ",cases);
		
		foru(i,1,n) {
			a[i].input();
			scanf("%lf",&r[i]);
		}
		double ans;
		if (n==1) {
			ans=r[1];	
		}
		else
		if (n==2) {
			ans=max(r[1],r[2]);	
		}
		else {
			
		ans=min( max(r[3],work(a[1],a[2],r[1],r[2])), 
		         max(r[1],work(a[2],a[3],r[2],r[3]))
				 );
		ans=min(ans,
		         max(r[2],work(a[1],a[3],r[1],r[3])));
		}
		printf("%.6lf\n",ans);
		
		
	}
     return 0;
}
    
