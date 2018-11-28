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


int N,M;
int U[1001];
int V[1001];

int Gs;
int G[10][9];
int Col[10];
int fix[10];
int mc;

int fincheck() {
	int i,j,k,l,l2;
	
	
	FOR(i,Gs) {
		k=0;
		FOR(j,N) {
			if(G[i][j]==0) continue;
			if(Col[j]==0) {
				return 0;
			}
			else {
				k |= 1<<(Col[j]-1);
			}
		}
		if(k!=((1<<mc)-1)) {
			return 0;
		}
	}
	return 1;
}

int colcheck() {
	int i,j,k,l;
	
	FOR(i,Gs) {
		k=l=0;
		FOR(j,N) {
			if(G[i][j]==0) continue;
			if(Col[j]==0) {
				l=1;
				break;
			}
			else {
				k |= 1<<(Col[j]-1);
			}
		}
		
		if(l==0 && k!=((1<<mc)-1)) {
			return 0;
		}
	}
	return 1;
}

int Check() {
	int i,j,k;
	j=-1;
	FOR(i,N) {
		if(Col[i]==0) {
			j=i;
			break;
		}
	}
	
	if(j==-1) {
		return fincheck();
	}
	else {
		if(colcheck()==0) {
			return 0;
		}
		FOR(i,mc) {
			Col[j]=i+1;
			k=Check();
			if(k==1) return 1;
			Col[j]=0;
		}
		return 0;
	}
	
}

void solve(int _loop) {
	int i,j,k,result,res,dir,ok,state,fstate,up,x,y,sp,dist1,dist2;
	int wid,hei,mv,mi;
	double br,tb1,tb2,start,end;
	
	ZERO(G);
	
	GET2(&N,&M);
	FOR(i,M) {
		U[i] = GETi()-1;
	}
	FOR(i,M) {
		V[i] = GETi()-1;
	}
	Gs=1;
	FOR(i,N) {
		G[0][i]=1;
	}
	
	FOR(i,M) {
		FOR(j,Gs) {
			if(!(G[j][U[i]] && G[j][V[i]])) continue;
			for(k=U[i];k<=V[i];k++) {
				if(G[j][k]==1) {
					G[j][k]=0;
					G[Gs][k]=1;
				}
			}
			G[j][U[i]]=G[j][V[i]]=1;
			Gs++;
			break;
		}
		
	}
	
	//Å¬‚Ì•Ó
	mv=9;mi=-1;
	FOR(i,Gs) {
		k=0;
		FOR(j,N) k+=G[i][j];
		if(k<mv){
			mi=i;
			mv=k;
		}
	}
	
	//Œˆ‚ß‚Ä‚µ‚Ü‚¤
	ZERO(fix);
	ZERO(Col);
	k=1;
	FOR(i,N) {
		if(G[mi][i]==1){
			fix[i]=1;
			Col[i]=k++;
		}
	}
	
	mc=mv;
	i=Check();
	_PE("Case #%d: %d\n",_loop,mc);
	FOR(i,N) {
		_PE("%d ",Col[i]);
	}
	_PE("\n");
	
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



