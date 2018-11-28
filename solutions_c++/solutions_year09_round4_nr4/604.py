#include <iostream>
#include <algorithm>
#include <cmath>
#include <fstream>
#include <complex>
using namespace std;

ifstream fin("d.in");
ofstream fout("d.out");

int T;

typedef complex<double> P;

P A,B,C;
double ra,rb,rc;
int n;

int main() {
	fin>>T;
	int t;
	for(t=1;t<=T;++t) {
		fin>>n;
		double x,y;
		double ret,tmp;
		if(n==1) {
			fin>>x>>y;
			A = P(x,y);
			fin>>ra;
			ret = ra;
		}
		else if(n==2) {
			fin>>x>>y;
			A = P(x,y);
			fin>>ra;
			fin>>x>>y;
			B = P(x,y);
			fin>>rb;
			ret = ra;
			if(rb>ret)ret=rb;
		}
		else {
			fin>>x>>y;
			A = P(x,y);
			fin>>ra;

			fin>>x>>y;
			B = P(x,y);
			fin>>rb;

			fin>>x>>y;
			C = P(x,y);
			fin>>rc;

			tmp = abs(A-B) + ra + rb;
			tmp *= 0.5;
			if(tmp<rc)tmp=rc;
			ret = tmp;

			tmp = abs(A-C) + ra + rc;
			tmp *= 0.5;
			if(tmp<rb)tmp=rb;
			if(tmp<ret)ret=tmp;

			tmp = abs(B-C) + rb + rc;
			tmp *= 0.5;
			if(tmp<ra)tmp=ra;
			if(tmp<ret)ret=tmp;
		}

			fout.setf(ios::floatfield,ios::fixed);
			fout.precision(9);
			fout<<"Case #"<<t<<": "<<ret<<endl;
	}
	return 0;
}
