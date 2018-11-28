#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <cmath>
#include <cstring>
#include <memory.h>
#include <algorithm>
#define sqr(x) ((x)*(x))
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define abs(a) ((a)<0?(-(a)):(a))
#define swap(a,b) {typeof(a) t_=a; a=b; b=t_;}
#define For(i,a,b) for(int &i_=i=(a), e_=(b); i_<e_; ++i_)
#define Forw(i,a,u) for(i=(a); u; ++i)
#define cinar(m,n) for(int i_=0; i_<n; ++i_) cin>>m[i_];
#define fill(m) memset(m,0,sizeof(m));
#define pi 3.141592653589793
#define y1 stupid_math
/*	printf("Case #%d:\n",ti+1);*/
typedef long long int64;
typedef unsigned char byte;
using namespace std;

int t,ti;

int c, p[500], v[500], n,i,j,k,l;
double d;

double f(double x){
	int i, j, n;
	double res=0;
	
	i=0; j=0;
	while(i<c){
		res = max(res, abs(p[i]-x));
		//cout<<res<<' '<<i<<' '<<x<<endl;
		
		x+=d;
		++j;
		if(j>=v[i]){
			++i; j=0;
		}
	}
	
	return res;
}	

bool check(double m){ //cout<<"here\n"; cout.flush();
	double r, x=-1e18;
	int i, j;
	
	For(i,0,c){
		For(j,0,v[i]){ //cout<<x<<' '; cout.flush();
			if(p[i]-m>=x+d) x=p[i]-m; else
			if(p[i]-m<x+d && p[i]>x+d) x=x+d; else
			if(x+d-p[i]<=m) x=x+d; else return false;
		}
	}
	return true;
}

double gss(double left, double right){
    double fi = 0.6180339887498948482;
    double p1, p2, f1, f2;
    p1 = right - (right - left)*fi;
    p2 = left + (right - left)*fi;
    f1 = f(p1);
    f2 = f(p2);
	
	int it;
    For(it,0,160){
        if( f1>f2 ){
            left = p1;
            p1 = p2;
            p2 = left + (right - left)*fi;
            f1 = f2;
            f2 = f(p2);
        }else{
            right = p2;
            p2 = p1;
            p1 = right - (right - left)*fi;
            f2 = f1;
            f1 = f(p1);
        }
    }
    return f1;
}

double bs(double l, double r){
	double c;
	
	int it;
    For(it,0,100){
		c = (l+r)/2.;
		//cout<<c<<endl;
		if(check(c)) r=c; else l=c;
	}
	
	return c;
}

int main(){
	freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
	
	cin>>t;
	For(ti,0,t){
		
		cin>>c>>d;
		For(i,0,c) cin>>p[i]>>v[i];
		
		
		
		
		printf("Case #%d: ",ti+1);
		double r=4e17;
		printf("%0.6lf\n",bs(0, r));
	}
	
	return 0;
}