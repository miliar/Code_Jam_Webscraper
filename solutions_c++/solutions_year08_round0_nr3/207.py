#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;

long long puppa(string a) {
	long long r=0;
	bool f=false;
	int k=0;
	for (int i=0; i<a.size(); i++) {
		if (f) k++;
		if (a[i]!='.') {r*=10; r+=a[i]-'0';}
		else f=true;
		}
	for (; k<6; k++) r*=10;
	return r;
	}

double quarto(double R) {
	return (R*R*3.141592653589793)/4.0;
	}

int main (void) {
    ofstream OUT;
    OUT.open ("OU.txt");
    ifstream FILE("IN.txt");
    int Num;
    FILE>>Num;
	for (int z=1; z<=Num; z++) {
		string f0, R0, t0, r0, g0;
		FILE>>f0>>R0>>t0>>r0>>g0;
		long long f1,R1,t1,r1,g1;
		f1=puppa(f0);
		R1=puppa(R0);
		t1=puppa(t0);
		r1=puppa(r0);
		g1=puppa(g0);
		long long a2, b2, p2, r2, R2;
		a2=r1+f1;
		b2=g1-2*f1;
		p2=r1*2+g1;
		R2=R1;
		r2=R2-t1-f1;
		
		if (b2<=0 || r2<=0) {cout<<"MERDA\n"; OUT<<"Case #"<<z<<": "<<"1.000000"<<"\n";}
		else {
			double a=(double)a2/1000000, b=(double)b2/1000000, p=(double)p2/1000000, r=(double)r2/1000000, R=(double)R2/1000000;
	//		cout<<a<<" "<<b<<" "<<p<<" "<<r<<" "<<R<<"\n";
			
			double AREA=0;
			double areetta=b*b;
			for (double x=a; x<r; x+=p) {
				for (double y=a; y<r; y+=p) {
					if (sqrt(pow(x,2.0)+pow(y,2.0))>r) y=2.0*r;
					else if (sqrt(pow(x+b,2.0)+pow(y+b,2.0))<=r) AREA+=areetta;
					else {
						pair<double,double> j,k;
						if (sqrt(pow(x+b,2.0)+pow(y,2.0))>r) {j.second=y; j.first=sqrt(pow(r,2.0)-pow(y, 2.0));}
						else {j.first=x+b; j.second=sqrt(pow(r,2.0)-pow(x+b, 2.0));}
						if (sqrt(pow(x,2.0)+pow(y+b,2.0))>r) {k.first=x; k.second=sqrt(pow(r,2.0)-pow(x, 2.0));}
						else {k.second=y+b; k.first=sqrt(pow(r,2.0)-pow(y+b, 2.0));}
						double area=acos((j.first*k.first+j.second*k.second)/pow(r,2.0))*pow(r,2.0);
						area+=y*(x+b-j.first)+(x+b)*(j.second-y);
						area+=x*(y+b-k.second)+(y+b)*(k.first-x);
						area-=y*b+x*b;
						area*=0.5;
						if (area>areetta) cout<<"MERDAMERDAMERDAMERDA!!!!!!!!!" <<area<<" "<<areetta<<"\n\n";
						AREA+=area;
						}
					}
				}

			double AA=1.0-(AREA)/quarto(R);
			if (AA<0.0000005) OUT<<"Case #"<<z<<": "<<0.000000<<"\n";
			else OUT<<"Case #"<<z<<": "<<AA<<"\n";
			cout<<z<<" "<<AA<<"\n";
			}
        	}
    FILE.close();
    OUT.close();
    system("PAUSE");
    return 0;
    }
