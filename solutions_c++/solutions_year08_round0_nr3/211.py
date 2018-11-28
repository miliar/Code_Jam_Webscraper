#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <bitset>

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,b) FOR(i,0,b)
#define sqr(a) ((a)*(a))

const double EPS=1e-5;
const double PI=4*atan(1.0);
#define eq(a,b) (abs((a)-(b))<=EPS)

using namespace std;

char fin[]="c.in",fout[]="c.out";
int n;
double f,r,t,l,g,res;

inline double integ(double x,double a){return (sqr(a)*asin(x/abs(a))+sqrt(sqr(a)-sqr(x))*x)/2;}
inline double suma(double x1,double x2,double a){return integ(x2,a)-integ(x1,a);}

int main(){
	freopen(fin,"r",stdin);
	freopen(fout,"w",stdout);
	scanf("%d",&n);
	REP(z,n){
		double a,x,y,sh,sa,sf,curx,cury,te;
		int i,j;
		cin>>f>>r>>t>>l>>g;
		g-=2*f;//hole width
		t+=f;//ring radius
		l+=f;//string radius
		res=1;
		if(g<=0)goto FUK;
		a=r-t;//radius
		sa=PI*sqr(a)/4;
		sf=PI*sqr(r)/4;
		sh=i=j=0;
		while(true){
			y=l+i*(g+2*l);
			if(y>=a)break;
			j=0;
			while(true){
				x=l+j*(g+2*l);
				curx=sqrt(sqr(a)-sqr(y));
				if(x>=curx)break;
				cury=sqrt(sqr(a)-sqr(x));
				if(sqrt(sqr(x+g)+sqr(y+g))<=a)
					te=sqr(g);
				else if(y+g>cury && x+g>curx)
					te=sa-suma(0,x,a)-suma(0,y,a)+x*y;
				else if(y+g>cury)
					te=sa-suma(0,x,a)-suma(x+g,a,a)-g*y;
				else if(x+g>curx)
					te=sa-suma(0,y,a)-suma(y+g,a,a)-g*x;
				else
					te=sa-suma(y+g,a,a)-suma(x+g,a,a)-x*y-g*(x+y);
				sh+=te;
				j++;
			}
			i++;
		}
		res-=sh/sf;
FUK:
		printf("Case #%d: %0.6lf\n",z+1,res);
	}
	exit(0);
}
