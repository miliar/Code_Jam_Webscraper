#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<limits.h>
#include<iostream>
#include<iomanip>
#include<sstream>
#include<algorithm>
#include<functional>
#include<vector>
#include<string>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<complex>
#define EPS (1e-9)
#define PI (3.141592653589793238)
#define MP make_pair
typedef long long ll;
using namespace std;

int w,l,u,g;
int lx[200],ly[200],ux[200],uy[200];
double ld[200],ud[200];

double calc(double line){
	int i,j,k;
	double ans=0;
	double nly=ly[0],nld=ld[0],nuy=uy[0],nud=ud[0];
	int lpos=0,upos=0;
	bool end=false;
	for(i=1;i<=w;i++){
		double dx=(double)i;
		if(line<dx){dx=line;end=true;}
		double haba=dx-(i-1);
		double puy=nuy+nud*haba;
		double ply=nly+nld*haba;
		double ue=nuy-nly;
		double sita=puy-ply;
		ans+=(ue+sita)*haba/2;
		if(end)break;
		nly=ply;
		nuy=puy;
		if(lx[lpos+1]==i){
			nld=ld[lpos+1];
			lpos++;
		}
		if(ux[upos+1]==i){
			nud=ud[upos+1];
			upos++;
		}
	}
	return ans;
}

int main(void){
	int T;
	scanf("%d",&T);
	for(int casenum=1;casenum<=T;casenum++){
		int i,j,k;
		scanf("%d %d %d %d",&w,&l,&u,&g);
		for(i=0;i<l;i++){
			scanf("%d %d",&lx[i],&ly[i]);
		}
		for(i=0;i<u;i++){
			scanf("%d %d",&ux[i],&uy[i]);
		}
		for(i=0;i<l-1;i++){
			ld[i]=((double)ly[i+1]-ly[i])/((double)lx[i+1]-lx[i]);
		}
		for(i=0;i<u-1;i++){
			ud[i]=((double)uy[i+1]-uy[i])/((double)ux[i+1]-ux[i]);
		}
		double allarea=calc(w);
		printf("Case #%d:\n",casenum);
		for(i=1;i<=g-1;i++){
			double area=allarea/g*i;
			double up=w,down=0,mid;
			for(j=0;j<=100;j++){
				mid=(up+down)/2;
				double x=calc(mid);
				if(area<x){
					up=mid;
				}else{
					down=mid;
				}
			}
			printf("%.12lf\n",mid);
		}
	}
	return 0;
}
