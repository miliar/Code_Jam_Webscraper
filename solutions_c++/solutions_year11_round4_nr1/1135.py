#include <stdio.h>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <stdio.h>
#include <sstream>
#include <string>
#include <string.h>
#include <vector>
#include <math.h>
#include <map>
#define MaxLength INT_MAX
#define MaxNode 12
#define MN 1005
using namespace std;
struct ww{
	double b,e,w,x;
	
}typedef WalkWay;
WalkWay w[MN];

int M,T,N,D,L,H;
double X,S,R,t;

int cmp(const void* x, const void * y){
	WalkWay * a = (WalkWay *) x;
	WalkWay * b = (WalkWay *) y;
	if(a->w > b->w)
		return 1;
	else
		if(a->w < b->w)
			return -1;
	return 0;
}
int main(){
	int i,j,k,len,tt,n,m,maxv,minv;
	double result,temp,a,b;
	int x,y,r;
	scanf("%d",&T);

	for(tt=1; tt<=T;tt++){
		result =0;
		scanf("%lf %lf %lf %lf %d", &X, &S, &R, &t ,&N);
		for(i=0; i<N;i++){
			scanf("%lf %lf %lf",&w[i].b,&w[i].e,&w[i].w);
			X = X - w[i].e + w[i].b;
			w[i].x = w[i].e - w[i].b;
		}
		w[N].x = X;
		w[N].w = 0;
		N++;
		qsort(w,N,sizeof(WalkWay),cmp);


		for(i=0; i<N;i++)
			if(t>0){
				if(w[i].x/(w[i].w+R) > t){
					result += t;
					w[i].x -= (w[i].w+R) * t;
					result += w[i].x/(w[i].w+S);
					t=0;
				}else{
					result += w[i].x/(w[i].w+R);
					t -= w[i].x/(w[i].w+R);
				}
			}
			else
				result += w[i].x / (w[i].w+S);


		printf("Case #%d: %.12lf\n",tt, result);
	}

	return 0;
}
