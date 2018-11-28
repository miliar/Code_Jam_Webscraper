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


const int MAXN=110;
int arr[MAXN][MAXN];
double rwp[MAXN];
double rowp[MAXN];
double roowp[MAXN];
int main(){
	int T;
	cin>>T;
	for(int tt=1;tt<=T;tt++){
		int N;
		cin>>N;

		for(int i=0;i<N;i++)
			for(int j=0;j<N;j++){
				char ch;
				scanf(" %c",&ch);
				dump(ch);
				if(ch=='.')arr[i][j]=0;
				else if(ch=='1')arr[i][j]=1;
				else if(ch=='0')arr[i][j]=-1;
				else RE;
			}
		cout<<"Case #"<<tt<<":"<<endl;
		for(int t=0;t<N;t++){
			int wpttl=0;
			int wp=0;
			for(int i=0;i<N;i++)if(arr[t][i]){
				wpttl++;
				if(arr[t][i]==1)wp++;
			}
			rwp[t]=(double)wp/(double)wpttl;
		}
		for(int t=0;t<N;t++){
			double pwp[MAXN]={0};
			int hasa=0;
			for(int p=0;p<N;p++)if(arr[t][p]){
				hasa++;
				int wpttl=0,wp=0;
				for(int i=0;i<N;i++)if(arr[p][i] && i!=t){
					wpttl++;
					if(arr[p][i]==1)wp++;
				}
				pwp[p]=(double)wp/(double)wpttl;
			}
			rowp[t]=0;
			for(int i=0;i<N;i++)rowp[t]+=pwp[i];
			rowp[t]/=(double)hasa;
		}
		for(int t=0;t<N;t++){
			double north=0,south=0;
			for(int p=0;p<N;p++)if(arr[t][p]){
				south+=1.0;
				north+=rowp[p];
			}
			roowp[t]=north/south;
		}
		for(int i=0;i<N;i++)
			printf("%.8lf\n",rwp[i]*0.25+rowp[i]*0.5+roowp[i]*0.25);
	}
	return 0;
}

			
			


