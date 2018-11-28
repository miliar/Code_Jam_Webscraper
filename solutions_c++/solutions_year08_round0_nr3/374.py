#include<iostream>
#include<fstream>
#include<string>
#include<cstdio>
#include<cmath>
#define PI 3.14159
#define PRECISION 1000000
using namespace std;

int main(int argc, char* argv[]){
  ifstream fin (argv[1]);
  FILE* fout =fopen(argv[2],"w");
  int numCases;
  double f,R,t,r,g;
  fin>>numCases;
  for(int thisCase=1;thisCase<=numCases;thisCase++){
    fin>>f>>R>>t>>r>>g;
    double radius=R-t-f;
    double str=r+f;
    double gap=g-2*f;
    double area=0;
    for(int col=1;col<radius/(2*str+gap)+2;col++)
      for(int row=1;row<radius/(2*str+gap)+2;row++){
	double square=0;
	double x=col*(2*str+gap)-str;
	double y=row*(2*str+gap)-str;
	if(x*x+y*y<=radius*radius){
	  area+=gap*gap;
	  continue;
	}
	double y_base=((row-1)*(2*str+gap)+str);
	double dist=gap/PRECISION;
	/*if(x<radius){
	  y=min(gap,pow(radius*radius-x*x,.5)-y_base);
	  if(y>0){
	    square+=y/2;
	  }
	  }*/
	for(int step=0;step<PRECISION;step++){
	  x-=dist;
	  if(x<radius){
	    y=min(gap,pow(radius*radius-x*x,.5)-y_base);
	    if(y>0){
	      square+=y;

	      //cout<<"got HERE value "<<square<<" with y"<<y<<"where gap is "<<
	      //gap<<"and pow is "<<pow(radius*radius-x*x,.5)<<"and base "<<
	      //(row-1)*(2*str+gap)+str<<endl;
	    }
	  }
	}
	//square-=y/2;
	//cout<<"Border "<<row<< " "<<col<<": "<<square*gap/PRECISION<<" out of "
	//  <<gap*gap<<endl;
	area+=square*gap/PRECISION;
	/*double x=col*(2*str+gap)-str;
	double y=row*(2*str+gap)-str;
	for(int n=PRECISION;n>0;n--){
	  x-=gap/PRECISION;
	  y-=gap/PRECISION;
	  if(x*x+y*y<radius*radius){
	    area+=(n*gap/PRECISION)*gap;
	    break;
	    }*/
      
      }
    
    fprintf(fout,"Case #%d: %.6f\n",thisCase,1-(4*area/(PI*R*R)));
  }
  return 0;
}
