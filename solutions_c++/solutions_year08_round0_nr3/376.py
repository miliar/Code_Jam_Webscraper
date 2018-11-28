#include <iostream>
#include <fstream>
#include <string.h>
#include <math.h>
using namespace std;

double pi=3.141592653589;

double my_int(double x, double R)
{
	if(fabs(x-R)<1e-5)return pi*R*R/4;
	//cout <<"\natat "<<1/2*(atan(x/sqrt(R*R-x*x))*R*R+x*sqrt(R*R-x*x)) <<"\n";
  return 0.5*(atan(x/sqrt(R*R-x*x)) * R*R +x*sqrt(R*R-x*x) );
}
double tri_area(double x, double y, double R)
{
	double x2 = sqrt(R*R-y*y);
	//cout<< "x="<<x<<" y="<<y<<" x2="<<x2<<" r="<<R<<" res "<<my_int(x2,R)<<" "<<my_int(x,R);
	return my_int(x2,R)-my_int(x,R)-y*(x2-x);
}

double rect_area(double x1, double y1, double x2, double  y2,double  R)
{
	//cout <<777;
	return my_int(x2,R)-my_int(x1,R)-y1*(x2-x1);
}
double pent_area(double x1, double y1, double x2,double  y2,double  R)
{
	double x3 = sqrt(R*R-y2*y2);
	double tri_area = y2*(x2-x3) - (my_int(x2,R)-my_int(x3,R));
	//cout<< "x1="<<x1<<" y1="<<y1<<" x3="<<x3<<" res "<<(x2-x1)*(x2-x1)-tri_area;
	return (x2-x1)*(x2-x1)-tri_area;
}


double get_squares(double f, double R, double t, double r, double g)
{
	int ns = int(ceil((R-t-f) / (g+2*r)));
	double a=R-t-f;
	double area = 0;
	for(int i=0; i<ns; i++){
		for(int j=0; j<ns; j++){
			double x1 = (g+2*r)*i+r+f;
			double  y1 = (g+2*r)*j+r+f;
			double x2 = (g+2*r)*i+r+g-f;
			double  y2 = (g+2*r)*j+r+g-f;
	//cout<< "x1="<<x1<<" y1="<<y1<<" x2="<<x2<<" y2="<<y2<<"\n";

			if (x2*x2+y2*y2<=a*a){ //inside
				area+=(x2-x1)*(x2-x1);
			}else{
				if(x1*x1+y1*y1>=a*a){ //outside
				}else{//intersect
					if(x2*x2+y1*y1<=a*a){//lrcorner inside
						if(x1*x1+y2*y2<=a*a){ //ul corner inside
							area+=pent_area(x1,y1,x2,y2, a);
						}else{// ulcorner outside
							area+=rect_area(x1,y1,x2,y2, a);
						}
										
					}else{// lrcorner outside
						if(x1*x1+y2*y2<=a*a){ //ul corner inside
							area+=rect_area(y1,x1,y2,x2, a);
						}else{// ulcorner outside
							area+=tri_area(x1,y1, a);
						}
					}
				}
			}
		}
	}
	return area*4;
}


int main () {
	//string line;
	//cout <<my_int(1,1);
	int cases;
	cin >> cases;
	for (int j=1; j<=cases; j++){
		double f, R, t, r, g ;
		
		cin >> f>> R>> t>> r>>g; cin.get();
	//	cout << f<<"   "<<g<<"\n";
		double result, result1;
		if((2*f>=g) || r+f>=R-t){
			result =1;
		}else{
			result1 = 1-(g-2*f)*(g-2*f) /   (2*r+g)/ (2*r+g)  *(R-t)*(R-t)/R/R ;
	//		cout<< "squares "<<get_squares(f, R, t,r,g )<<"\n";
			result = 1-get_squares(f, R, t,r,g )/R/R/pi;
		}
		cout.precision(6);
cout.setf(ios::fixed,ios::floatfield);
		cout<<"Case #"<<j<<": "<<result<<"\n";
	}
}