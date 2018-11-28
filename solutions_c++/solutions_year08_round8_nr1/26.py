#include <algorithm>
#include <iostream>
#include <iterator>
#include <fstream>
#include <cstdlib>
#include <sstream>
#include <string>
#include <vector>
#include <bitset>
#include <math.h>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <complex>

#pragma comment(linker, "/STACK:60777216")

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<pii> vpi;
typedef pair<ld,ld> pdd;
typedef complex<ld> VEC;
typedef vector<pdd> vdd;
typedef unsigned long long ul;
typedef unsigned int UI;
typedef pair<pii,int> p3i;
typedef vector<p3i> vp3i;
typedef vector<double> vd;

#define F(i,a,b) for (int _n(b), i(a); i < _n; i++) 
#define FD(i,a,b) for (int _n(b), i(a); i >= _n; i--) 
#define R(i,n) F(i,0,n) 
#define SORT(a) sort((a).begin(),(a).end())
#define UN(v) SORT(v),v.erase(unique(v.begin(),v.end()),v.end())
#define RV(v) reverse((v).begin(),(v).end())
#define CL(a,b) memset(a,b,sizeof(a))
#define pb push_back

const int INF = 1011111111;
const double Pi =acos(-1.);
const ld eps =1e-8;

int nb(int x){return x?nb(x&(x-1))+1:0;}
ll gcd(ll a,ll b){while(a&&b){if(a>b) a%=b;else b%=a;}return a+b;}
int gcd(int a,int b){while(a&&b){if(a>b) a%=b;else b%=a;}return a+b;}

ld det(ld a11,ld a21,ld a12,ld a22){return fabs(a11*a22-a12*a21);}

int TC;
struct T{

	ld x[3],y[3];
	T(){CL(x,0),CL(y,0);}
	void ccin(){
		R(i,3) cin>>x[i]>>y[i];
	}
	pdd getC(ld X,ld Y){
		pdd r;
		r.first=hypot(x[0]-X,y[0]-Y);
		ld d1,d2,d3;
		d1=hypot(x[1]-x[0],y[1]-y[0]);
		d2=hypot(X-x[0],Y-y[0]);
		d3=hypot(X-x[1],Y-y[1]);
		ld a=0;
		if(fabs(d1)>eps && fabs(d2)>eps){
			a=acos((d1*d1+d2*d2-d3*d3)/2/d1/d2);
		}
		r.second=a;
		return r;
	}
	bool good(pdd t){
		ld s=det(x[1]-x[0],y[1]-y[0],x[2]-x[0],y[2]-y[0]);
		ld s1=det(x[1]-x[0],y[1]-y[0],t.first-x[0],t.second-y[0]);
		ld s2=det(t.first-x[0],t.second-y[0],x[2]-x[0],y[2]-y[0]);
		ld s3=det(x[1]-t.first,y[1]-t.second,x[2]-t.first,y[2]-t.second);
		if(fabsl(s-s1-s2-s3)<eps) return true;
		return false;
	}
	pdd getP(pdd v){
		VEC q1(x[1]-x[0],y[1]-y[0]);
		q1/=hypot(q1.real(),q1.imag());
		q1=q1*polar<ld>(1.,v.second);
		q1*=v.first;

		VEC q2(x[1]-x[0],y[1]-y[0]);
		q2/=hypot(q2.real(),q2.imag());
		q2=q2*polar<ld>((ld)1.,(ld)-v.second);
		q2*=v.first;

		pdd x1,x2;
		x1=pdd(x[0]+q1.real(),y[0]+q1.imag());
		x2=pdd(x[0]+q2.real(),y[0]+q2.imag());

//		if(good(x1))
			return x1;
//		if(good(x2)) 
//			return x2;
//		puts("FUCK");
//		return x2;

		//return x1;
		 
	}
};

int main(){    
    
    freopen("input.txt","r",stdin);       
    freopen("output.txt","w",stdout);   
	cin>>TC;
	R(tc,TC){
		cout<<"Case #"<<tc+1<<": ";

		T t1,t2;
		t1.ccin(),t2.ccin();
		ld x=t1.x[0],y=t1.y[0];
		ld M=hypot(t2.x[0]-t2.x[1],t2.y[0]-t2.y[1])/hypot(t1.x[0]-t1.x[1],t1.y[0]-t1.y[1]);
		ld D=0;
		R(i,200000){
			pdd q=t1.getC(x,y);
			q.first*=M;
			pdd w=t2.getP(q);
			

			//if(i==199999)				cout<<(D=hypot(x-w.first,y-w.second))<<endl;
			x=w.first;
			y=w.second;

		}
		/*if(D>1e-6){
                   for(ld q=-0.00010;q<=0.00010;q+=0.000001)
                       for(ld q2=-0.00010;q2<=0.00010;q2+=0.000001){
                              	pdd qq=t1.getC(x+q,y+q2);
			qq.first*=M;
			pdd w=t2.getP(qq);
			

			if(D>hypot(x+q-w.first,y+q2-w.second)){
//				cout<<(D=)<<endl;
				D=hypot(x+q-w.first,y+q2-w.second);
    			x=w.first;
	   	  	y=w.second;
         }
                       }
        }*/
		printf("%.6lf %.6lf",(double)x,(double)y);
		cout<<endl;
	}
    
    return 0;
}   
