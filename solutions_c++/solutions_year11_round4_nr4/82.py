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


int P,W;
int X[1001];
int Y[1001];
int mat[1001][1001];
int minc,maxt;
int visited[37];

int num_threat(){
	int i,j,t;
	int threat[37];
	
	ZERO(threat);
	t=0;
	FOR(i,P) {
		if(!visited[i]) continue;
		FOR(j,P) {
			if(i!=j && !visited[j] && !threat[j] && mat[i][j]) {
				t++;
				threat[j]=1;
			}
		}
	}
	return t;
	
}


void search(int depth, int planet) {
	int i,j,k;
	if(mat[planet][1]) {
		//ê™ïûäÆóπ
		if(depth<minc) {
			minc = depth;
			maxt = num_threat();
		}
		else if(depth==minc) {
			i = num_threat();
			if(i>maxt) maxt=i;
		}
		return;
	}
	
	//Ç±ÇÍà»è„ÇÕÉÄÉ_
	if(depth>=minc) return;
	
	//íTçı
	for(i=0;i<P;i++) {
		if(mat[planet][i] && visited[i]==0) {
			visited[i]=1;
			search(depth+1,i);
			visited[i]=0;
			if(depth>=minc) return;
			
		}
	}
	
}

void solve(int _loop) {
	int i,j,k,result,res,dir,ok,state,fstate,up,x,y,sp,dist1,dist2;
	int wid,hei,mv,mi;
	double br,tb1,tb2,start,end;
	
	ZERO(mat);
	GET2(&P,&W);
	FOR(i,W) {
		scanf("%d,%d", &X[i],&Y[i]);
		mat[X[i]][Y[i]]=mat[Y[i]][X[i]]=1;
	}
	
	minc = 999;
	maxt = 0;
	ZERO(visited);
	visited[0]=1;
	search(0,0);
	
	_PE("Case #%d: %d %d\n",_loop,minc,maxt);
	
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



