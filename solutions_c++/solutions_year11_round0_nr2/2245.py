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
#include <vector>
int main(){
	int T;
	cin>>T;
	char arr[26][26];
	for(int tt=1;tt<=T;tt++){
		int C,D,N;
		bz(arr);
		cin>>C;
		char cs[1000];
		for(int i=0;i<C;i++){
			scanf(" %s",cs);
			arr[cs[0]-'A'][cs[1]-'A']=cs[2];
			dump(cs);
		}
		cin>>D;
		vector<pair<int,int> > exc;
		
		for(int i=0;i<D;i++){
			scanf(" %s",cs);
			exc.push_back(pair<int,int>(cs[0]-'A',cs[1]-'A'));
		}
		int has[26]={0};
		cin>>N;
		if(N)scanf(" %s",cs);
		char opt[1000],*iopt;
		iopt=opt;
		for(int i=0;i<N;i++){
			*iopt++=cs[i];
			has[*(iopt-1)-'A']++;
			if(iopt-opt>=2){
				char ths;
				int x=*(iopt-1)-'A',y=*(iopt-2)-'A';
				if((ths=arr[x][y]) || (ths=arr[y][x])){
					has[*--iopt-'A']--;
					has[*--iopt-'A']--;
					*iopt++=ths;
					has[*(iopt-1)-'A']++;
				}else{
					for(vector<pair<int,int> >::iterator it=exc.begin();
							it!=exc.end();it++)
						if(has[it->first] && has[it->second]){
							bz(has);
							iopt=opt;
						}
				}
			}
		}
		cout<<"Case #"<<tt<<": [";
		int sz=iopt-opt;
		for(int i=0;i<sz;i++){
			cout<<opt[i];
			if(i!=sz-1)cout<<", ";
		}
		cout<<"]"<<endl;
	}
	return 0;
}




			
