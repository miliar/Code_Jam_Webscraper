#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <assert.h>
#include <iomanip>
using namespace std;

//Compiled using MS VC++ 2005

/*
We will basically count the safe areas
assume the fly is a point and the wires are r+f thick instead. and the border is t+f thick
*/

double chordarea(double length,double radius){
	double theta=2.0*asin(length/(2*radius));
	assert(theta>0);
	double triarea=(length/2.0)*sqrt(radius*radius-length*length/4.0);
	return (radius*radius*theta/2.0-triarea);
}

double CalcProb(double f, double R, double t, double r, double g){
	const double PI=3.14159265358979323846;
	double safearea=0;
	double totalarea=PI*R*R;
	double sqwidth=g-2.0*f;
	double Rf=R-t-f;
	if (sqwidth==0)
		return 1;
	double nextsq=g+2.0*r;
	for(double y1=r+f;y1<Rf;y1+=nextsq){
		for (double x1=r+f;x1<sqrt(Rf*Rf-y1*y1);x1+=nextsq){
			double x2=x1+sqwidth;
			double y2=y1+sqwidth;
			if ((sqrt(x2*x2+y1*y1)<=Rf) && (sqrt(x1*x1+y2*y2)<=Rf) && (sqrt(x2*x2+y2*y2)<=Rf)){
				//whole square inside circle
				safearea+=sqwidth*sqwidth;
			}
			else if ((sqrt(x2*x2+y1*y1)<Rf) && (sqrt(x1*x1+y2*y2)<Rf) && (sqrt(x2*x2+y2*y2)>Rf)){
				//top right corner is out
				double c1=sqrt(Rf*Rf-y2*y2);	//(c1,y2)
				double c2=sqrt(Rf*Rf-x2*x2);	//(x2,c2)
				double s=sqrt((x2-c1)*(x2-c1)+(y2-c2)*(y2-c2));
				double area=sqwidth*(c1-x1)+(x2-c1)*(c2-y1)+(y2-c2)*(x2-c1)/2.0;
				area+=chordarea(s,Rf);
				safearea+=area;
			}
			else if ((sqrt(x2*x2+y1*y1)>Rf) && (sqrt(x1*x1+y2*y2)<Rf) && (sqrt(x2*x2+y2*y2)>Rf)){
				//right 2 corners out
				double c1=sqrt(Rf*Rf-y2*y2);	//(c1,y2)
				double c2=sqrt(Rf*Rf-y1*y1);	//(c2,y1)
				double s=sqrt((c2-c1)*(c2-c1)+(y2-y1)*(y2-y1));
				double area=sqwidth*((c2-x1)+(c1-x1))/2.0;
				area+=chordarea(s,Rf);
				safearea+=area;
			}
			else if ((sqrt(x2*x2+y1*y1)<Rf) && (sqrt(x1*x1+y2*y2)>Rf) && (sqrt(x2*x2+y2*y2)>Rf)){
				//top 2 corners out
				double c1=sqrt(Rf*Rf-x2*x2);	//(x2,c1)
				double c2=sqrt(Rf*Rf-x1*x1);	//(x1,c2)
				double s=sqrt((c2-c1)*(c2-c1)+(x2-x1)*(x2-x1));
				double area=sqwidth*((c2-y1)+(c1-y1))/2.0;
				area+=chordarea(s,Rf);
				safearea+=area;
			}
			else if ((sqrt(x2*x2+y1*y1)>Rf) && (sqrt(x1*x1+y2*y2)>Rf) && (sqrt(x2*x2+y2*y2)>Rf)){
				//3 corners out
				double c1=sqrt(Rf*Rf-x1*x1);	//(x1,c1)
				double c2=sqrt(Rf*Rf-y1*y1);	//(c2,y1)
				double s=sqrt((c2-x1)*(c2-x1)+(c1-y1)*(c1-y1));
				double area=((c1-y1)*(c2-x1))/2.0;
				area+=chordarea(s,Rf);
				safearea+=area;
			}
			else {
				//Error!!
				safearea+=0;
			}
		}
	}
	return 1.0-(4.0*safearea/totalarea);
}

//Takes the input file as only argument and spits to cout
int main (int argc,char* argv[]) {	
	int cs=0;	//# of cases
	ifstream infile;
	infile.open (argv[1], ifstream::in);
	infile>>cs;
	for (int c=0;c<cs;c++){
		double f,R,t,r,g;
		infile>>f>>R>>t>>r>>g;
		cout<<"Case #"<<(c+1)<<": "<<std::fixed << std::setprecision(6)<<CalcProb(f,R,t,r,g)<<endl;
	}
	//clean up
	infile.close();
	return 0;
}

