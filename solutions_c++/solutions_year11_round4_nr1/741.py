#include"stdlib.h"
#include"stdio.h"
#include <string>
#include<cmath>
#include<iostream>
#include<fstream>
#include <algorithm>
#include<iomanip>
using namespace std;

struct region{
	double len;
	double v;
	double time;
};
region co[2003]={0};

int cmp( const region &a, const region &b ){
    if( a.v < b.v )
       return 1;
    else
       return 0;
}


int main()
{
ifstream in;
ofstream out;
in.open("A-large.in");
out.open("OUTPUT.txt");

int T;
in>>T;

int X,S,R,N;
double t;
for(int Case=1;Case<=T;Case++){
	in>>X>>S>>R>>t>>N;
	int e0=0;
	int step=0;
		int s,e,w;
	for(int i=0;i<N;i++){

	in>>s>>e>>w;
	if(e0<s){
		co[step].len=s-e0;
		co[step].v=S;
		step++;
	}
	e0=e;
	co[step].len=e-s;
	co[step].v=w+S;
	step++;
	}
	if(e<X){
		co[step].len=X-e;
		co[step].v=S;
		step++;
	}
	N=step;
	sort(co,co+N,cmp);
	double total=0;
	for( i=0;i<N;i++){
		if(t>co[i].len/(co[i].v+R-S)){
			co[i].v+=R-S;
			t-=co[i].len/co[i].v;
			co[i].time=co[i].len/co[i].v;
			total+=co[i].time;
		}
		else if(t>0){
			co[i].time=t;
			co[i].len-=t*(co[i].v+R-S);
			co[i].time+=co[i].len/co[i].v;
			total+=co[i].time;
			t=-1;
		}
		else{
			total+=co[i].len/co[i].v;
		}
		
	}
	out<<"Case #"<<Case<<": "<<fixed<<setprecision(7)<<total<<endl;


}

in.close();
out.clear();
out.close();
return 0;
}