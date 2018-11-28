#include <stdio.h>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <complex>
#include <stdlib.h>
#include <assert.h>

using namespace std;

#define INF 0x7f7f7f7f
#define INFL 0x7f7f7f7f7f7f7f7fLL
#define RE {*((int*)0)=0;}

#ifndef M_PIl
    #define M_PIl 3.141592653589793238L
    #define M_PI 3.141592653589793238
#endif

#define forv(i,n) for(int (i)=0;(i)<(n);(i)++)
#define forr(i,a,b)for(int (i)=(a);(i)<(b);(i)++)
#define bz(i) {memset(i,0,sizeof(i));assert(sizeof(i)!=sizeof(int*));}
#define IC(it,array) {assert(sizeof(array)!=sizeof(int*));if((it) >=(array)+sizeof(array)/sizeof(*(array)) || (it)<(array))RE;}

#ifdef DBG
#define ISD true
#define dump(x) cerr<<"[Line "<<__LINE__<<"]: "<<#x<<"="<<(x)<<endl;
#define hint(x,y) cerr<<"[Line "<<__LINE__<<"]: "<<(x)<<":"<<(y)<<endl
#else
#define ISD false
#define dump(x)
#define hint(x,y)
#endif

#define CPT complex<T>
#ifdef __GNUC__
    const long double INFd= ((double)1/(double)0);
    typedef long long LL;
    typedef unsigned long long u64;
#else
    const long double INFd=1.0e99;
    typedef __int64 LL;
    typedef unsigned __int64 u64;
#endif

typedef unsigned char u8;
typedef unsigned short u16;
typedef unsigned int u32;

template <typename T>
inline bool maxi(T& tg, const T& cp) {
    if (tg < cp) {
        tg = cp;
        return true;
    }
    return false;
};

template <typename T>
inline bool mini(T& tg, const T& cp) {
    if (cp < tg) {
        tg = cp;
        return true;
    }
    return false;
};
//========================================

const int MAXV=1100000;

int opos[MAXV];
double npos[MAXV];

bool calc(double mid,double D,int cnt){
	double lm=opos[0]-mid;
	for(int i=1;i<cnt;i++){
		double tg=lm+D;
		double dist=fabs(tg-opos[i]);
		if(dist<mid)lm+=D;
		else {
			if(tg<opos[i])lm=tg+(dist-mid);
			else return false;
		}
	}
	return true;
}

		
int main(){
	int T;
	cin>>T;
	for(int tt=1;tt<=T;tt++){
		int C,D;
		cin>>C>>D;
		int av=0;
		for(int c=0;c<C;c++){
			int P,V;
			cin>>P>>V;
			for(int i=0;i<V;i++){
				opos[av++]=P;
			}
		}
		sort(opos,opos+av);
		if(!av)RE;
		double l=0,r=1e14,mid;
		while(fabs(l-r)>1e-8){
			mid=(l+r)*0.5;
			bool yn=calc(mid,D,av);
			if(yn)r=mid;
			else l=mid;
		}
		printf("Case #%d: %.7lf\n",tt,mid);
	}
	return 0;
}

