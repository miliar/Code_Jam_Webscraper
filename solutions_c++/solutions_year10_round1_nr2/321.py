#include <cstdlib>
#include <cstring>
#include <memory>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/time.h>

#define DEBUG
#ifdef DEBUG
#define DBG(...) cerr << #__VA_ARGS__ << ": " << __VA_ARGS__ << endl
#define DV(...) cerr << __VA_ARGS__ << endl
#else
#define DBG(...)
#define DV(...)
#endif


#define _PE(...) printf(__VA_ARGS__); fprintf(stderr, __VA_ARGS__);
#define _E(...) fprintf(stderr, __VA_ARGS__)
#define _Dm(fmt) fprintf(stderr, "%s %d : " fmt,__FUNCTION__,__LINE__)
#define _D(fmt, ...) fprintf(stderr, "%s %d : " fmt,__FUNCTION__,__LINE__,__VA_ARGS__)
#undef _P
#define _P(...) printf(__VA_ARGS__)

#define FOR(x,to) for(x=0;x<to;x++)
#define FOR2(x,from,to) for(x=from;x<to;x++)
#define ZERO(a) memset(a,0,sizeof(a))
void _fill_int(int* p,int val,int rep) {int i;	FOR(i,rep) p[i]=val;}
#define FILL_INT(a,val) _fill_int((int*)a,val,sizeof(a)/4)
#define ZERO2(a,b) memset(a,0,b)
#define MINUS(a) _fill_int((int*)a,-1,sizeof(a)/4)
#define GETs(x) scanf("%s",x);
int GETi() { int i;scanf("%d",&i); return i;}
#define GET1(x) scanf("%d",x);
#define GET2(x,y) scanf("%d%d",x,y);
#define GET3(x,y,z) scanf("%d%d%d",x,y,z);

#define EPS (1e-11)
template <class T> T sqr(T val){ return val*val;}

//-------------------------------------------------------


int D,I,M,N;
char line[1000];
char data[41][41];
int step[12][12][4];
int array[101];


int cost2(int a,int b, int* w) {
	int d,cc,changec,step,stepc,sd,res,stepc2;
	
	d = abs(a-b);
	if(d<=M){
		*w=0;
		return 0;
	}
	
	changec = d-M;
	if(M==0) stepc=999999;
	else {
		stepc = (d/M) * I;
		stepc2 = ((d/M)-1)*I+(d%M);
		if(stepc2<stepc) stepc=stepc2;
	}
	
	
	res = changec; *w=changec;
	if(D<res) { res=D; *w = -2;}
	if(stepc<res) { res=stepc; *w = -3;}
	
	return res;
	
}

int cost3(int a,int b,int c,int* w2) {
	int cc,d2,d11,d12,d13,w,i,j,tc,k;
	
	if(abs(a-b)<=M && abs(b-c)<=M){ *w2=0; return 0;}
	//2‚ÂÁ‚·
	cc = D*2; *w2=-1000001;
	//1‚ÂÁ‚·
	d11 = D + cost2(b,c,&w); if(d11<cc){ cc=d11; *w2=-1000002;}
	d12 = D + cost2(a,c,&w); if(d12<cc){ cc=d12; *w2=-1000003;}
	d13 = D + cost2(a,b,&w); if(d13<cc){ cc=d13; *w2=-1000004;}
	if(cc==0) return cc;
	//Á‚³‚È‚¢
	FOR(i,256) {
		FOR(j,256) {
			tc = abs(i-a) + abs(j-b);
			if(tc>cc) continue;
			FOR(k,256) {
				tc = abs(i-a) + abs(j-b) + abs(k-c);
				if(tc>cc) continue;
				tc += cost2(i,j,&w) + cost2(j,k,&w);
				if(tc<cc) { cc=tc; *w2 = -(i*256+j);}
			}
		}
	}
	return cc;
}

void solve(int _loop) {
	int i,j,k,result,dir,ok,state,fstate,up,w;
	double br,tb1,tb2,start,end;
	
	GET2(&D,&I);
	GET2(&M,&N);
	ZERO(array);
	FOR(i,N) {
		GET1(&array[i]);
	}
	
	result=0;
	if(N==2) {
		result = cost2(array[0],array[1],&w);
	}
	else if(N==3){
		result = cost3(array[0],array[1],array[2],&w);
		
	}
	
end1:
	if(w<-1000000) _E("%d   %d %x %d %d\n",N,w,w,(-w)/256,(-w)%256);
	_PE("Case #%d: %d\n",_loop,result);
}

void init() {
}

int main(int argc,char** argv){
	int loop,loops;
	long long span;
	char tmpline[1000];
	struct timeval start,end,ts;
	
	if(argc>1) {
		freopen(argv[1], "r", stdin);
	}
	
	gettimeofday(&ts,NULL);
	
	GET1(&loops);
	gets(tmpline);
	init();
	
	for(loop=1;loop<=loops;loop++) {
		gettimeofday(&start,NULL);
		solve(loop);
		gettimeofday(&end,NULL);
		span = (end.tv_sec - start.tv_sec)*1000000LL + (end.tv_usec - start.tv_usec);
		_E("                                     time: %lld ms\n",span/1000);
	}
	
	start = ts;
	span = (end.tv_sec - start.tv_sec)*1000000LL + (end.tv_usec - start.tv_usec);
	_E("**Total time: %lld ms\n",span/1000);
	
	return 0;
	
}



