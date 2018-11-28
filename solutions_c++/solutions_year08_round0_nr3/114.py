#include <iostream>
#include <fstream>
#include <cmath>
#include <iomanip>
using namespace std;

int main(int argc, char *argv[]) {
	ifstream fin("C-large.in");
	ofstream fout("C-large.out");
	int n;
	fin>>n;
	for (int i=0;i<n;i++) {
		double f,R,t,r,g;
		fin>>f>>R>>t>>r>>g;
		double Rtf=R-t-f;
		double aux_p=(R-t-f)*(R-t-f)/(2);
		double agn=0;
		double ax=r+f;
		while (ax<Rtf) {
			double ay=r+f;
			while (ay*ay+ax*ax<Rtf*Rtf) {
				
				double x1=ax, x2=ax+g-f-f;
				double y1=ay, y2=ay+g-f-f;
				
				if (x2<=x1 || y2<=y1) {
					ay+=g+r+r;
					continue;
				}
				
				double cx1y=x1>Rtf?-1:sqrt(Rtf*Rtf-x1*x1);
				double cx2y=x2>Rtf?-1:sqrt(Rtf*Rtf-x2*x2);
				double cy1x=y1>Rtf?-1:sqrt(Rtf*Rtf-y1*y1);
				double cy2x=y2>Rtf?-1:sqrt(Rtf*Rtf-y2*y2);
//				cout<<cx1y<<"  "<<cx2y<<"   "<<cy1x<<"  "<<cy2x<<endl;
				if (cx1y<y1||cx1y>y2) cx1y=-1;
				if (cx2y<y1||cx2y>y2) cx2y=-1;
				if (cy1x<x1||cy1x>x2) cy1x=-1;
				if (cy2x<x1||cy2x>x2) cy2x=-1;
				
				if (cy1x<0 && cy2x<0 && cx1y<0 && cx2y<0) {
//					cout<<"F";
					agn+=(g-f-f)*(g-f-f);
				} else if (cx1y>=0 && cy1x>=0) {
//					cout<<"1";
					double xi1 = y1*x1/cx1y;
					double a1 = atan2(xi1,y1);
					double a2 = atan2(cy1x,y1);
					double da = a1>a2?a1-a2:a2-a1;
					double ap = aux_p*da;
					double apt = (cy1x*y1-xi1*y1)/2;
					double al1 = (x1-xi1)*(cx1y-y1)/2;
					double af = ap-apt-al1;
					agn+=af;
					if (af>(g-f-f)*(g-f-f) || af<0) cout<<"  MAAAAL  1  ";
				} else if (cx1y>=0 && cx2y>=0) {
//					cout<<"2";
					double a1 = atan2(x1,cx1y);
					double a2 = atan2(x2,cx2y);
					double da = a1>a2?a1-a2:a2-a1;
					double ap = aux_p*da;
					double xi1 = y1 * x1 / cx1y;
					double xi2 = y1 * x2 / cx2y;
					double apt = (xi2*y1-xi1*y1)/2;
					double al1 = (x1-xi1)*(cx1y-y1)/2;
					double al2 = (x2-xi2)*(cx2y-y1)/2;
					double af = ap-apt-al1+al2;
//	cout<<af<<"  "<<ap<<"  "<<apt<<"  "<<al1<<"  "<<al2<<endl;
					agn+=af;
					if (af>(g-f-f)*(g-f-f) || af<0) cout<<"  MAAAAL  2  ";
				} else if (cy2x>=0 && cx2y>=0) {
//					cout<<"3";
					double a1 = atan2(x2,cx2y);
					double a2 = atan2(cy2x,y2);
					double da = a1>a2?a1-a2:a2-a1;
					double ap = aux_p*da;
					double xi1 = y1 * cy2x / y2;
					double xi2 = y1 * x2 / cx2y;
					double apt = (xi2*y1-xi1*y1)/2;
					double al1,al2;
					if (xi1<x1)  {
						if (xi2<x1) {
							double yi1 = x1 * cx2y / x2;
							double yi2 = x1 * y2 / cy2x;
							al1 = (yi1-y1)*(x2-x1)+(x2-x1)*(cx2y-yi1)/2;
							al2 = ( (cy2x-x1)*(y2-yi2)-(yi2-y1)*(x1-xi1) +(yi1-y1)*(x1-xi2))/2;
						} else {
							al1 = (x2-xi2)*(cx2y-y1)/2;
							double yi1 = x1 * y2 / cy2x;
							al2 = ((cy2x-x1)*(y2-yi1)-(x1-xi1)*(yi1-y1))/2;
						}
					} else {
						al1 = (x2-xi2)*(cx2y-y1)/2;
						al2 = (y2-y1)*(xi1-x1)+(cy2x-xi1)*(y2-y1)/2;
					}
					double af = ap-apt+al1+al2;
//					cout<<"  "<<af/(x2-x1)/(y2-y1)<<endl;
					agn+=af;
					if (af>(g-f-f)*(g-f-f) || af<0) cout<<"  MAAAAL  3  ";
				} else if (cy1x>=0 && cy2x>=0) {
//					cout<<"4";
					double a1 = atan2(y1,cy1x);
					double a2 = atan2(y2,cy2x);
					double da = a1>a2?a1-a2:a2-a1;
					double ap = aux_p*da;
					double yi1 = x1 * y1 / cy1x;
					double yi2 = x1 * y2 / cy2x;
					double apt = (yi2*x1-yi1*x1)/2;
					double al1 = (y1-yi1)*(cy1x-x1)/2;
					double al2 = (y2-yi2)*(cy2x-x1)/2;
					double af = ap-apt-al1+al2;
					agn+=af;
					if (af>(g-f-f)*(g-f-f) || af<0) cout<<"  MAAAAL  4  ";
				} else {
					cout<<"  OTRO!!!  \n";
//					cout<<cx1y<<"  "<<cx2y<<"   "<<cy1x<<"  "<<cy2x<<endl;
				}
				ay+=g+r+r;
			}
			ax+=g+r+r;
		}
		double p=1-4*agn/(R*R*M_PI);
//		if (p>1) p=1;
//		if (p<0.000001) p=0;
		
		cout<<"Case #"<<i+1<<": "<<setprecision(6)<<fixed<<p<<endl;		
		fout<<"Case #"<<i+1<<": "<<setprecision(6)<<fixed<<p<<endl;		
	}
	fout.close();
	fin.close();
	return 0;
}

