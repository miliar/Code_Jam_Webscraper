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

typedef long double LD;

struct cor_t{
	LD s,e;
	LD w;
	LD l,t;
	bool operator <(const cor_t& o)const{
		return w<o.w;
	}
};

const int MAXN=10000;

cor_t ipt[MAXN];


int main(){
	int T;
	cin>>T;
	for(int tt=1;tt<=T;tt++){
		LD X,S,R,t;
		int N;
		cin>>X>>S>>R>>t;
		cin>>N;
		if(R<S)RE;
		LD ttll=0;
		for(int i=0;i<N;i++){
			cin>>ipt[i].s>>ipt[i].e>>ipt[i].w;
			ttll+=(ipt[i].l=ipt[i].e-ipt[i].s);
			ipt[i].w+=S;
		}
		ipt[N].l=X-ttll;
		ipt[N].w=S;
		N++;
		sort(ipt,ipt+N);
		LD res=0;
		for(int i=0;i<N;i++){
			LD l=ipt[i].l;
			LD v=ipt[i].w;
			if(l/(v+R-S)<t){
				t-=l/(v+R-S);
				res+=l/(v+R-S);
			}else{
				LD lh=t*(v+R-S);
				
					res+=t;
					res+=(l-lh)/v;
				
				t=0;
			}
		};
		printf("Case #%d: %.7lf\n",tt,(double)res);
	}
	return 0;
}

		

	
