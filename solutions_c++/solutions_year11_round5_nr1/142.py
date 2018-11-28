/* Author: Zuo.Overmind.Zerg */
#include<cassert>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
//#include<deque>
//#include<functional>
//#include<iostream>
//#include<list>
//#include<map>
//#include<set>
//#include<vector>
using namespace std;

typedef long long i64;
typedef unsigned u32;
template<class _> void maz(_ &a,const _ b) {if(b>a)a=b;}
template<class _> void miz(_ &a,const _ b) {if(b<a)a=b;}

const int LMAX=100;
const int UMAX=100;

typedef struct {
	int x,y;
} Point;

int W,G;
int L; Point LP[LMAX];
int U; Point UP[UMAX];

double area(double left,double right) {
	int i,x1,y1,x2,y2; double m,x3,y3,x4,y4,ret=0;
	if(left<0)left=0;
	if(right>W)right=W;
	if(left>=right)return 0;
	for(i=1;i<U;i++) {
		x1=UP[i-1].x;y1=UP[i-1].y;
		x2=UP[i  ].x;y2=UP[i  ].y;
		if(x1>=right||x2<=left)continue;
		x3=max((double)x1,left);
		x4=min((double)x2,right);
		if(x3>=x4)continue;
		m=(double)(y2-y1)/(x2-x1);
		y3=m*(x3-x1)+y1;
		y4=m*(x4-x1)+y1;
		ret+=(y3+y4)*(x4-x3)/2;
	}
	for(i=1;i<L;i++) {
		x1=LP[i-1].x;y1=LP[i-1].y;
		x2=LP[i  ].x;y2=LP[i  ].y;
		if(x1>=right||x2<=left)continue;
		x3=max((double)x1,left);
		x4=min((double)x2,right);
		if(x3>=x4)continue;
		m=(double)(y2-y1)/(x2-x1);
		y3=m*(x3-x1)+y1;
		y4=m*(x4-x1)+y1;
		ret-=(y3+y4)*(x4-x3)/2;
	}
	return ret;
}

void solve() {
	double TotalArea=area(0,W);
	double EachArea=TotalArea/G;
	double saki=0;
	int i; double _l,_r,_m,test;
	for(i=1;i<G;i++) {
		_l=saki;
		_r=W;
		while(_r-_l>1e-9) {
			_m=(_l+_r)/2;
			test=area(saki,_m);
			if(test>=EachArea)_r=_m;
			else _l=_m;
		}
		_m=(_l+_r)/2+1e-12;
		printf("%.9f\n",_m);
		saki=_m;
	}
}

void input() {
	int i;
	scanf("%d%d%d%d",&W,&L,&U,&G);
	for(i=0;i<L;i++)scanf("%d%d",&LP[i].x,&LP[i].y);
	for(i=0;i<U;i++)scanf("%d%d",&UP[i].x,&UP[i].y);
}

int main() {
	int T,S;
	scanf("%d",&T);
	for(S=1;S<=T;S++) {
		input();
		printf("Case #%d:\n",S);
		solve();
	}
	return 0;
}
