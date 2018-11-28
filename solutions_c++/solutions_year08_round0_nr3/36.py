#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

const double pi=3.1415926535897932384626433832795;

double f,R,t,r,g,lado,x,y;

inline bool in(double a, double b){
	return a*a+b*b<R*R;
}

double calc(){
	if (in(x+lado,y+lado)) return lado*lado;
	vector<double> xx,yy;
	xx.push_back(x); yy.push_back(y);
	int i,tam,pos;
	if (in(x+lado,y)){
		xx.push_back(x+lado); yy.push_back(y);
		pos=2;
		double tmp=sqrt(R*R-(x+lado)*(x+lado));
		xx.push_back(x+lado); yy.push_back(tmp);
	}else{
		pos=1;
		double tmp=sqrt(R*R-y*y);
		xx.push_back(tmp); yy.push_back(y);
	}
	
	if (in(x,y+lado)){
		double tmp=sqrt(R*R-(y+lado)*(y+lado));
		xx.push_back(tmp); yy.push_back(y+lado);
		xx.push_back(x); yy.push_back(y+lado);
	}else{
		double tmp=sqrt(R*R-x*x);
		xx.push_back(x); yy.push_back(tmp);
	}
	tam=xx.size();
	double dosarea=0.0;
	
	for (i=0;i<tam;i++){
		if (i==pos){
			double sig=(((xx[i]*yy[(i+1)%tam]-xx[(i+1)%tam]*yy[i])>0)?1.0:-1.0);
			double b2=(xx[i]-xx[(i+1)%tam])*(xx[i]-xx[(i+1)%tam])+(yy[i]-yy[(i+1)%tam])*(yy[i]-yy[(i+1)%tam]);
			double alfa=acos(1.0-(b2/(2*R*R)));
			dosarea+=sig*alfa*R*R;
		}else{
			dosarea+=xx[i]*yy[(i+1)%tam]-xx[(i+1)%tam]*yy[i];
		}
	}
	return abs(dosarea)/2.0;
}

int main(){
	int casos,c;
	
	cin>>casos;
	for (c=1;c<=casos;c++){
		cin>>f>>R>>t>>r>>g;
		
		double prob=0.0,total=pi*R*R;
		
		lado=g-2*f;
		R-=t+f;
		if (lado<=0 || R<=0){
			printf("Case #%d: %.10f\n",c,1.0);
		}else{
			x=r+f;
			while (x<R){
				y=r+f;
				while (in(x,y)){
					prob+=calc();
					y+=g+2*r;
				}
				x+=g+2*r;
			}
			double rta=1.0-(4.0*prob/total);
			printf("Case #%d: %.10f\n",c,rta);
		}
	}
	return 0;
}
