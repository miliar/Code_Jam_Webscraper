#include <iostream>
#include <complex>
#include <iomanip>
using namespace std;

typedef std::complex<double> P;
#define PI 3.14159265358979


int main(){
	int n,i,x,y;
	double f,R,RR,t,r,g;
	double p,s;
	cout.setf(ios_base::fixed, ios_base::floatfield);
    cout << setprecision(8);
	cin >> n;
	for (i=0;i<n;i++) {
		cin >> f >> RR >> t >> r >> g;
		s=0;
		double R=RR-t-f , sz=g-f*2;
		if (sz>0 && R>0)
		for (y=0;y<(int)(R/(g+2*r))+1;y++) {
			double py=y*(g+2*r)+r+f;
			for (x=0;x<(int)(R/(g+2*r))+1;x++) {
				double px=x*(g+2*r)+r+f;
				P p(px,py);
				if (abs(p)>=R) continue;
				if (abs(p+P(sz,sz))<=R) {
					s+=sz*sz; continue;
				}

				double t1,t2;
				if (abs(p+P(sz,0))>=R) {
					t1=asin(py/R);
				} else {
					t1=acos((px+sz)/R);
				}
				if (abs(p+P(0,sz))>=R) {
					t2=acos(px/R);
				} else {
					t2=asin((py+sz)/R);
				}
				P p1=P(cos(t1)*R,sin(t1)*R);
				P p2=P(cos(t2)*R,sin(t2)*R);
				double mx=p1.real(), my=p2.imag();
				double s1=R*R*(t2-t1)/2;
				double s2=R*R*sin(t2-t1)/2;
				double s4=(mx-p2.real())*(my-p1.imag())/2;
				double s3=s4-(s1-s2);
				s+=(mx-px)*(my-py) - s3;
			}
		}

		cout << "Case #" <<  i+1 << ": " << (RR*RR*PI-s*4)/(RR*RR*PI) << endl;
	}
}
